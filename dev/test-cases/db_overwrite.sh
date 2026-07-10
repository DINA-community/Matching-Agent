#!/bin/bash

# Check if an argument was provided
if [[ -z "$1" ]]; then
	echo "Please provide ad database. Usage: $0 <new db>"
	exit 1
fi

if [[ "$(dirname "$1")" == "." ]]; then
	echo "It seems you provided a filename: $1"
	if [[ -f "$1" ]]; then
		echo "File was found in the folder"
	else
		echo "However, it is not in the folder"
	fi
else
	echo "Please provide a database in the folder of the script."
	exit 1
fi

echo "You provided file: $1"
read -r -p "The current database will be deleted. Do you want to proceed? [y/n]: " confirm

case "${confirm,,}" in
[yY] | [yY][eE][sS]) echo "Let's replace some data..." ;;
"" | [nN] | [nN][oO])
	echo "Abort"
	exit 1
	;;
*) echo "Please answer y or n." ;;
esac

full_container=$(docker ps -a --format "{{.Names}}" | grep -i postgres-1 | head -n1)

if [ -z "$full_container" ]; then
	echo "No postgres container found!"
	exit 1
fi

# Extract the prefix by removing '-postgres-1'
prefix="${full_container%-postgres-1}"
echo "Detected prefix: $prefix"

## In this setting it must be dev
if [[ $prefix != "dev" ]]; then
	echo "$prefix does not seems right for the development setup. Exit."
	exit 1
fi

docker start "${prefix}-postgres-1"
sleep 3
docker exec "${prefix}-postgres-1" dropdb -U netbox netbox
docker exec "${prefix}-postgres-1" createdb -U netbox netbox

# Check for custom binary dump first (magic bytes PGDMP)
if head -c 5 "$1" 2>/dev/null | grep -q "PGDMP"; then
	echo "Detected: pg_dump custom format → use pg_restore"
	docker exec -i "${prefix}-postgres-1" pg_restore -v --clean -d netbox -U netbox <$1 2>"err_db_${1}.log"
else
	# Check if it's a readable text file
	if file "$1" | grep -q "ASCII text\|UTF-8 text"; then
		echo "Detected: plain SQL text → use psql"
		docker exec -i "${prefix}-postgres-1" psql -U netbox <$1 >/dev/null 2>"err_db_${1}.log"
	else
		echo "Unknown dump format!"
		exit 1
	fi
fi

# Remove netbox-setup so it can run a clean setup after import.
if docker ps -a --format "{{.Names}}" | grep -Fxq "netbox-setup"; then
	docker rm -f "netbox-setup"
fi

cat <<HINT
In case of trouble, this might help:
docker exec netbox python3 manage.py migrate
HINT
