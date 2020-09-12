# -*- coding: utf-8 -*-

from .context import swarmclients

import unittest

sc = swarmclients.SwarmClient(1)

class TestSwarmClient(unittest.TestCase):
    """Basic test cases."""

    def test_sc_id (self):
        assert sc.id == 1

    def test_sc_writebuffer (self):
        sc.tx_buffer += b'Hello'
        assert sc.tx_buffer[:5] == bytearray(b'Hello')
        sc.tx_buffer.clear()
        assert sc.tx_buffer == bytearray(b'')

    def test_sc_readbuffer (self):
        sc.rx_buffer += b'Hallo'
        assert sc.rx_buffer[:5] == bytearray(b'Hallo')
        sc.rx_buffer.clear()
        assert sc.rx_buffer == bytearray(b'')

    def test_sc_failcounter (self):
        assert sc.fail_counter == 0
        sc.fail_counter +=1
        assert sc.fail_counter == 1
    def test_sc_xx (self):
        sc.prio = 100
        assert sc.prio == 100
        sc.prio += 1
        assert sc.prio == 101
        
    

if __name__ == '__main__':
    unittest.main()