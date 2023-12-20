import pickle
import os
import shutil

RESULT_DIR = "/media/jik/samples/experiment1-1000"
SOURCE_DIR = "/media/jik/Crucial X8/scires 23-24/packware/files/datasets/wild-ember/samples"
SAMPLE_DIRS = [
        "/media/jik/Crucial X8/scires 23-24/experiment1-1000/bp.pickle",
        "/media/jik/Crucial X8/scires 23-24/experiment1-1000/bu.pickle",
        "/media/jik/Crucial X8/scires 23-24/experiment1-1000/mp.pickle"
]

for sample_dir in SAMPLE_DIRS:
    with open(sample_dir, 'rb')  as f:
        df = pickle.load(f)

    for sha1 in df['sample_sha1']:
        dir = f"{SOURCE_DIR}/{sha1[0]}/{sha1[1]}/{sha1[2]}/{sha1}.bin"
        if not os.path.isfile(dir):
            continue

        shutil.copy(dir, RESULT_DIR)
