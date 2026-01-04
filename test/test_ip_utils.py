import pytest
from scansentinel.util import parse_targets

def test_singe_ip():
  assert parse_targets("192.168.1.1") == ["192.168.1.1"]

def test_cidr_block():
  result = parse_targets("192.168.1.0/30")
  assert len(result) == 4
  assert "192.168.1.0" in result
  assert "192.168.1.3" in result

def test_rage_dash():
  result = parse_targets("192.168.1.1-192.168.1.3")
  assert result == ["192.168.1.1", "192.168.1.2", "192.168.1.3"]