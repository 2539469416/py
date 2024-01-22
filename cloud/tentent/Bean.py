import json
import ast


class Bean:
    def __init__(self):
        pass

    def get_region(self):
        with open('tmp', 'r', encoding='utf-8') as f:
            return list(ast.literal_eval(f.read()))
