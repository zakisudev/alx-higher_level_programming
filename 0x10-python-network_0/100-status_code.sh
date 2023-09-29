#!/bin/bash

curl -o /dev/null -sIw "%{http_code}" "$1"
