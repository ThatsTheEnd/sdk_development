from abc import ABC, abstractmethod
from typing import Any, Dict


class Communication(ABC):
    """
    Abstract base class for defining the communication contract.

    Methods:
        connect: Establish a connection.
        disconnect: Terminate an existing connection.
        send: Send a command message.
        receive: Await and receive a message response.
    """

    @abstractmethod
    def connect(self) -> None:
        """Establish a connection."""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """Terminate an existing connection."""
        pass

    @abstractmethod
    def send(self, command: str, parameters: Dict[str, Any] = {}, id: int = 0) -> None:
        """
        Send a command message.

        Args:
            command (str): The command to send.
            parameters (Dict[str, Any], optional): Additional parameters for the command. Defaults to {}.
            id (int, optional): The ID of the message. Defaults to 0.
        """
        pass

    @abstractmethod
    def receive(self) -> Dict[str, Any]:
        """Await and receive a message response. Returns the parsed message."""
        pass
