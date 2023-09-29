#!/usr/bin/bash
# request and display the size of the body of the response

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
res=$(mktemp)
curl -s -o "$res" "$1"
res_size=$(stat -c%s "$res")

echo "$res_size"
