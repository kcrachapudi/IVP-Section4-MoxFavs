from src import favorites

def deploy_favorites():
    favorites_contract = favorites.deploy()
    start_number = favorites_contract.retrieve()
    print("Start number: ", start_number)
    favorites_contract.store(84)
    updated_number = favorites_contract.retrieve()
    print("Updated number: ", updated_number)
    return favorites_contract


def moccasin_main():
    deploy_favorites()
