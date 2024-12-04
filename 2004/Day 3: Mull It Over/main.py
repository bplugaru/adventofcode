import re

file_name = 'input.txt'

def p1(content):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, content)
    total_sum = 0
    for match in matches:
        total_sum += int(match[0]) * int(match[1])
    
    return total_sum;

def p2(content):
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    matches = re.findall(pattern, content)
    total_sum = 0
    enabled = True
    for match in matches:
        nums = re.findall(r"\d+", match)
        
        if not nums:
            enabled = "do()" in match
        elif enabled:
            total_sum += int(nums[0]) * int(nums[1])
    return total_sum



with open(file_name, 'r') as file:
    content = file.read()

sum_p1 = p1(content)
sum_p2 = p2(content)
print(sum_p1)
print(sum_p2)

