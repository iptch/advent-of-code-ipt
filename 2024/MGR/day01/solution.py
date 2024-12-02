import sys, math

file = open("/home/manuelgr/advent-of-code-ipt/2024/MGR/day01/input.txt", "r")

left_list = []
right_list = []

while True:
    line = file.readline()
    split_line = line.split("   ")
    
    if len(split_line) == 2:
        left_list.append(split_line[0])
        right_list.append(split_line[1])
    
    if not line:
        break

file.close()

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

if len(left_list) != len(right_list):
    print("ERROR")
    
sum = 0
for i in range(0, len(sorted_left_list)):
    left_elem, right_elem = sorted_left_list[i], sorted_right_list[i]
    sum += abs(int(left_elem) - int(right_elem))

print(sum)

left_dict = {}
right_dict = {}

for right_elem in right_list:
    right_dict[int(right_elem)] = right_dict.get(int(right_elem), 0) + 1

similarity_score = 0
for left_elem in left_list:
    similarity_score += int(left_elem) * right_dict.get(int(left_elem), 0)

print(similarity_score)