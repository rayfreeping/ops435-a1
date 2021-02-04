#! /usr/bin/env python3
'''1st attempt for 2021 Winter Semester Assignment 1'''
# Author: Raymond Chan
# Date: 2021-02-03
import sys
dob = sys.argv[1].replace('/','')
month_name = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
year = dob[0:4]
month = int(dob[4:6])
day = dob[6:]
new_dob = month_name[month - 1] + ' ' + day + ', ' + year
print("Your date of birth is:", new_dob)
