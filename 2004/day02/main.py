file_name = 'input.txt'

safe_count = 0
safe_count_second_round = 0

unsafe_columns = []

def check_safe(column):

    direction = 'desc' if column[0] > column[1] else 'inc'
    is_safe = True

    for i in range(len(column) - 1):
        diff = column[i] - column[i + 1]

        if 1 <= abs(diff) <= 3:
            if (direction == 'desc' and diff > 0) or (direction == 'inc' and diff < 0):
                continue
            else:
                is_safe = False
                break
        else:
            is_safe = False
            break

    return is_safe

def generate_sublists(column):
    return [column[:i] + column[i + 1:] for i in range(len(column))]

with open(file_name, 'r') as file:
    for line in file:
        columns = list(map(int, line.strip().split()))
        if check_safe(columns):
            safe_count += 1
        else:
            unsafe_columns.append(generate_sublists(columns))

for sublists in unsafe_columns:
    for sublist in sublists:
        if check_safe(sublist):
            safe_count_second_round += 1
            break;

print(safe_count)
print(safe_count + safe_count_second_round)
