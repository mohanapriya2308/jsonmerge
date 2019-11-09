import json
import os
import glob

def merge(directory,input_base,output_base,max_size):
    # to read the input files with .json Extension
    pattern=os.path.join(directory,input_base+"*.json")
    data = []
    seq=0

    newdict1={}
    for file_name in glob.glob(pattern):                                   
        with open(file_name) as f:
            i = json.load(f)
            for key in i.keys():
                if key in newdict1:
                    # to merge objects with same key
                    newdict1[key]+=i[key]                                      
                else:
                    newdict1[key]=i[key]

    if (len(json.dumps(newdict1))>max_size):
        raise Exception("Merged file size is greater")
    else:
        pattern = os.path.join(directory,output_base+str(seq)+".json")      
        new_file=open(pattern,"w")

        # to write the merged output to the json file
        json.dump(newdict1,new_file)                                        
        new_file.close()    

def main():
    dir='./test/input'
    merge(dir,"data","output",1000)
    
       
