import json
from sdk_development.communication import (
    format_message,
    parse_received_message,
)  # Adjust the import statement based on your module name


def test_format_message():
    # Sample data
    cmd = "test_command"
    params = {"key1": "value1", "key2": 2}
    msg_id = 1

    # Expected result
    expected = {"id": msg_id, "command": cmd, "parameters": params}

    assert format_message(cmd, params, msg_id) == expected


def test_parse_received_message_without_errors():
    # Sample message
    message = json.dumps(
        {
            "id": 1,
            "command": "test_command",
            "results": {"key1": "value1"},
            "errors": [],
        }
    )

    expected = {
        "id": 1,
        "command": "test_command",
        "results": {"key1": "value1"},
        "errors": [],
    }

    assert parse_received_message(message) == expected


def test_parse_received_message_with_errors():
    # Sample message with errors
    message = json.dumps(
        {
            "id": 1,
            "command": "test_command",
            "results": {},
            "errors": ["[E];001;Sample error", "General error without code"],
        }
    )

    # Expected structured errors based on the parse_errors function
    expected = {
        "id": 1,
        "command": "test_command",
        "results": {},
        "errors": [
            {"error_code": "001", "error_message": "Sample error"},
            {"error_message": "General error without code"},
        ],
    }

    assert parse_received_message(message) == expected
