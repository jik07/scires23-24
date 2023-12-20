import os
import shutil
import json
from time import sleep

ANALYSIS_DIR = "/home/jk/.cuckoocwd/storage/analyses"
RESULT_DIR = "/home/jk/Desktop/scires/experiment1-1000/reports"

while True:
    for day in os.listdir(ANALYSIS_DIR):
        for analysis in os.listdir(f"{ANALYSIS_DIR}/{day}"):
            dir = f"{ANALYSIS_DIR}/{day}/{analysis}"

            if not os.path.isfile(f"{dir}/task_1/task.log") or not os.path.isfile(f"{dir}/task_1/report.json"):
                continue
            with open(f"{dir}/task_1/task.log") as f:
                if not "Setting task to reported." in f.read():
                    continue

            with open(f"{dir}/identification.json") as f:
                id = json.load(f)
            sha1 = id['target']['sha1']

            shutil.copyfile(f"{dir}/task_1/report.json", f"{RESULT_DIR}/{sha1}.json")
            shutil.rmtree(dir)
    sleep(1000)
