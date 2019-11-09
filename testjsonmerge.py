import unittest
from jsonmerge import merge
class TestJSONMerge(unittest.TestCase):
    def test_base(self):
        dir='C:/Users/Sneha/Desktop/freshworks/test/input'
        merge(dir,"data","output",2000)
        output=open("C:/Users/Sneha/Desktop/freshworks/test/input/output0.json","r")
        expected_output=open("C:/Users/Sneha/Desktop/freshworks/test/input/expected_output.json","r")
        self.assertEqual(output.read(),expected_output.read())
        output.close()
        expected_output.close()
    
    def test_different_name(self):
        dir='C:/Users/Sneha/Desktop/freshworks/test/input2'
        merge(dir,"data","output2",2000)
        output2=open("C:/Users/Sneha/Desktop/freshworks/test/input2/output20.json","r")
        expected_output2=open("C:/Users/Sneha/Desktop/freshworks/test/input2/expected_output2.json","r")
        self.assertEqual(output2.read(),expected_output2.read())
        output2.close()
        expected_output2.close()
    
    def test_maxsize(self):
        dir='C:/Users/Sneha/Desktop/freshworks/test/input2'
        with self.assertRaises(Exception):
            merge(dir,"data","output2",1)
            print("File Size Exceeding than the maximum size")
            
    def test_different_files(self):
        dir='C:/Users/Sneha/Desktop/freshworks/test/input3'
        merge(dir,"data","output3",2000)
        output3=open("C:/Users/Sneha/Desktop/freshworks/test/input3/output30.json","r")
        expected_output3=open("C:/Users/Sneha/Desktop/freshworks/test/input3/expected_output3.json","r")
        self.assertEqual(output3.read(),expected_output3.read())
        output3.close()
        expected_output3.close()

unittest.main()