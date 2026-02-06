import pytest
from moccasin.boa_tools import VyperContract
from script.deploy import deploy_favorites

@pytest.fixture
def favorites_contract(scope: str = "session") -> VyperContract:
    return deploy_favorites()
