#!/bin/bash
# displaye the request status
curl -o /dev/null -sIw "%{http_code}" "$1"
