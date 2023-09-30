#!/bin/bash
# request and display the size of the body of the response
curl -so /dev/null -w "%{size_download}\n" $1
