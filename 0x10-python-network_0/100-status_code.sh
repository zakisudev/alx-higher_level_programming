#!/bin/bash
# displaye the request status
curl -so /dev/null -w "%{http_code}" $1
