#!/bin/bash
# Get the number of bytes from server response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
