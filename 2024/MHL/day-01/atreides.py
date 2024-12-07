print("""The Great House of: """)
print("""ATREIDES ATREIDES ATREIDES""")

path = 'data.txt'

with open(path, 'r', encoding='utf-8') as datei:
    input_data = datei.read()

lines = input_data.splitlines()
lines = [line for line in lines if line.strip()]
left = []
right = []
for line in lines:
    line: list = line.split()
    left.append(int(line[0]))
    right.append(int(line[1]))
left = sorted(left)
right = sorted(right)
distance: int = 0

for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
print("""ATREIDES ATREIDES ATREIDES""")