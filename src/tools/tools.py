import re

def get_latests_path(path):
    if "loginpage" in path :
        latest_path = "/loginpage"
    else:
        latest_path = "/threads"
    return latest_path