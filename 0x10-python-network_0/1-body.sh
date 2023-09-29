#!/bin/bash
# send a GET request to a url and display the body of the response

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL="$1"
res=$(mktemp)
curl -s -o "$res" "$URL"

http=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
if [ "$http" -eq 200 ]; then
	cat "$res"
fi
rm "$res"
