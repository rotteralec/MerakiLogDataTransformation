import pandas as pd
import os
import multiprocessing as mp

#This is for the occupancy data set retroactively

#init objects
counter = 0
pool = mp.Pool(2)
jobs = []



def create_jobs():
    
    return
""" def get_chunks():
    # If you have N processors,
    # then we need memory to hold 2 * (N - 1) chunks (one processor
    # is reserved for the main process).
    # The size of a chunk is CHUNK_SIZE * average-line-length.
    # If the average line length were 100, then a chunk would require
    # approximately 1_000_000 bytes of memory.
    # So if you had, for example, a 16MB machine with 8 processors,
    # you would have more
    # than enough memory for this CHUNK_SIZE.
    CHUNK_SIZE = 1_000

    return """
occ_dic = {
    "BLD": 145,
    "BAS": 50,
    "NY": 35,
    "DC": 39,
    "OAK": 38
}


acc_occ_dic = {
    "BLD": 0,
    "BAS": 0,
    "NY": 0,
    "DC": 0,
    "OAK": 0
}

folder_path = "K:/raw_meraki_logs/"
folder_path_2 = "K/raw_meraki_logs/WinSyslog-2023-10-13.log"
def get_dir():
    print("os.chdir start")
    os.chdir(folder_path)
    with open(folder_path_2) as f:
        for line in f:
            jobs.append(pool.apply_async(process, (line)))
    """ for file in os.listdir():
        print("in file for loop")
        if file.endswith("10-14.log"):
            print(file)
            file_path = f"{folder_path}/{file}"
            read_log(file_path)
        else:
            continue
 """

def read_log(_path):
    print("open path before")
    with open(_path) as f:
        print("openpath")
        for i in f:
            print(i)
        f.close()

    

def txt_parse(_data):
    print("txtparse start")
    for i in _data:
        line = i.split(',')
        
        for k in line:
            print(k)
get_dir()