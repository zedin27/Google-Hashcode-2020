import numpy as np

with open("testcases/a_example.txt") as file_in:
	lines = []
	count = 0;
	for line in file_in:
		print(count)
		count += 1
		lines.append(line.rstrip())
	print(lines)

# with open("testcases/b_read_on.txt") as file_in:
# 	lines = []
# 	for line in file_in:
# 		lines.append(line.rstrip())
# 	print(lines)
#
# with open("testcases/c_incunabula.txt") as file_in:
# 	lines = []
# 	for line in file_in:
# 		lines.append(line.rstrip())
# 	print(lines)
#
# with open("testcases/e_so_many_books.txt") as file_in:
# 	lines = []
# 	for line in file_in:
# 		lines.append(line.rstrip())
# 	print(lines)
#
# with open("testcases/f_libraries_of_the_world.txt") as file_in:
# 	lines = []
# 	for line in file_in:
# 		lines.append(line.rstrip())
# 	print(lines)
