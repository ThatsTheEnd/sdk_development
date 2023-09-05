from sdk_development.communication import WebSocketClient  # , MessageParsingError

# from sdk_development.utils import Result, Error


def test_initialization():
    client = WebSocketClient(uri="ws://example.com")
    assert client.uri == "ws://example.com"


# def test_connect(mocker):
#     mocker.patch("sdk_development.communication.websocket.connect")
#     client = WebSocketClient(uri="ws://example.com")
#     result = client.connect()
#     assert result.isSuccess == True
#
#
# def test_send_command(mocker):
#     mock_ws = mocker.MagicMock()
#     mocker.patch(
#         "sdk_development.communication.websocket.connect", return_value=mock_ws
#     )
#     client = WebSocketClient(uri="ws://example.com")
#     client.connect()
#     result = client.send("test_command")
#     assert result.isSuccess == True
#     mock_ws.send_json.assert_called_with(
#         {"id": mocker.ANY, "command": "test_command", "parameters": {}}
#     )
#
#
# def test_receive_valid_message(mocker):
#     mock_ws = mocker.MagicMock()
#     mock_ws.recv_json.return_value = {
#         "id": 1,
#         "command": "test_command",
#         "results": {"key": "value"},
#         "errors": [],
#     }
#     mocker.patch(
#         "sdk_development.communication.websocket.connect", return_value=mock_ws
#     )
#     client = WebSocketClient(uri="ws://example.com")
#     client.connect()
#     result = client.receive()
#     assert result.isSuccess == True
#     assert result.getValue() == {"key": "value"}
#
#
# def test_receive_invalid_message(mocker):
#     mock_ws = mocker.MagicMock()
#     mock_ws.recv_json.return_value = {"invalid": "message"}
#     mocker.patch(
#         "sdk_development.communication.websocket.connect", return_value=mock_ws
#     )
#     client = WebSocketClient(uri="ws://example.com")
#     client.connect()
#     result = client.receive()
#     assert result.isSuccess == False
#     assert isinstance(result.getError(), MessageParsingError)
#
#
# def test_disconnect(mocker):
#     mock_ws = mocker.MagicMock()
#     mocker.patch(
#         "sdk_development.communication.websocket.connect", return_value=mock_ws
#     )
#     client = WebSocketClient(uri="ws://example.com")
#     client.connect()
#     result = client.disconnect()
#     assert result.isSuccess == True
#     mock_ws.close.assert_called_once()
