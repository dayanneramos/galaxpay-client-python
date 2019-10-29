import pytest
from dynaconf import settings


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(
        galaxId="5473",
        galaxHash="83Mw5u8988Qj6fZqS4Z8K7LzOo1j28S706R0BeFe"
    )
