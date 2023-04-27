#!/bin/bash
# send JSON post
curl -sd "${cat "$2"}" -H "content-type:application/json" "$1"
