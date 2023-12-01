#!/bin/bash
# Displays the size of the body of the response
curl $1 -s -w '%{size_download}\n'