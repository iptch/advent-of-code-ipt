import sys, math

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day01/input.txt", "r")

sequence = []

while True:
    line = file.readline()
    if not line:
        break
    
    sequence.append((line[0], line[1:]))

file.close()

total_score = 0

# puzzle 1
position = 50
for move in sequence:
    if move[0] == 'L':
        position = (position - int(move[1])) % 100
    else:
        position = (position + int(move[1])) % 100
    if position == 0: 
        total_score += 1
        
print(total_score)


# puzzle 2
total_score = 0

position = 50
for move in sequence:
    print(position, move, total_score)
    total_score += int(move[1]) // 100
    if move[0] == 'L':
        new_position = (position - int(move[1])) % 100
        if int(move[1]) % 100 >= position:
            if position != 0:
                total_score += 1
    else:
        new_position = (position + int(move[1])) % 100
        if  int(move[1]) % 100 > 99 - position:
            total_score += 1
    position = new_position
                
print(total_score)
