#!/bin/bash
# Sending DELETE request to a server and displaying the response

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL="$1"
res=$(mktemp)
curl -X DELETE -s -o "$res" "$URL"
cat "$res"
rm "$res"
