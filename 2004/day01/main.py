file_name = 'input.txt'


first_column = []
second_column = []

with open(file_name, mode='r') as file:
		for line in file:
				first_column.append(line.split()[0])
				second_column.append(line.split()[1])
first_column.sort();
second_column.sort();



def get_sum(first_column, second_column):
	sum = 0;
	for i in range(len(first_column)):
			sum += abs(int(first_column[i]) - int(second_column[i]))
	return sum

def similar(first_column, second_column):
	prod = 0;
	for i in range(len(first_column)):
			prod += int(second_column.count(first_column[i]))*int(first_column[i])
	return prod

print(get_sum(first_column, second_column))
print(similar(first_column, second_column))

