import json
from .abstracts import AbstractCommandBuilder


class TelnetCommandBuilder(AbstractCommandBuilder):
    """
    Builds commands for Telnet communication.
    """

    @staticmethod
    def build(device_id, command, **kwargs):
        """
        Build a Telnet command.

        Args:
            device_id (int): ID of the device.
            command (str): Command to be sent.
            **kwargs: Additional keyword arguments.

        Returns:
            str: Formatted Telnet command.
        """
        command_parts = [command, str(device_id)]
        command_parts.extend(str(value) for value in kwargs.values())
        return " ".join(command_parts)


class WebSocketCommandBuilder(AbstractCommandBuilder):
    """
    Builds commands for WebSocket communication.
    """

    @staticmethod
    def build(device_id, command, **kwargs):
        """
        Build a WebSocket command in JSON format.

        Args:
            device_id (int): ID of the device.
            command (str): Command to be sent.
            **kwargs: Additional keyword arguments.

        Returns:
            str: Formatted WebSocket command as a JSON string.
        """
        cmd_dict = {
            "id": device_id,
            "command": command,
            "parameters": kwargs
        }
        return json.dumps(cmd_dict)
