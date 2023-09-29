#!/bin/bash
#script that takes url and display methods accepting it
curl -s -I "$1" | grep "^Allow: .*" | cut -d " " -f 2-
