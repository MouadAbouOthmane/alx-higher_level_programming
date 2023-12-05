#!/bin/bash
# Sends a JSON POST request to a URL passed 
curl -s -H "Content-type: application/json" --data "@$2" $1
