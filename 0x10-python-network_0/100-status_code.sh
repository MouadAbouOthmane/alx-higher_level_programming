#!/bin/bash
# Displays only the status code of the response.
curl -so nul  -w %{http_code} $1
