#!/bin/bash
# send a POST request with email and subject attributes

if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit
fi
URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"
curl -X POST -d "email=$EMAIL&subject=$SUBJECT" -s "$URL"
