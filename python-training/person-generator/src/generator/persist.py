import json
from src.model.person import Person, PersonEncoder
from functools import wraps
from src.base import session_scope


def mapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in args:
            func(*args, **kwargs)
    return wrapper


def persist(sink, sink_config: str = "out.json"):
    def decorator_persist(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if sink == "json":
                with open(sink_config, "w") as outfile:
                    json.dump(func(*args, **kwargs), outfile, cls=PersonEncoder)
            elif sink == "sql":
                print("sql")
                with session_scope() as session:
                    session.add_all(func(*args, **kwargs))
            else:
                raise Exception("Invalid argument")
        return wrapper
    return decorator_persist


def persist_json(file):
    def decorator_persist(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file, "w") as outfile:
                json.dump(func(*args, **kwargs), outfile, cls=PersonEncoder)
        return wrapper
    return decorator_persist


def persist_sql(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with session_scope() as session:
            session.add_all(func(*args, **kwargs))
    return wrapper


@mapper
def persist_person_decorated(person: "Person", sink: str) -> None:
    with open(sink, 'a') as outfile:
        outfile.write(json.dumps(person, cls=PersonEncoder))


def persist_person(person: "Person", sink: str) -> None:
    with open(sink, 'a') as outfile:
        json.dump(person, outfile, cls=PersonEncoder)


