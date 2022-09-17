class Solution(object):
    def letterCombinations(self, digits):
        temp_word = ""
        letters = []
        digits_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return letters
        elif len(digits) == 1:
            for letter in digits_dict[digits[0]]:
                letters.append(letter)
            return letters
        elif len(digits) == 2:
            for letter1 in digits_dict[digits[0]]:
                for letter2 in digits_dict[digits[1]]:
                    letters.append(letter1+letter2)
            return letters

        elif len(digits) == 3:
            for letter1 in digits_dict[digits[0]]:
                for letter2 in digits_dict[digits[1]]:
                    for letter3 in digits_dict[digits[2]]:
                        letters.append(letter1+letter2+letter3)
            return letters

        elif len(digits) == 4:
            for letter1 in digits_dict[digits[0]]:
                for letter2 in digits_dict[digits[1]]:
                    for letter3 in digits_dict[digits[2]]:
                        for letter4 in digits_dict[digits[3]]:
                            letters.append(letter1+letter2+letter3+letter4)
            return letters