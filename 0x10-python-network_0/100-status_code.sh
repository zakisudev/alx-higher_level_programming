#!/bin/bash
# displays the request status from the server
curl -sw '%{http_code}' "$1" -o /dev/null
