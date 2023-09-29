#!/bin/bash
# send a POST request with a JSON data

curl -X POST -d "@$2" -H "Content-Type: application/json" "$1"
