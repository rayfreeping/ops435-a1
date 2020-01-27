When you have your python script for assignment 1 ready, name your script as
a1_[seneca_id].py. The following example assume "rchan" is the [seneca_id]. 
Run the test script checkA1.py as show below.

Please note that this test script "checkA1.py" does not perform a full test. 
It will not check the docstring in your script.

Your algorithm file and other files on github.com will be checked manually.

[rchan@centos7 a1]$ python3 checkA1.py rchan

== Preliminary A1 Test Run Report for rchan==
The following is your preliminary test run report for assignment 1. Please review the report and fix all the errors identified before submitting your algorithm, python script, and test report to blackboard using the assignment 1 submission link which will be available on Friday, February 7, 2020.

========================================
Test run command 1 : python3 a1_rchan.py 2018/01/01 1
--test passed--
Test run command 2 : python3 a1_rchan.py 2018/01/01 -1
--test passed--
Test run command 3 : python3 a1_rchan.py 2018/01/01 2
--test passed--
Test run command 4 : python3 a1_rchan.py --step 2018/01/01 3
--test passed--
Test run command 5 : python3 a1_rchan.py 2018/07/01 500
--test passed--
Test run command 6 : python3 a1_rchan.py 2018/99/01 2
--test passed--
Test run command 7 : python3 a1_rchan.py 2018/01/99 2
--test passed--
Test run command 8 : python3 a1_rchan.py 2018 2
--test passed--
Test run command 9 : python3 a1_rchan.py 2020/02/28 1
--test passed--
Test run command 10 : python3 a1_rchan.py 2020/03/01 -1
--test passed--
Test Results: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
Total test run marks:  48.0
Total marks for script (max. 48): 48.0

--------------------------------------------------------------

If you see any test being failed, please debug your script and fix 
the error(s) and re-run the above command to re-test your script.

Once you are satisfied with the result, capture the test run results to a file and name it as "a1_results.txt". Submit the test result and your script, together with the algorithm file to blackboard.

