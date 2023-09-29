#!/bin/bash
# Identify the HTTP requests a url is accepting

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL="$1"
curl -X OPTIONS -I "$URL" | grep "Allow:" | sed 's/Allow: //'
