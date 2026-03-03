# test_decentralvault.py
"""
Tests for DecentralVault module.
"""

import unittest
from decentralvault import DecentralVault

class TestDecentralVault(unittest.TestCase):
    """Test cases for DecentralVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentralVault()
        self.assertIsInstance(instance, DecentralVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentralVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
