#!/bin/bash
# send JSON post
curl -sd "${cat "$2"}" -H 'Content-Type: application/json' "$1"
