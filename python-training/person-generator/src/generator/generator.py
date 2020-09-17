import random
from src.generator.persist import persist


@persist("sql")
def generate_person_sequence(item_list: list, sequence_size: int = 10,) -> list:
    person_sequence = set()
    for _ in range(sequence_size):
        person_sequence.add(random.choice(item_list))
    return list(person_sequence)

