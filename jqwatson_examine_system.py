import os
from re import S
import readline
import sys

owd = os.getcwd()

# Load data into a list
def LoadList (filename):
    os.chdir("/proc")
    with open (filename, 'r') as fin:
        input_raw = fin.readlines()

    os.chdir("../")    
    return input_raw

def Search (search_term, input_list):
    for i in range (0, len(input_list)):
        if search_term in input_list[i]:
            return input_list[i]
        else:
            return False


# Get Cpu information
cpu_info = LoadList("cpuinfo")

# Get Kernel Information
temp_list = LoadList("version")
kernel_version = temp_list[0]

# Get Uptime Information
temp_list = LoadList("uptime")
uptime = temp_list[0]

# Number 4 proc 1 sched 
os.chdir("/proc/1")
with open ("sched", 'r') as fin:
    input_list= fin.readlines()


time_last_boot = input_list[2]


# Get Disk Information
disk_info = LoadList("diskstats")

reads_completed = 0
reads_merged = 0
writes_completed = 0
writes_merged = 0

for i in range (0, len(disk_info)):
    disk_info_columns = disk_info[i].split(" ")
    #print(disk_info_columns[12])
    # print(disk_info_columns[13])
    #print(disk_info_columns[16])
    # print(disk_info_columns[17])
    reads_completed += int(disk_info_columns[12], 10)
    reads_merged += int(disk_info_columns[13],10)
    writes_completed += int(disk_info_columns[16],10)
    writes_completed += int(disk_info_columns[17],10)


        
total_disk_requests = reads_completed + reads_merged + writes_completed + writes_merged



# Get Num of Proccesses 
temp_list = LoadList("stat")
processes = temp_list[8]

os.chdir(owd)


file1 = open("jqwatson_systemDetails.txt","w")

# Print All varibles to Text File
file1.write("CPU Info: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
for i in range (0, 8):
    file1.write(cpu_info[i])
file1.write("\n")
file1.write("Kernel Version: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
file1.write(kernel_version)
file1.write("\n")
file1.write("Uptime: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
file1.write(uptime)
file1.write("\n")
file1.write("Time Since Last Boot: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
file1.write(time_last_boot)
file1.write("\n")
file1.write("Num of Disk Requests: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
string_disk = str(total_disk_requests)
file1.write(string_disk)
file1.write("\n")

# for i in range (0, len(disk_info)):
#     file1.write(disk_info[i])
file1.write("\n")
file1.write("Number of Processes: ")
file1.write("\n")
file1.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
file1.write("\n")
file1.write(processes)

file1.close()