#!/bin/bash
#script that sendsurl and displays size of body resposne
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
