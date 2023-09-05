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

    
    
""" eventarr = []
xarr = []
firewallarr = []
vpnfirewallarr = []
flowsarr = []
ipflowarr = []
urlarr = []
otherarr = [] """
#fieldNames = ("type", 'radio', 'vap')
counter = 0
headers = ["uuid", "date", "time", "IP", "6", "7", "8", "location", "log_class", "type", "radio", "vap", "client_mac", "client_ip", "client_ip6", "identity", "aid"]
idarr = []
xsucarr = []
xautharr = []
xdeautharr = []
xclientdeautharr = []
folder_path = "C:/Users/arotter/Documents/winsyslog"

xsucarr.append(headers)
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

def read_log(_logs):
    with open(_logs) as f:
        data = f.read().splitlines()
        txt_parse(data)
        

def val_add(cat):
    return headers.index(cat)




def field_seperator(temp_arr, _data):
    
    temp_arr[0:9] = _data[0:9]
    for i in _data[9:]:
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



def location_short(loc_long):
    if(loc_long.find('BAS') != -1):
        return 'Basalt'
    if(loc_long.find('BLD') != -1):
        return 'Boulder'
    else:
        return 'Other'

def event_sorter( event_data):
    each_log = [""]*20
    
    if(event_data[9] == "type=8021x_eap_success"):
        each_log = field_seperator(each_log, event_data)
        if(each_log == []):
            return
        else:
            each_log[7] = location_short(each_log[7])
            #del each_log[0:1]
            xsucarr.append(each_log)
    elif(event_data[10] == "type=8021x_auth"):
        xautharr.append(event_data)
    elif(event_data[10] == "type=8021x_client_deauth"):
        xclientdeautharr.append(event_data)
    elif(event_data[10] == "type=8021x_deauth"):
        xdeautharr.append(event_data)
    #else:
        #eventarr.append(event_data)


def txt_parse(_data):

    for i in _data:
        temp = []
        parts = i.split(',')
        temp.append(str(uuid.uuid4()))
        for k in parts[2:7]:
            temp.append(k)
        
        parts[7] = parts[7].split(' ')
        for k in parts[7]:
            temp.append(k)
        if(temp[8] == "events"):
            event_sorter(temp)
    


get_dir()
#print(xsucarr)

pd.DataFrame(xsucarr).to_csv('xsuccess_all_test.csv')

#event_sorter(data)


""" for i in data:
    temp = []
    parts = i.split(',')
    if(parts[10] == "urls"):
        urlarr.append(parts)

    elif(parts[10] == "firewall"):
        firewallarr.append(parts)
    elif(parts[10] == "flows"):
        flowsarr.append(parts)

    elif(parts[10] == "vpn_firewall"):
        vpnfirewallarr.append(parts)
    elif(parts[10] == "events"):
        eventarr.append(parts)
    elif(parts[10] == "ip_flow_start"):
        ipflowarr.append(parts)
    elif(parts[10] == "ip_flow_end"):
        ipflowarr.append(parts)
    else:
        otherarr.append(parts)
     """















    
