#!/bin/bash
# send a request to a url and display custome text
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
