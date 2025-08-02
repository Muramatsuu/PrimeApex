# test_primeapex.py
"""
Tests for PrimeApex module.
"""

import unittest
from primeapex import PrimeApex

class TestPrimeApex(unittest.TestCase):
    """Test cases for PrimeApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeApex()
        self.assertIsInstance(instance, PrimeApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
