#!/bin/bash
# find the allowed methods
curl -sI "$1" | grep Allow | sed 's/Allow: //g'
