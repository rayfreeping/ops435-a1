#!/usr/bin/env/python3
'''Python script for OPS435 assignment 1'''

#Author: Raymond Chan
#Author ID: rchan
#Date: 2020-01-26

import sys
first_number = int(sys.argv[1].replace('-',''))
second_number = int(sys.argv[2])
result = str(first_number + second_number)
print(result[0:4]+'-'+result[4:6]+'-'+result[6:])
