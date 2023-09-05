import json
import websockets
from typing import Any, Dict
from .base_communication import Communication
from .message_parser import format_message, parse_received_message

# type: ignore[attr-defined]
# mypy doesn't find the connection methods


class WebSocketClient(Communication):
    """
    Concrete implementation of the Communication contract using WebSockets.

    Attributes:
        uri (str): The WebSocket URI to connect to.
        websocket (WebSocketClient, optional): The active WebSocket connection.

    Methods inherited from Communication:
        connect, disconnect, send, receive
    """

    def __init__(self, uri: str) -> None:
        """
        Initialize a WebSocketClient.

        Args:
            uri (str): The WebSocket URI to connect to.
        """
        self.uri = uri
        self.websocket = None

    async def connect(self) -> None:
        """Establish a WebSocket connection to the provided URI."""
        self.websocket = await websockets.connect(self.uri)  # pylint: disable=no-member, type: ignore[attr-defined]

    async def disconnect(self) -> None:
        """Close the active WebSocket connection if one exists."""
        if self.websocket:
            await self.websocket.close()
            self.websocket = None

    async def send(
        self, command: str, parameters: Dict[str, Any], message_id: int = 0
    ) -> None:
        """
        Send a command message over the WebSocket connection.

        Args:
            command (str): The command to send.
            parameters (Dict[str, Any], optional): Additional parameters for the command. Defaults to {}.
            message_id (int, optional): The ID of the message. Defaults to 0.
        """
        message = format_message(command, parameters, message_id)
        await self.websocket.send(json.dumps(message))  # type: ignore[attr-defined]

    async def receive(self) -> Dict[str, Any]:
        """Await and receive a message response from the WebSocket. Returns the parsed message."""
        response = await self.websocket.recv()  # type: ignore[attr-defined]
        return parse_received_message(response)


class MessageParsingError(Exception):
    """Exception raised for errors in the input message format."""

    def __init__(self, message: str = "Message format is invalid") -> None:
        self.message = message
        super().__init__(self.message)
