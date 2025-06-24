import pytest
from main import Person, create_person_list  # Імпортуй свої класи


def test_create_person_list() -> None:

    Person.people = {}

    people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Rachel", "age": 28, "husband": "Ross"}
    ]

    person_list = create_person_list(people)

    assert isinstance(person_list[0], Person)
    assert person_list[0].name == "Ross"
    assert person_list[0].wife is person_list[2]
    assert person_list[0].wife.name == "Rachel"
    assert person_list[1].name == "Joey"

    with pytest.raises(AttributeError):
        person_list[1].wife

    assert isinstance(person_list[2], Person)
    assert person_list[2].name == "Rachel"
    assert person_list[2].husband is person_list[0]
