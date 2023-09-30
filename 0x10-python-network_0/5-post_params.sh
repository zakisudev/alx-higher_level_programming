#!/bin/bash
# send a POST request with email and subject attributes
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
