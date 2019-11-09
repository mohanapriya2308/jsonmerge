# JSON Merge Task

This Python Module allows you to merge a series of files containing JSON array of Objects into a single file containing one JSON object.

N-Number of files
M-Number of root keys
K-Number of entires in array of a given root key

The time complexity would be O(N.M.K). Under the given test cases N and M are negligible O(K)

Consider a the following JSON files:

Data1.json contains -
 {"strikers": [ { "name": "Alexis Sanchez", "club": "Manchester United" }, { "name": "Robin van Persie", "club": "Feyenoord" }  ] } 

 data2.json contains - 
 {"strikers": [ { "name": "Nicolas Pepe", "club": "Arsenal" } ] } 

 data3.json contains - 
 {"strikers": [ { "name": "Gonzalo Higuain", "club": "Napoli" }, { "name": "Sunil Chettri", "club": "Bengaluru FC" } ] } 

*We call merge from jsonmerge.py to merge the objects -*

`def merge(directory,input_base,output_base,max_size):
    ...
    for file_name in glob.glob(pattern):
    ...`  

**glob**-glob is a general term used to define techniques to match specified pattern according to rules related Unix shell. Linux and Unix systems and shells also supports glob and also provide function glob() in system libraries. In this tutorial we will look glob() function usage in Python programming language.



1.glob.glob is used to find the extension patterns and read all files into a single file.
2.After reading all files, the objects are merged together.




*After merging, the output file looks like*

{"strikers": [ { "name": "Alexis Sanchez", "club": "Manchester United" }, { "name": "Robin van Persie", "club": "Feyenoord" }, { "name": "Nicolas Pepe", "club": "Arsenal" }, { "name": "Gonzalo Higuain", "club": "Napoli" }, { "name": "Sunil Chettri", "club": "Bengaluru FC" } ] } 
 
---

**Testcases**

*In testjsonmerge.py, the following are each case description*

1.In class TestJSONMerge, function def test_base(self) tests the base case.

2.In class TestJSONMerge, function def different_name(self) tests the files by changing the keyname(eg:from Strikers to employees)

3.In class TestJSONMerge, function def test_maxsize(self) tests the case where Maximum size is less than the file size.

4.In class TestJSONMerge, function def test_different_files(self) tests the files with different objects having different keys which merges to a single file.

---
