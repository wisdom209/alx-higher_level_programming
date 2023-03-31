#!/bin/bash
# Send a header variable while curling
curl -X GET -H "X-School-User-Id: 98" -s "$1"
