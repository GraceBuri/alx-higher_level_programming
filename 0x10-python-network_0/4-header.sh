#!/bin/bash
#writea script that sends a request and  returns body of resposnse
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
