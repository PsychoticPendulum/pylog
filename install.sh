#! /usr/bin/bash

DIR=$(ls /usr/lib/ | grep "python" | tail -n 1)
cp src/* /usr/lib/$DIR
