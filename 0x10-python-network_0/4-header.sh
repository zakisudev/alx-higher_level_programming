#!/bin/bash
# send a GET request with an id attribute

if [ $# -eq 0]; then
	echo "Usage: $0 <URL>"
	exit 1
fi
URL="$1"
curl -H "X-School-User-Id: 90" -s "$URL"
