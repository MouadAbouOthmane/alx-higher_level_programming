#!/bin/bash
# Displays the size of the body of the response

curl $1 --silent -w '%{stderr}%{size_download}\n' 1> /dev/null
