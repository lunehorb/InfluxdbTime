# test_influxdbtime.py
"""
Tests for InfluxdbTime module.
"""

import unittest
from influxdbtime import InfluxdbTime

class TestInfluxdbTime(unittest.TestCase):
    """Test cases for InfluxdbTime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfluxdbTime()
        self.assertIsInstance(instance, InfluxdbTime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfluxdbTime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
