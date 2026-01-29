#!/bin/bash

# Check if an argument was provided
if [ -z "$1" ]; then
    echo "Please provide ad database. Usage: $0 <new db>"
    exit 1
fi

if [ -n "$2" ]; then
    confirm="$2"
else
    # Prompt the user if no second argument
    echo "You provided file: $1"
    read -r -p "The current database will be deleted. Do you want to proceed? [y/n]: " confirm
fi

case "${confirm,,}" in
    y|yes) echo "Continuing...";;
    n|no)  echo "Aborting."; exit 1;;
    *)     echo "Invalid response. Please answer y or n."; exit 1;;
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

if [[ $prefix != "dev" ]];then
    echo "$prefix does not seems right for the development setup. Exit."
    exit 1
fi

docker start "${prefix}-postgres-1"
sleep 3 # Avoid following error (Please validate JANEK)
#dropdb: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
	#Is the server running locally and accepting connections on that socket?
#createdb: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
#	Is the server running locally and accepting connections on that socket?


docker exec "${prefix}-postgres-1" dropdb -U netbox netbox
docker exec "${prefix}-postgres-1" createdb -U netbox netbox

# Check for custom binary dump first (magic bytes PGDMP)
if head -c 5 "$1" 2>/dev/null | grep -q "PGDMP"; then
    echo "Detected: pg_dump custom format → use pg_restore"
    docker exec -i "${prefix}-postgres-1" pg_restore -v --clean -d netbox -U netbox < $1  2> "err_db_${1}.log"
else
    # Check if it's a readable text file
    if file "$1" | grep -q "ASCII text\|UTF-8 text"; then
        echo "Detected: plain SQL text → use psql"
        docker exec -i "${prefix}-postgres-1" psql -U netbox < $1  > /dev/null 2> "err_db_${1}.log"
    else
        echo "Unknown dump format!"
        exit 1
    fi
fi


# docker exec netbox python3 manage.py migrate