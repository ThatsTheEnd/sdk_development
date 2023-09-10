import pytest
import os
from sdk_development.communication import TelnetCommunicator


@pytest.fixture(scope="function")
def reset_singleton():
    """Fixture to reset the singleton instance before each test."""
    TelnetCommunicator._instances = {}
    yield
    TelnetCommunicator._instances = {}


@pytest.fixture
def communicator_class():
    if os.environ.get("HAS_HARDWARE") == "true":
        return TelnetCommunicator
    else:
        return MockedTelnetCommunicator


def test_telnet_communicator_open_close_connection(reset_singleton, communicator_class):
    communicator = communicator_class(host="localhost", port=25000)

    # Try closing
    try:
        communicator.close()
    except Exception as e:
        pytest.fail(f"Closing the connection resulted in an error: {e}")


def test_telnet_communicator_send_invalid_command(reset_singleton, communicator_class):
    expected_response = ["\r", "Error: Unknown command\r", "-501\r", "cmd: "]
    communicator = communicator_class(host="localhost", port=25000)
    # Try sending invalid command
    response = communicator.send_and_receive("bla")
    communicator.close()
    assert response == expected_response


def test_telnet_communicator_send_help(reset_singleton):
    expected_partial_response = [
        "\r",
        "\r",
        "Remote Command Interface Commands:\r",
        " Node Commands\r",
        "    exit                        - Disconnect\r",
    ]
    communicator = TelnetCommunicator(host="localhost", port=25000)
    # Try sending valid command
    response = communicator.send_and_receive("help")
    communicator.close()
    # Then the first five elements of the response matches the expected partial response
    assert response[:5] == expected_partial_response


class MockedTelnetCommunicator:
    """Mocked class to simulate communication"""
    def __init__(self, host, port=25000):
        self.command = ''

    def send(self, command):
        self.command = command

    def receive(self, timeout=10):
        # Just for this example, we'll simulate responses based on specific commands
        if self.command == "bla":
            return ["\r", "Error: Unknown command\r", "-502\r", "cmd: "]
        elif self.command == "help":
            return [
                "\r",
                "\r",
                "Remote Command Interface Commands:\r",
                " Node Commands\r",
                "    exit                        - Disconnect\r",
            ]
        else:
            return ["cmd: "]  # Default response

    def send_and_receive(self, command):
        self.send(command)
        return self.receive()  # Simulate by directly returning a response

    def close(self):
        pass  # This won't actually close any connection since it's mocked

