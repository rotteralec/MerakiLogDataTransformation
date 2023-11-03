##This script is for moving previous day's log to long term blob storage in azure
import shutil
source_path = "C:/MerakiLogs"
dest_path = "Q:/"
file_name = "test_log.txt"

f = open("C:/Users/arotter/Documents/MerakiLogDataTransformation/test_log.txt", 'r+')
print("before")
print(f.readlines())
print("after")
##os.system(r"NET USE P: \\ComputerName\ShareName %s /USER:%s\%s" % (password, domain_name, user_name))
shutil.copyfile(source_path + file_name, dest_path + file_name)
