import re

PATTERN = re.compile("\[\[[\w\s-]+\]\]")


def get_definitions_from_token(token):
    matches = [match.group() for match in re.finditer(PATTERN, token)]
    return [match.replace("[", "").replace("]", "") for match in matches if "category:" not in match.lower()]


def main(part):
    obtained = [get_definitions_from_token(token) for token in part["tokens"]]
    all_definitions = []
    for o in obtained:
        if len(o) > 0:
            all_definitions.extend(o)
    return all_definitions
