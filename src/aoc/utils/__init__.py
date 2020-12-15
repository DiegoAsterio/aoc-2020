from pathlib import Path

def local_path(basename, relativeroute):
    return Path(basename).resolve().parent.joinpath(relativeroute)

def get_lines(path):
    with open(path) as f:
        return f.read().split('\n')

def find(lst, elem):
    return [i for i, x in enumerate(lst) if x == elem]
