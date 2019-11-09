import json
import os
import glob

def merge(directory,input_base,output_base,max_size):
    pattern=os.path.join(directory,input_base+"*.json")
    print(pattern)
    data = []
    seq=0
    for file_name in glob.glob(pattern):
        print(file_name)
        with open(file_name) as f:
            data.append(json.load(f))
    newdict1={}
    i=0
    for i in data: 
        for key in i.keys():
            if key in newdict1:
                newdict1[key]+=i[key]
            else:
                newdict1[key]=i[key]
   
    if (len(json.dumps(newdict1))>max_size):
        raise Exception("Merged file size is greater")
    else:
        pattern = os.path.join(directory,output_base+str(seq)+".json")      
        new_file=open(pattern,"w")
        json.dump(newdict1,new_file)
        new_file.close()

def main():
    dir='C:/Users/Sneha/Desktop/freshworks/test/input'
    merge(dir,"data","output",1000)
    
       