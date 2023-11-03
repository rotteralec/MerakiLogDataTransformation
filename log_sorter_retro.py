# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 10:10:57 2023

@author: arotter
"""


##To do now:
###*Fix formatting
##Run on all files in folder
## 

##To do long:
##*Add to headers from parsing
#add unit tests
##*user based****
##Optimize script performance
#
#

import pandas as pd
##Use uuid.uuid4() for random
##in future use uuid5 with sha-1 hash of uuid and name/data/time??
import uuid
import os

import time
st = time.time()
print("Current Time: ", st)

    
    
counter = 0
headers = ["uuid", "date", "time", "IP", "6", "7", "8", "location", "log_class", "type", "radio", "vap", "client_mac", "client_ip", "client_ip6", "identity", "aid"]
idarr = []
xsucarr = []
xautharr = []
xdeautharr = []
xclientdeautharr = []

##Set this to the location of all WinSyslog.log files
folder_path = "K:/raw_meraki_logs/"


## adds self made header row to top of array
#xsucarr.append(headers)


"""
get_dir
use: sets OS directory to folder_path ^^
     searches through all files in directory to access each .log file
     calls read_log on each .log file path to read the contents
"""
def get_dir():
    global idarr
    os.chdir(folder_path)
    for file in os.listdir():
        if file.endswith(".log"):
            print(idarr)
            idarr = []
            file_path = f"{folder_path}/{file}"
            print(file_path)
            read_log(file_path)

"""
read_log
_logs: .log file path to be read
use: read log file and call txt_parse on the data split by newline 
"""
def read_log(_logs):
    with open(_logs) as f:
        for line in f:
        #data = f.read().splitlines()
            txt_parse(line)
        
"""
val_add
cat: string category to find in header row
use: given the category name, find index of that category in header row
return: int index of 
"""
def val_add(cat):
    return headers.index(cat)



"""
field_seperator
temp_arr: array to be appended with proper categories
_data: array with data to be appended is in
use: Check for type=val values and seperates them into proper indexes
     also checks if type is identity to seperate @rmi.org or RMI/ from username (probably move to other function)
"""
def field_seperator(temp_arr, _data):
    
    temp_arr[0:9] = _data[0:9]
    #print(_data[8:])
    for i in _data[8:]:
        temp_cat = ""
        temp_val = ""
        equal_ind = -1
        equal_ind = i.find('=')
        if(equal_ind != -1):
            temp_cat = str(i[0:equal_ind]).lower()
            temp_val = str(i[equal_ind+1:]).lower()
            if(temp_cat == "identity"):
                ind_dom = (temp_val.lower().find("rmi"))
                ind_at = (temp_val.find("@"))
                if(ind_dom in [0, 1, 2]):
                    if(temp_val[ind_dom+3] == "\\" ):
                        temp_val = temp_val[ind_dom+4:]
                        temp_val = temp_val.strip("'")
                elif(temp_val.find("@") != -1):
                    temp_val = temp_val[1:temp_val.find("@")]
                    temp_val = temp_val.strip("'")
                else:
                    temp_val = temp_val.strip("'")
                if(temp_val not in idarr):
                    idarr.append(temp_val)
                    temp_arr[val_add(temp_cat)] = temp_val
                elif(temp_val in idarr):
                    temp_arr = []
                    return temp_arr
            else:
                temp_arr[val_add(temp_cat)] = temp_val
    if(temp_arr == []):
        return []
    elif(temp_arr != []):
        return temp_arr


"""
location_short
loc_long: string
use: simple function to shorten location to 3 letter abreviation
(need to add other office locations)
"""
def location_short(loc_long):
    if(loc_long.find('BAS') != -1):
        return 'Basalt'
    if(loc_long.find('BLD') != -1):
        return 'Boulder'
    if(loc_long.find('NY') != -1):
        return 'New York City'
    if(loc_long.find('DC') != -1):
        return 'Washington D.C.'
    if(loc_long.find('OAK') != -1):
        return 'Oakland'
    else:
        return 'Other'
"""
event_sorter
event_data: array of event data to be sorted
use: sorts given event data into each event type in the 9th index
(need to add non 8021x events)
"""
def event_sorter(event_data):
    each_log = [""]*20
    if(event_data[9] == "type=8021x_eap_success"): 
        #print(event_data)
        each_log = field_seperator(each_log, event_data)
        if(each_log == []):
            return
        else:
            each_log[7] = location_short(each_log[7])
            #del each_log[0:1]
            #print(each_log)
            xsucarr.append(each_log) 
            """
    elif(event_data[10] == "type=8021x_auth"):
        xautharr.append(event_data)
    elif(event_data[10] == "type=8021x_client_deauth"):
        xclientdeautharr.append(event_data)
    elif(event_data[10] == "type=8021x_deauth"):
        xdeautharr.append(event_data)
    #else:
        #eventarr.append(event_data) """



"""
txt_parse
_data: array of unchanged Meraki Log data
use: loop through each log line
     add Universally Unique ID (UUID) to each record
"""
def txt_parse(_data):
    temp = []
    parts = _data.split(',')
    
    #print(parts[7]=="")
    if (len(parts)>7):
        parts[7] = parts[7].split(' ')
        #print(parts)
        if(parts[7][2]=="events"):
            for i in parts[7]:
                parts.append(i)
   
            del parts[7]
        #print(parts)
            del parts[0:2]
    
            parts.insert(0,str(uuid.uuid4()))
            event_sorter(parts)
    else:
        print(len(parts))
    #print (parts)
  ## """  for i in _data:
      #3  temp = []
      #  parts = i.split(',')
     #   temp.append(str(uuid.uuid4()))
      #  print(i) """
        
        #
        #for k in parts[7]:
        #if(temp[8] == "events"):
            #event_sorter(temp)
    
get_dir()
#print(xsucarr[0:20])
et = time.time()
elapsed_time = et - st
print('Execution Time: ', elapsed_time, 'seconds')
os.chdir('C:/Users/arotter/Documents/MerakiLogDataTransformation/')
et = time.time()
elapsed_time = et - st
print('Execution Time: ', elapsed_time, 'seconds')
pd.DataFrame(xsucarr).to_csv('xsuccess_all_test.csv', mode='a+', index=False, header=False)

et = time.time()
elapsed_time = et - st
print('Execution Time: ', elapsed_time, 'seconds')
#event_sorter(data)











