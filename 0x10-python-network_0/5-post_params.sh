#!/bin/bash
# sends a POST request with some data
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
