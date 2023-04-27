#!/bin/bash
# send JSON post
curl -sd 'user_id=98' -X PUT -H 'Origin: HolbertonSchool' -L 0.0.0.0:5000/catch_me
