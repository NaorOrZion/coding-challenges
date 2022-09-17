class Solution(object):
    def reorderedPowerOf2(self, n):
        reordered_numbers = []
        count_reordered_possibilities = self.calc_reordered_possiblities(n)
        disassembled_num_list = self.dismantle_number(n)
        i = 0
        while i < count_reordered_possibilities:
            random_digits_num = self.gen_random_num(disassembled_num_list)
            if random_digits_num not in reordered_numbers:
                reordered_numbers.append(random_digits_num)
                i += 1
            if len(str(random_digits_num)) != len(str(n)): # Because the int() function removes the zeros if existed at the beginning of a number
                reordered_numbers.remove(random_digits_num)
                count_reordered_possibilities -= 1
                i -= 1
        
        return self.is_power_of_two(reordered_numbers)
    
    
    def is_power_of_two(self, reordered_numbers):
        for number in reordered_numbers:
            if sqrt(number).is_integer():
                return True
          

    def calc_reordered_possiblities(self, n):
        length_num = len(str(n))
        previous_reorder_possibility = 1
        for length_current_number in range(2, length_num+1):
            previous_reorder_possibility *= length_current_number
            
        return previous_reorder_possibility
    
    
    def gen_random_num(self, original_digits_list):
        digits_list = list(original_digits_list)
        rand_number_generated = []
        len_list = len(digits_list)
        i = 0
        while i < len_list:
            outcome = random.choice(digits_list)
            rand_number_generated.append(str(outcome))
            digits_list.remove(outcome)
            i += 1
            
        return int("".join(rand_number_generated))
    
    
    def dismantle_number(self, n):
        num_digits = []
        n = str(n)
        for i in n:
            num_digits.append(int(i))
        
        return num_digits