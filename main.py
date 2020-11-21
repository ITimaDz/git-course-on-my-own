s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
length = {('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800}

def roman_to_arabic(roman_number):
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
        self.assertEquals(roman_to_arabic('I'), 1)
        self.assertEquals(roman_to_arabic('II'), 2)
        self.assertEquals(roman_to_arabic('III'), 3)
        self.assertEquals(roman_to_arabic('IV'), 4)
        self.assertEquals(roman_to_arabic('V'), 5)
        self.assertEquals(roman_to_arabic('VI'), 6)
        self.assertEquals(roman_to_arabic('VII'), 7)
        self.assertEquals(roman_to_arabic('VIII'), 8)
        self.assertEquals(roman_to_arabic('IX'), 9)
        self.assertEquals(roman_to_arabic('X'), 10)
        self.assertEquals(roman_to_arabic('XXXI'), 31)
        self.assertEquals(roman_to_arabic('XLVI'), 46)
        self.assertEquals(roman_to_arabic('XCIX'), 99)
        self.assertEquals(roman_to_arabic('DLXXXIII'), 583)
        self.assertEquals(roman_to_arabic('DCCCLXXXVIII'), 888)
        self.assertEquals(roman_to_arabic('MDCLXVIII'), 1668)
        self.assertEquals(roman_to_arabic('MCMLXXXIX'), 1989)
        self.assertEquals(roman_to_arabic('MMX'), 2010)
        self.assertEquals(roman_to_arabic('MMXI'), 2011)
        self.assertEquals(roman_to_arabic('MMXII'), 2012)
        self.assertEquals(roman_to_arabic('MMMCMXCIX'), 3999)

print(roman_to_arabic('III'))
print(roman_to_arabic('IV'))
print(roman_to_arabic('IX'))
print(roman_to_arabic('LVIII'))
print(roman_to_arabic('MCMXCIV'))
