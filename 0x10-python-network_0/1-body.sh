#!/bin/bash
# print body of response if status is 200
if curl -sLI "$1" | grep -q 200; then curl -s "$1"; fi
