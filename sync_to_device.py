# Just a warning, this script ignores all errors from the device.
# It will wipe the device filesystem, and then sync files back on.
# This means you'll need to make sure boot.py and main.py get
# put back on the system for sure.

import os
import sys
import time
from pprint import pprint

# CONNECTION SETTINGS
COM = "COM8"
BAUD = 115200
DELAY = 0.6

# SPESIFIC FILES TO SYNC
files_to_sync=[
    "./ssd1306.py",
    "./display_pbm.py",
    "./demo.py",
    "./boot.py",
    "./main.py",
]

# DIRECTORIES TO SYNC
directories_to_sync = [
    #"./",
    "./ani",
    "./img",
]


print("\n\n\nWARNING THIS SYNC WILL REMOVE ALL FILES CURRENTLY ON THE DEVICE, USE WITH CARE!")
warning = input("Press ENTER to continue, Q + ENTER to quit.\n\n> ").lower()
if "q" in warning:
    print("Exiting...")
    sys.exit()

ampy_command = f"ampy.exe -p {COM} -b {BAUD} -d {DELAY:0.2F}"

print("Getting files and directories lists.")

files = files_to_sync
directories = directories_to_sync.copy()
def get_dir_contents(directory):
    for name in os.listdir(directory):
        dir_path = f"{directory}/{name}"
        if os.path.isdir(dir_path):
            dir_path = f"{directory}/{name}"
            directories.append(dir_path)
            get_dir_contents(dir_path)
        else:
            files.append(f"{directory}/{name}")

for directory in directories_to_sync:
    get_dir_contents(directory)

pprint(files)
pprint(directories)
print("Done building files and directories lists.")


print("\nRemoving all files and directories on the device!")
os.system(f"{ampy_command} rmdir ./ 2> nul")
    
print("Creating new sync directories on device!")
for directory in directories:
    os.system(f"{ampy_command} mkdir {directory} 2> nul")

print("\nSending new sync files...\nThis may take some time if you have a lot of files\n\n¯\\_(ツ)_/¯\n")
files_to_send = len(files)
files_sent = 0
timing = {
    "average":0,
    "count":0,
    "total":0,
    }
for file in files:
    start_time = time.time()
    os.system(f"{ampy_command} put {file} {file}  2> nul")
    files_sent += 1
    timing["count"] += 1
    end_time = time.time()
    timing["total"] += end_time - start_time
    timing["average"] = timing["total"] / timing["count"]

    print(f'File {files_sent} of {files_to_send} |',
    f'FPS: {1 / timing["average"]:0.2f} | EST Time Remaining: {(files_to_send - files_sent) * timing["average"]:0.2f}s',
    f'({(files_to_send - files_sent) * timing["average"] / 60:0.1f}m)')