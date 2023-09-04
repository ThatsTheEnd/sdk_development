import json
from typing import Any, Dict, List


def format_message(command: str, parameters: Dict[str, Any], id: int) -> Dict[str, Any]:
    """
    Format a message for sending.

    Args:
        command (str): The command to format.
        parameters (Dict[str, Any]): Additional parameters for the command.
        id (int): The ID for the message.

    Returns:
        Dict[str, Any]: Formatted message.
    """
    return {
        "id": id,
        "command": command,
        "parameters": parameters
    }


def parse_received_message(message: str) -> Dict[str, Any]:
    """
    Parse a received message into a structured format.

    Args:
        message (str): The raw message string.

    Returns:
        Dict[str, Any]: Parsed message with structured errors.
    """
    parsed = json.loads(message)

    # Handle potential future changes in the error format
    if "errors" in parsed:
        parsed["errors"] = parse_errors(parsed["errors"])

    return parsed


def parse_errors(errors: List[str]) -> List[Dict[str, Any]]:
    """
    Parse errors into a more structured format.

    Args:
        errors (List[str]): List of raw error strings.

    Returns:
        List[Dict[str, Any]]: List of parsed errors with structured information.
    """
    structured_errors = []
    for error in errors:
        if ";" in error:
            _, error_code, error_message = error.split(";", 2)
            structured_errors.append({
                "error_code": error_code,
                "error_message": error_message
            })
        else:
            structured_errors.append({"error_message": error})
    return structured_errors
