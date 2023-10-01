#!/bin/bash
# displays the request status from the server
curl -so /dev/null -w "%{http_code}" "$1"
