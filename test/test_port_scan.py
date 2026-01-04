from unittest.mock import MagicMock, patch
from scansentinel.portscanner import PortScanner

def test_port_scan_open():
  scanner = PortScanner()

  with patch("socket.socket") as mock_socket:
    mock_socket.return_value.__enter__.return_value.connect_ex.return_value = 0

    result = scanner.scan_host("127.0.0.1", [80])
    assert 80 in result

def test_port_scan_closed():
  scanner = PortScanner()

  with patch("socket.socket") as mock_socket:
    mock_socket.return_value.__enter__.return_value.connect_ex.return_value = 111

    result = scanner.scan_host("127.0.0.1", [80])
    assert result == []