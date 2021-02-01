"""
iterate through parts for each word
if part is in PARTS_OF_SPEECH, try to obtain definition:
    iterate tokens
    find things that are [[ ]] (but exclude the Category tag)
    add entry with { word, part_of_speech, definitions }
"""
import sys
import json

from definition.constants import PARTS_OF_SPEECH
from definition.get_definitions_from_part import main as get_definitions_from_part


def _run(word, source_file_path):
    with open(source_file_path, 'r') as f:
        parts = json.loads(f.read())

    part_of_speech_sections = [
        part for part in parts if part["name"] in PARTS_OF_SPEECH
    ]

    if len(part_of_speech_sections) == 0:
        raise RuntimeError(
            "No parts of speech found for {w}".format(w=word))

    return [
        {
            "part_of_speech": pos["name"],
            "definitions": get_definitions_from_part(pos),
        }
        for pos in part_of_speech_sections
    ]


def main(word, source_file_path, target_file_path):
    res = _run(word, source_file_path)
    with open(target_file_path, 'w+') as f:
        f.write(json.dumps(res))

    return res


if __name__ == "__main__":
    file_path = sys.argv[1]
    result = _run(file_path)
    print(result[0])
