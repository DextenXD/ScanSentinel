from unittest.mock import patch
from scansentinel.hostDiscovery import HostDiscovery

@patch("scansentinel.hostDiscovery.ping")
def test_host_discovery_found(mock_ping):
  mock_ping.return_value.success.return_value = True

  hd = HostDiscovery()
  alive = hd.discover(["192.168.1.1"])

  assert len(alive) == 1
  assert alive[0] == "192.168.1.1"

@patch("scansentinel.hostDiscovery.ping")
def test_host_discovery_dead(mock_ping):
  mock_ping.return_value.success.return_value = False

  hd = HostDiscovery()
  alive = hd.discover(["192.168.1.1"])

  assert len(alive) == 0

