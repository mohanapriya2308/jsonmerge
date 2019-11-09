import unittest
import json 
from jsonmerge import merge

# custom compare function that compares one level deep
def compareJSON(a,b):
    for key in a.keys():
        if key in b:
            for i in a[key]:
                if i in b[key]:
                     continue
                else:
                     return False
        else:
            return False
    return True

class TestJSONMerge(unittest.TestCase):
    # to test the given base case 
    def test_base(self):                                                                                       
        dir='./test/input'
        merge(dir,"data","output",2000)
        output=open("./test/input/output0.json","r")
        expected_output=open("./test/input/expected_output.json","r")
        self.assertTrue(compareJSON(json.load(output), json.load(expected_output)))
        output.close()
        expected_output.close()
    
    # to change the key of the given case and check the output
    def test_different_name(self):                                                                              
        dir='./test/input2'
        merge(dir,"data","output2",2000)
        output2=open("./test/input2/output20.json","r")
        expected_output2=open("./test/input2/expected_output2.json","r")
        self.assertTrue(compareJSON(json.load(output2), json.load(expected_output2)))
        output2.close()
        expected_output2.close()

    # to check maximum size of the file smaller than the given json files                                    
    def test_maxsize(self):                                                                                      
        dir='./test/input2'
        with self.assertRaises(Exception):
            merge(dir,"data","output2",1)
            print("File Size Exceeding than the maximum size")
            
    # to check with more than 1 key in the file
    def test_different_files(self):                                                                              

        dir='./test/input3'
        merge(dir,"data","output3",2000)
        output3=open("./test/input3/output30.json","r")
        expected_output3=open("./test/input3/expected_output3.json","r")
        self.assertTrue(compareJSON(json.load(output3), json.load(expected_output3)))
        output3.close()
        expected_output3.close()

unittest.main()
