from moccasin.boa_tools import VyperContract

def test_fav_number(favorites_contract: VyperContract) -> None:
    #act
    fav_number: int = favorites_contract.retrieve()
    #assert
    assert fav_number == 84

def test_can_change_fav_number(favorites_contract: VyperContract) -> None:
    #Act
    favorites_contract.store(33)
    fav_number: int = favorites_contract.retrieve()
    #Assert
    assert fav_number == 33

def test_can_add_people(favorites_contract: VyperContract) -> None:
    #Arrange
    new_person: str = "Becca"
    new_fav_number: int = 13
    #Act
    favorites_contract.add_person(new_person, new_fav_number)
    #Assert
    assert favorites_contract.list_of_people(0) == (new_fav_number, new_person)