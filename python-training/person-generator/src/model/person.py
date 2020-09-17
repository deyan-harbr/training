import json
import csv
from random import randint
from src.base import Base
from sqlalchemy import Column, String, Integer


class Person(Base):
    __tablename__ = 'person'

    _id = Column(Integer, primary_key=True)
    _name = Column(String)
    _gender = Column(String)
    _age = Column(Integer)

    def __init__(self, name: str, gender: str, age: int) -> None:
        self._name = name
        self._gender = gender
        self._age = age

    def __repr__(self) -> json:
        return f"{{{self.name()}, {self.gender()}, {self.age()}}}"

    def __eq__(self, other) -> bool:
        return self.name() == other.name() and self.age() == other.age()

    def __hash__(self) -> int:
        return id(self.name())*self.age()*id(self.gender())

    def name(self):
        return self._name

    def age(self):
        return self._age

    def gender(self):
        return self._gender

    @staticmethod
    def from_json(person_list_dict: list) -> set:
        sequence_person = set()
        for p in person_list_dict:
            sequence_person.add(Person(p["name"],
                                       p["age"]))
        return sequence_person

    @staticmethod
    def from_csv(person_file: 'str') -> list:
        persons = []
        #TODO handle exception
        with open(person_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                persons.append(Person(row['name'], row['gender'], randint(1, 99)))
        return persons


class PersonEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, Person):
            return o.__dict__
        return json.JSONEncoder.default(self, o)
