import unittest
from common import *

class TestMethods(unittest.TestCase):

    def test_has_req_fields(self):
        self.assertTrue(has_req_fields("eyr:2028 pid:494999718 byr:1928 hgt:176cm iyr:2015 ecl:oth hcl:#733820"))
        self.assertFalse(has_req_fields("eyr:2028 pid:494999718 byr:1928 hgt:176cm iyr:2015 ecl:oth"))

    def test_valid_birthyear(self):
        self.assertTrue(valid_birthyear(1920))
        self.assertTrue(valid_birthyear(2002))

        self.assertFalse(valid_birthyear(1919))
        self.assertFalse(valid_birthyear(2003))

    def test_valid_issueyear(self):
        self.assertTrue(valid_issueyear(2010))
        self.assertTrue(valid_issueyear(2020))

        self.assertFalse(valid_issueyear(2009))
        self.assertFalse(valid_issueyear(2021))

    def test_valid_expiration(self):
        self.assertTrue(valid_expiration(2020))
        self.assertTrue(valid_expiration(2030))

        self.assertFalse(valid_expiration(2019))
        self.assertFalse(valid_expiration(2031))
    
    def test_valid_height_cm(self):
        self.assertTrue(valid_height("150cm"))
        self.assertTrue(valid_height("193cm"))

        self.assertFalse(valid_height("149cm"))
        self.assertFalse(valid_height("194cm"))
    
    def test_valid_height_in(self):
        self.assertTrue(valid_height("59in"))
        self.assertTrue(valid_height("76in"))

        self.assertFalse(valid_height("58in"))
        self.assertFalse(valid_height("77in"))
    
    def test_valid_haircolor(self):
        self.assertTrue(valid_haircolor("#123abc"))

        self.assertFalse(valid_haircolor("#123ab"))
        self.assertFalse(valid_haircolor("#123abg"))
        self.assertFalse(valid_haircolor("#123abcd"))

    def test_valid_eyecolor(self):
        self.assertTrue(valid_eyecolor("amb"))
        self.assertTrue(valid_eyecolor("brn"))
        self.assertTrue(valid_eyecolor("oth"))

        self.assertFalse(valid_eyecolor("brw"))
        self.assertFalse(valid_eyecolor("br"))
    
    def test_valid_passportid(self):
        self.assertTrue(valid_passportid("123456789"))
        self.assertTrue(valid_passportid("000012345"))

        self.assertFalse(valid_passportid("0123456789"))
        self.assertFalse(valid_passportid("12345678"))
        self.assertFalse(valid_passportid("12345678a"))

if __name__ == '__main__':
    unittest.main()
