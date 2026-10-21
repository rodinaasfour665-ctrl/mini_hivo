import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import unittest
from numbers_api import clamp_number

class ClampBehavior(unittest.TestCase):
    def test_above_upper(self): self.assertEqual(clamp_number(99, 0, 10), 10)
    def test_below_lower(self): self.assertEqual(clamp_number(-2, 0, 10), 0)
    def test_inside(self): self.assertEqual(clamp_number(2.5, 0, 10), 2.5)
    def test_boundary(self): self.assertEqual(clamp_number(10, 0, 10), 10)
    def test_inverted_bounds(self):
        with self.assertRaises(ValueError): clamp_number(4, 10, 0)

if __name__ == '__main__': unittest.main(verbosity=2)
