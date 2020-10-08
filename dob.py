#! /usr/bin/env python3
import sys
dob = sys.argv[1].replace('/','')
month_name = ['Jan','Feb','Mar','Apr','May','Jun',
              'Jul','Aug','Sep','Oct','Nov','Dec']
year = dob[0:4]
month = int(dob[4:6])
day = dob[6:]
new_dob = month_name[month - 1] + ' ' + day + ', ' + year
print("Your date of birth is:", new_dob)
