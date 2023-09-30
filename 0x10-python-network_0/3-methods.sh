#!/bin/bash
# Identify the HTTP requests a url is accepting
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
