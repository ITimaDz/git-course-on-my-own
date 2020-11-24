class Solution:
    ROMAN_NUMBERS_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    DIFFERENCE_ROMAN_NUMBER = {
        ('I', 'V'): 3, ('I', 'X'): 8, ('X', 'L'): 30, ('X', 'C'): 80, ('C', 'D'): 300, ('C', 'M'): 800
    }

    def form_roman_to_int(self, roman_number: str) -> int:
        num = 0
        prev_literal = None
        for literal in roman_number:
            if prev_literal and self.ROMAN_NUMBERS_DICT[prev_literal] < self.ROMAN_NUMBERS_DICT[literal]:
                num += self.DIFFERENCE_ROMAN_NUMBER[(prev_literal, literal)]
            else:
                num += self.ROMAN_NUMBERS_DICT[literal]
            prev_literal = literal
        return num

    if str(1) <= str(ROMAN_NUMBERS_DICT) <= str(15):
        length = len(ROMAN_NUMBERS_DICT)
        print(True)
    else:
        print(False)











