#!/bin/bash
# displays the request status from the server
curl -s -o /dev/null -w "%{http_code}" "$1"
