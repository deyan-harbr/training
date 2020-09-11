from functools import wraps
import json


def persist(func):
    @wraps
    def wrapper(*args, **kwargs):
        with open(kwargs["file"], "w") as outfile:
            json.dump(func(*args, **kwargs), outfile, cls=kwargs["encoder"])
    return wrapper
