# -*- coding: utf-8 -*-
import json
from flatten_json import unflatten 
import ast
dictionary = {}
f_write = open("data.json","w") 
f_read = open("sample_products.txt", "r")
for line in f_read:
    line = line.strip()
    if len(line.split()) == 0:
        continue
    line = line.replace('=',':')
    y = json.dumps(line)
    f_write.write(y + "\n")
    with open('data.json','r') as json_file:
        for value in json_file:
            if(len(value.split(":"))==2):
                key,value = value.split(":")
                if(value ==  '"\n'):
                    dictionary[key] = "Null"
                else:
                    dictionary[key] = value    
           
            elif(len(value.split(":"))==3):
                key,value,value1 = value.split(":")
                dictionary[key] = value + value1
            elif(len(value.split(":"))==4):
                key,value,value1,value2 = value.split(":")
                dictionary[key] = value + value1 + value2
dict_write = open('dictionary.json','w')
dict_write.write(str(unflatten(dictionary)))    
print(unflatten(dictionary))
                

            
dict_write.close()
f_read.close()
f_write.close()