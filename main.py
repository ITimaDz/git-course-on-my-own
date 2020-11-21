s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
length = {('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800}

def from_roman_to_int(roman_number):
    num = 0
    prev_literal = None
    for literal in roman_number:
        if prev_literal and s[prev_literal] < s[literal]:
            num += length[(prev_literal, literal)]
        else:
            num += s[literal]
        prev_literal = literal
    return num

class Solution:
    def romanToInt(self):
        self.assertEquals(from_roman_to_int('I'), 1)
        self.assertEquals(from_roman_to_int('II'), 2)
        self.assertEquals(from_roman_to_int('III'), 3)
        self.assertEquals(from_roman_to_int('IV'), 4)
        self.assertEquals(from_roman_to_int('V'), 5)
        self.assertEquals(from_roman_to_int('VI'), 6)
        self.assertEquals(from_roman_to_int('VII'), 7)
        self.assertEquals(from_roman_to_int('VIII'), 8)
        self.assertEquals(from_roman_to_int('IX'), 9)
        self.assertEquals(from_roman_to_int('X'), 10)
        self.assertEquals(from_roman_to_int('XXXI'), 31)
        self.assertEquals(from_roman_to_int('XLVI'), 46)
        self.assertEquals(from_roman_to_int('XCIX'), 99)
        self.assertEquals(from_roman_to_int('DLXXXIII'), 583)
        self.assertEquals(from_roman_to_int('DCCCLXXXVIII'), 888)
        self.assertEquals(from_roman_to_int('MDCLXVIII'), 1668)
        self.assertEquals(from_roman_to_int('MCMLXXXIX'), 1989)
        self.assertEquals(from_roman_to_int('MMX'), 2010)
        self.assertEquals(from_roman_to_int('MMXI'), 2011)
        self.assertEquals(from_roman_to_int('MMXII'), 2012)
        self.assertEquals(from_roman_to_int('MMMCMXCIX'), 3999)

print(from_roman_to_int('III'))
print(from_roman_to_int('IV'))
print(from_roman_to_int('IX'))
print(from_roman_to_int('LVIII'))
print(from_roman_to_int('MCMXCIV'))
