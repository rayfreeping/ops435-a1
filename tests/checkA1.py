#! /usr/bin/env python3
'''
This check script will run the sample tests on assignment 1 script 
before submitting to blackboard by the students.
Please note that this script does not check the docstring of the script 
or its functions.
This check scripts will only account for 30% of assignment 1.

Released by Raymond Chan on Oct 30, 2018
Updated for the 2021 Winter Semester version on Feb 3, 2021
'''

import types 
import sys
import os
import subprocess


def preliminary_grading(stud_name):
    message = '\n== Preliminary A1 Test Run Report for '+stud_name+'==\nThe following is your preliminary test run report for assignment 1. Please review the report and fix all the errors identified before submitting your algorithm, python script, and test report to blackboard using the assignment 1 submission link which will be available on Monday, October 16 2020.\n'
    return message


if __name__ == '__main__':
   if len(sys.argv) != 2:
        student = input('Please enter your email user id:')
   else:
        student = sys.argv[1]
   
   a1_script = 'a1_'+student+'.py'
   if not os.path.isfile(a1_script):
        print('=' * 70)
        print('Your A1 script file',a1_script,'is not in the current direcoty')
        print('Please copy this script to the directory that contains your')
        print('A1 script file and run this test script again.')
        print('=' * 70)
        sys.exit()
   
   print(preliminary_grading(student))
   print('=' * 40)
   doc_marks = {} # data dictionary for documentation mark
   total_doc_marks = 0
   # test running student's script
   tests = { 1:['2020-10-10','Oct 10, 2020\n'],
             2:['2020-10-09','Oct 9, 2020\n'],
             3:['2020-06-30','Jun 30, 2020\n'],
             4:['20201010','Oct 10, 2020\n'],
             5:['2020/10/10','Oct 10, 2020\n'],
             6:['2020.02.29','Feb 29, 2020\n'],
             7:['2019.02.29','Error 03: wrong day entered\n'],
             8:['2019.13.12','Error 02: wrong month entered\n'],
             9:['2019.06.31','Error 03: wrong day entered\n'],
            10:['201802','Error 09: wrong date entered\n'],
            11:['18981225','Error 10: year out of range, must be 1900 or later\n'],
            12:['19981299','Error 03: wrong day entered\n'],
            13:['189802','Error 09: wrong date entered\n'],
            14:['20201010 2020/10/10','Usage: '+a1_script+' YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD\n'],
            15:['','Usage: '+a1_script+' YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD\n']
            }
   test_marks = {}
   for test_no in range(1,len(tests)+1):
       cmd = 'python3 a1_'+student+'.py '+tests[test_no][0]
       print('Test run command',test_no,':',cmd)
       p1 = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
       result = p1.communicate()[0].decode('utf-8').strip('\n')
       expected = tests[test_no][1].strip('\n')
       if result == expected:
          print('--test passed--')
          test_marks[test_no] = 1
       else:
          print('--test failed--')
          print('---- expect:',expected)
          print('----  given:',result)
          test_marks[test_no] = 0
   print('Test Results:',test_marks)
   total_test_marks = 0
   for item in test_marks:
       total_test_marks += test_marks[item] 
   total_test_marks = total_test_marks / len(tests) * 30
   print('Total test run marks: ',total_test_marks)
   grand_total = total_test_marks + total_doc_marks
   print('Total marks for script (max. 30):',grand_total)
