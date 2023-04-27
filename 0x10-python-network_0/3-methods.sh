#!/bin/bash
# Send a delete request with curl
curl -sI "$1" | grep 'Allow:' | sed 's/^Allow: //'
