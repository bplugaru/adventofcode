import re

def check_diagonals_for_xmas(matrix):
  count = 0
  word_diagonal_main = matrix[0][0]+matrix[1][1]+matrix[2][2]+matrix[3][3];
  if word_diagonal_main == "XMAS" or word_diagonal_main == "SAMX":
    count += 1
  word_diagonal_anti = matrix[0][3]+matrix[1][2]+matrix[2][1]+matrix[3][0];
  if word_diagonal_anti == "XMAS" or word_diagonal_anti == "SAMX":
    count += 1
  return count

def check_diagonals_for_mas(matrix):
  word_diagonal_main = matrix[0][0]+matrix[1][1]+matrix[2][2];
  word_diagonal_anti = matrix[0][2]+matrix[1][1]+matrix[2][0];

  if (word_diagonal_main == "MAS" or word_diagonal_main == "SAM") and (word_diagonal_anti == "MAS" or word_diagonal_anti == "SAM"):
   return 1;  
  return 0;

  
def p1(content):
  count  = 0
  for i in range(len(content)):
    word = ''.join(content[i])
    count += len(re.findall(r'XMAS', word))
    count += len(re.findall(r'SAMX', word))
  for i in range(len(content[0])):
    word = ''.join(content[k][i] for k in range(len(content)))
    count += len(re.findall(r'XMAS', word))
    count += len(re.findall(r'SAMX', word))

  for i in range(len(content)-3):
    for j in range(len(content[i])-3):
      row1 = content[i][j:j+4]
      row2 = content[i+1][j:j+4]
      row3 = content[i+2][j:j+4]
      row4 = content[i+3][j:j+4]
      count += check_diagonals_for_xmas([row1, row2, row3, row4])
  return count


def p2(content):
  count = 0
  for i in range(len(content)-2):
    for j in range(len(content[i])-2):
      row1 = content[i][j:j+3]
      row2 = content[i+1][j:j+3]
      row3 = content[i+2][j:j+3]
      count += check_diagonals_for_mas([row1, row2, row3])
  return count
  
with open("input.txt") as file:
  lines = file.read().splitlines()

content = [list(line) for line in lines]
xmas = p1(content);

x_mas = p2(content);
print(xmas)
print(x_mas)