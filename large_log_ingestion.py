import os


folder_path = "C:/Users/arotter/Documents/MerakiLogDataTransformation"
event_total_arr = {}
detail_total_arr = {}
loc_arr = {'BLD': 0,
           'NY': 0,
           'DC': 0,
           'BAS': 0,
           'OAK': 0,
           "TOTAL": 0}
def get_dir():
    global idarr
    os.chdir(folder_path)
    for file in os.listdir():
        if file.endswith("30.log"):
            file_path = f"{folder_path}/{file}"
            print(file_path)
            read_log(file_path)


def read_log(_logs):
    with open(_logs) as f:
        data = f.read().splitlines()
        txt_parse(data)


##72 = events
##73 = details
def detail_total(_data):
    if _data in detail_total_arr.keys():
        detail_total_arr[_data] = detail_total_arr[_data] + 1
    else:
        detail_total_arr[_data] = 1

def event_totals(_data):
    if _data in event_total_arr.keys():
        event_total_arr[_data] = event_total_arr.get(_data) + 1
    else:
        event_total_arr[_data] = 1

def loc_totals(_data):
    if "BLD" in _data:
        loc_arr["BLD"] = loc_arr["BLD"] + 1
    elif "NY" in _data:
        loc_arr["NY"] = loc_arr["NY"] + 1
    elif "OAK" in _data:
        loc_arr["OAK"] = loc_arr["OAK"] + 1
    elif "BAS" in _data:
        loc_arr["BAS"] = loc_arr["BAS"] + 1
    elif "DC" in _data:
        loc_arr["DC"] = loc_arr["DC"] + 1
    loc_arr["TOTAL"] = loc_arr["TOTAL"] + 1
    
    


def txt_parse (_data):
    for i in _data:
        temp = []
        parts = i.split(',')
        parts[7] = parts[7].split(' ')
        ##print(parts[7])
        event_totals(parts[7][2])
        detail_total(parts[7][3])
        loc_totals(parts[7][1])


print("test print")
get_dir()
{k: v for k, v in sorted(detail_total_arr.items(), key=lambda item: item[1])}
print(event_total_arr)
print(detail_total_arr)
print(loc_arr)