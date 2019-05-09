#!/bin/bash

result=`python hello.py`

if [ $result == "hello" ]; then 
  exit 0
else
  exit 1
fi
