from abc import ABC, abstractmethod
from typing import Any, Dict, TypeVar

T = TypeVar("T", bound="SingletonMeta")


class SingletonMeta(type):
    """
    The SingletonMeta metaclass ensures that there's only one instance of any class that uses it as its metaclass.
    """

    _instances: Dict[T, T] = {}

    def __call__(cls: T, *args: Any, **kwargs: Any) -> T:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AbstractCommandBuilder(ABC):
    """
    Abstract base class for building commands.
    """

    @staticmethod
    @abstractmethod
    def build(device_id: int, command: str, **kwargs: Any) -> str:
        """
        Abstract method to build a command.

        Args:
            device_id (int): ID of the device.
            command (str): Command to be sent.
            **kwargs: Additional keyword arguments.
        """
        pass


class AbstractCommunicator(ABC):
    """
    Abstract base class for communication protocols.
    """

    @abstractmethod
    def _connect(self) -> None:
        """
        Abstract method to establish a connection.
        """
        pass

    @abstractmethod
    def send(self, command: str) -> None:
        """
        Abstract method to send a command.

        Args:
            command (str): Command to be sent.
        """
        pass

    @abstractmethod
    def receive(self, timeout: int = 10) -> str:
        """
        Abstract method to receive a response.

        Args:
            timeout (int, optional): Time in seconds to wait for a response. Defaults to 10.

        Returns:
            str: The received response.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Abstract method to close the connection.
        """
        pass
