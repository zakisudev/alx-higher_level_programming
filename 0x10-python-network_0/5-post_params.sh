#!/bin/bash
# send a POST request with email and subject attributes

EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"
curl -sX POST -d "email=$EMAIL&subject=$SUBJECT" "$1"
