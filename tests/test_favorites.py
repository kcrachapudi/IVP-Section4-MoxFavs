from script.deploy import deploy_favorites

def test_fav_number():
    #arrange
    favorites_contract = deploy_favorites()
    #act
    fav_number = favorites_contract.retrieve()
    #assert
    assert fav_number == 84

def test_can_change_fav_number():
    #Arrange
    favorites_contract = deploy_favorites()
    #Act
    favorites_contract.store(33)
    fav_number = favorites_contract.retrieve()
    #Assert
    assert fav_number == 33

def test_can_add_people():
    #Arrange
    new_person = "Becca"
    new_fav_number = 13
    favorites_contract = deploy_favorites()
    #Act
    favorites_contract.add_person(new_person, new_fav_number)
    #Assert
    assert favorites_contract.list_of_people(0) == (new_fav_number, new_person)