import telnetlib
from typing import List, Optional

from .error_codes import RCIError as Error
from .abstracts import AbstractCommunicator
from .command_builders import TelnetCommandBuilder


class TelnetCommunicator(AbstractCommunicator):
    """
    Handles Telnet communications. This class uses the metaclass=SingletonMeta to ensure there is only one instance
    of the TelnetCommunicator class.
    """

    host: str
    port: int
    _connection: Optional[telnetlib.Telnet]
    command_builder: TelnetCommandBuilder

    def __init__(self, host: str, port: int = 25000) -> None:
        """
        Initialize a Telnet communicator.

        Args:
            host (str): Host address.
            port (int, optional): Port number. Defaults to 25000.
        """
        self.host = host
        self.port = port
        self._connection = None
        self._connection = self._connect()
        self.command_builder = TelnetCommandBuilder()

    def _connect(self) -> Optional[telnetlib.Telnet]:
        """
        Establish a Telnet connection.

        Returns:
            telnetlib.Telnet: Telnet connection or None if an error occurred.
        """
        try:
            self._connection = telnetlib.Telnet(self.host, self.port)
            self._connection.read_until(b"cmd: ", 10)
            self._connection.write(b"\r\n")
            self._connection.read_until(b"cmd: ", 10)
            return self._connection
        except Exception as e:
            print(f"Error connecting to {self.host}: {e}")
            return None

    def send(self, command: str) -> None:
        """
        Send a Telnet command.

        Args:
            command (str): Command to be sent.
        """
        self._connection.write(command.encode("ascii") + b"\r\n")

    def receive(self, timeout: int = 10) -> List[str]:
        """
        Receive a response from the Telnet connection.

        Args:
            timeout (int, optional): Time in seconds to wait for a response. Defaults to 10.

        Returns:
            List[str]: List of response lines.
        """
        try:
            response = self._connection.read_until(b"cmd: ", timeout)
            return response.decode("ascii").split("\n")
        except Exception as e:
            print(f"Error receiving data: {e}")
            return [str(Error)]

    def send_and_receive(self, command: str) -> list[str]:
        """
        Send a command and immediately attempt to receive a response.

        Args:
            command (str): Command to be sent.

        Returns:
            List[str]: List of response lines.
        """
        self.send(command)
        return self.receive()

    def close(self) -> None:
        """
        Close the Telnet connection.
        """
        if self._connection:
            self._connection.close()
