#!/bin/bash
# Gets the size of the body of the response
curl -s --head "$1" | grep -i content-length
