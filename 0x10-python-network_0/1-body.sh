#!/bin/bash
# print body of response if status is 200
if curl -sI "$1" | grep -q 200; then curl -s "$1" | head -c -1; fi
