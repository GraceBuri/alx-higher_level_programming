#!/bin/bash
#send json post request to a given json file
curl -s "$1" -d "@$2" POST -H"Content-Type: application/json"
