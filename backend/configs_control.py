import json


def get_configs() -> dict:
    with open('configs.txt', 'r') as file:
        configs = json.load(file)
    return configs