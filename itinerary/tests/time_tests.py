import unittest
from time_functions import *
import itin_examples

class TestTimeValidation(unittest.TestCase):
    def test_validate_nooverlap(self):
        assertTrue(validate_nooverlap(itin1))
        assertFalse(validate_nooverlap(itin12))
        assertFalse(validate_nooverlap(itin13))
        assertFalse(validate_nooverlap(itin14))
        assertFalse(validate_nooverlap(itin9))
    def test_validate_chrono(self):
        assertTrue(validate_chrono(itin1))
        assertTrue(validate_chrono(itin10))
        assertTrue(validate_chrono(itin12))
        assertTrue(validate_chrono(itin13))
        assertFalse(validate_chrono(itin9))
        assertFalse(validate_chrono(itin14))
    def test_validate_isopen(self):
        assertTrue(validate_isopen(itin1,"mon"))
        assertTrue(validate_isopen(itin1,"tues"))
        assertTrue(validate_isopen(itin1,"wed"))
        assertTrue(validate_isopen(itin1,"thurs"))
        assertTrue(validate_isopen(itin1,"fri"))
        assertTrue(validate_isopen(itin1,"sat"))
        assertTrue(validate_isopen(itin1,"sun"))
        assertFalse(validate_isopen(itin15,"mon"))
        assertFalse(validate_isopen(itin15,"tues"))
        assertFalse(validate_isopen(itin15,"wed"))
        assertFalse(validate_isopen(itin15,"thurs"))
        assertFalse(validate_isopen(itin15,"fri"))
        assertFalse(validate_isopen(itin15,"sat"))
        assertFalse(validate_isopen(itin15,"sun"))
    def test_validate_within_usertime(self):
        assertFalse(validate_within_usertime(itin1,[800,1000]))
        assertFalse(validate_within_usertime(itin1,[630,850]))
        assertTrue(validate_within_usertime(itin1,[600,950]))




if __name__ == '__main__':
    unittest.main()        
