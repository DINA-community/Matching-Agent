#!/bin/bash

cat >&2 <<USAGE
This script will install a small netbox db for testing the matching agent and the CSAF Handler.
Also relevant csaf documents will be downloaded.
###############################################
#### The current database will be deleted! ####
###############################################
USAGE

CSAF_FILES=(
    "https://cert-portal.siemens.com/productcert/csaf/ssa-674753.json"
    "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2024/icsa-24-338-04.json"
    "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2024/icsa-24-352-04.json"
    "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2025/icsa-25-007-01.json"
    "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2025/icsa-25-345-03.json"
	"https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2026/icsa-26-008-01.json"
	"https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2025/icsma-25-364-01.json"
    )


get_csaf() {
	OUTPUT_DIR="./csaf_files"
	mkdir -p "$OUTPUT_DIR"

	# Download each file
	errors=0
	for url in "${CSAF_FILES[@]}"; do
		filename=$(basename "$url")
		filepath="$OUTPUT_DIR/$filename"

		if [ -f "$filepath" ]; then
			continue
		fi
		echo "Downloading: $filename"
		sleep 1
		if wget -q "$url"; then
			mv $filename $filepath
			echo "  ✓ Success"
		else
			if [ -f $filename ] && ["$(wc -c < "$file")" -eq 0 ]; then
  		  		rm $filename
			fi
			echo "  ✗ Failed to download"
			((errors++))
		fi
	done
	echo ""
	echo "Download complete!"
	echo "Files saved to: $OUTPUT_DIR/"

	if [ $errors -gt 0 ]; then
		echo "Warning: $errors file(s) failed to download."
		exit 1
	else
		echo "All files downloaded successfully."
	fi
}


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

get_csaf

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

docker stop "${prefix}-postgres-1"
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
