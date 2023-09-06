"""
base_communication.py

A foundational module providing an abstract base class for defining the communication
contract. The `Communication` class lays out the blueprint for communication methods
that any concrete implementation must provide.

The abstract methods in this class ensure that any derived class will have a consistent
interface for connecting, disconnecting, sending, and receiving messages, enabling
flexible and standardized communication across different mediums or protocols.

Classes:
- Communication: Abstract base class that provides a contract for communication methods.

Dependencies:
- abc: For abstract base class support.
- typing: For type annotations.
"""

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
    async def connect(self) -> None:
        """Establish a connection."""
        pass

    @abstractmethod
    async def disconnect(self) -> None:
        """Terminate an existing connection."""
        pass

    @abstractmethod
    async def send(
        self, command: str, parameters: Dict[str, Any], message_id: int = 0
    ) -> None:
        """
        Send a command message.

        Args:
            command (str): The command to send.
            parameters (Dict[str, Any], optional): Additional parameters for the command. Defaults to {}.
            message_id (int, optional): The ID of the message. Defaults to 0.
        """
        pass

    @abstractmethod
    async def receive(self) -> Dict[str, Any]:
        """Await and receive a message response. Returns the parsed message."""
        pass
