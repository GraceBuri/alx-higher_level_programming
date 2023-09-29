#!/bin/bash
#make a request to port 5000 and gets its message
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
