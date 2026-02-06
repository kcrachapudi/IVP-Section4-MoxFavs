from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites() -> VyperContract:
    favorites_contract: VyperContract = favorites.deploy()
    start_number: int = favorites_contract.retrieve()
    print("Start number: ", start_number)
    favorites_contract.store(84)
    updated_number: int = favorites_contract.retrieve()
    print("Updated number: ", updated_number)

    active_network = get_active_network()
    if active_network.has_explorer():
        verify_result = active_network.moccasin_verify(favorites_contract)
        verify_result.wait_for_verification()
    return favorites_contract


def moccasin_main() -> None:
    deploy_favorites()


# Deploy to Sepolia


# Verify on Sepolia
