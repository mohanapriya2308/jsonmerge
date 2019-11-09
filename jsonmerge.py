import json
import os
import glob

def merge(directory,input_base,output_base,max_size):
    pattern=os.path.join(directory,input_base+"*.json")
    data = []
    seq=0
    for file_name in glob.glob(pattern):                                    #to read the input files with .json Extension
        with open(file_name) as f:
            data.append(json.load(f))
    newdict1={}
    i=0
    for i in data: 
        for key in i.keys():
            if key in newdict1:
                newdict1[key]+=i[key]                                       #to merge objects with same key
            else:
                newdict1[key]=i[key]
    if (len(json.dumps(newdict1))>max_size):
        raise Exception("Merged file size is greater")
    else:
        pattern = os.path.join(directory,output_base+str(seq)+".json")      
        new_file=open(pattern,"w")
        json.dump(newdict1,new_file)                                        #to write the merged output to the json file
        new_file.close()    

def main():
    dir='C:/Users/Sneha/Desktop/freshworks/test/input'
    merge(dir,"data","output",1000)
    
       