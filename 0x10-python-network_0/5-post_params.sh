#!/bin/bash
# send Post HTTP request with curl
curl -sd 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
