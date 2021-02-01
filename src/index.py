import sys
import os
from definition import main

source_directory, target_directory = sys.argv[1:3]
source_files = os.listdir(source_directory)

stats = { "words": 0, "defined": 0 }
for i, file_name in enumerate(source_files):
    word, _ = file_name.split(".")
    source = os.path.join(source_directory, file_name)
    target = os.path.join(target_directory, file_name)
    result = main(word, source, target)

    for res in result:
        stats["words"] += 1
        if (len(res["definitions"]) > 0):
            stats["defined"] += 1

print("{} words/parts of speech".format(stats["words"]))
print("{} defined".format(stats["defined"]))
print("{} %".format(stats["defined"] / stats["words"] * 100))
