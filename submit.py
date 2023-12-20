import os

SAMPLE_DIRECTORY = "/home/jk/Desktop/scires/experiment1-1000/samples"

samples = os.listdir(SAMPLE_DIRECTORY)

start = 250
end = 1000

for i in range(start, end):
    os.system(f"cuckoo submit {SAMPLE_DIRECTORY}/{samples[i]}")
