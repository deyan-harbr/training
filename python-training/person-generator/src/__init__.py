from src.model.person import Person
from src.generator.generator import generate_person_sequence
from src.generator.persist import persist_person, persist_person_decorated
from src.base import session_scope, Base, engine


def main():
    """Entry point for the application"""
    Base.metadata.create_all(engine)

    person_list = Person.from_csv("..\data\person.csv")

    generate_person_sequence(person_list)

    with session_scope() as session:
        person = session.query(Person).all()
        for p in person:
            print(p)


if __name__ == "__main__":
    main()