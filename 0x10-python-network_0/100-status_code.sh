#!/bin/bash
#script that sends a Get request and display status code
curl -s -o /dev/null -w "%{http_code}" "$1"
