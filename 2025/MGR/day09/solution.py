import sys, math
from collections import defaultdict
from shapely.geometry import Point, LineString
from shapely.geometry.polygon import Polygon

file = open("/home/manuelgr/advent-of-code-ipt/2025/MGR/day09/input.txt", "r")

input = file.read().splitlines()
file.close()

tiles = set()
for line in input:
    tiles.add((int(line.split(',')[1]), int(line.split(',')[0])))

tiles = sorted(tiles)

max_square = 0
for i in range(len(tiles)-1):
    for j in range(i+1, len(tiles)):
        x = abs(tiles[i][0] - tiles[j][0])
        y = abs(tiles[i][1] - tiles[j][1])
        #if x*y > max_square:
            #print(tiles[i], tiles[j])
        max_square = max(max_square, (x+1)*(y+1))
        
print(max_square)

""" 
tiles = []
tiles_points = []
for line in input:
    tiles.append((int(line.split(',')[1]), int(line.split(',')[0])))
    tiles_points.append(Point(int(line.split(',')[1]), int(line.split(',')[0])))
    
polygon = Polygon(shell=tiles_points)

#print(polygon.is_closed)
#print(polygon.area)
#print(polygon.exterior)

max_square = 0
for i in range(len(tiles)-1):
    print(i)
    for j in range(i+1, len(tiles)):
        #print(i, j, len(tiles))
        minx = min(tiles[i][0], tiles[j][0])
        maxx = max(tiles[i][0], tiles[j][0])
        miny = min(tiles[i][1], tiles[j][1])
        maxy = max(tiles[i][1], tiles[j][1])
        
        line1 = LineString([Point(minx, miny), Point(minx, maxy)])
        line2 = LineString([Point(minx, maxy), Point(maxx, maxy)])
        line3 = LineString([Point(maxx, maxy), Point(maxx, miny)])
        line4 = LineString([Point(maxx, miny), Point(minx, miny)])
        
        #print('line intersect', polygon.intersection(line1))
        
        contained = True
        contained = contained and ( polygon.contains(line1) or (polygon.intersection(line1) == line1))
        contained = contained and ( polygon.contains(line2) or (polygon.intersection(line2) == line2))
        contained = contained and ( polygon.contains(line3) or (polygon.intersection(line3) == line3))
        contained = contained and ( polygon.contains(line4) or (polygon.intersection(line4) == line4))
        
        if contained:
            #print('here')
            x = abs(tiles[i][0] - tiles[j][0])
            y = abs(tiles[i][1] - tiles[j][1])
            #if x*y > max_square:
                #print(tiles[i], tiles[j])
            max_square = max(max_square, (x+1)*(y+1)) """

#print(max_square) #1569262188

tiles = []
for line in input:
    tiles.append((int(line.split(',')[1]), int(line.split(',')[0])))

boundary = set()
max_square = 0

maximum_x = 0
maximum_y = 0
for t in tiles:
    if t[0] > maximum_x:
        maximum_x = t[0]
    if t[1] > maximum_y:
        maximum_y = t[1]

def check(x, y):
    result = False
    score = 0
    if (x, y) in boundary:
        return True
    for i in range(x, maximum_x+1):
        if (i, y) in boundary:
            #print(i, y)
            score += 1
    if score % 2 == 1:
        result = True
    #print(x, y, score, result)
    
    score = 0
    for i in range(y, maximum_y+1):
        if (x, i) in boundary:
            score += 1
    if score % 2 == 1:
        result = result and True
    #print(x, y, result)

    return result

for i in range(len(tiles)-1):
    print(i)
    for j in range(i+1, len(tiles)):
        #print('current       ', tiles[i], tiles[j])
        if tiles[i][0] == tiles[j][0]:
            for k in range(min(tiles[i][1], tiles[j][1]), max(tiles[i][1], tiles[j][1])+1):
                boundary.add((tiles[i][0], k))
        else:
            for k in range(min(tiles[i][0], tiles[j][0]), max(tiles[i][0], tiles[j][0])+1):
                boundary.add((k, tiles[i][1]))

for i in range(len(tiles)-1):
    print(i)
    for j in range(i+1, len(tiles)):        
        minx = min(tiles[i][0], tiles[j][0])
        maxx = max(tiles[i][0], tiles[j][0])
        miny = min(tiles[i][1], tiles[j][1])
        maxy = max(tiles[i][1], tiles[j][1])
        
        contained = True
        for x in range(minx, maxx+1):
            contained = contained and check(x, miny)
            contained = contained and check(x, maxy)
            if not contained:
                break
        for y in range(miny, maxy+1):
            contained = contained and check(minx, y)
            contained = contained and check(maxx, y)
            if not contained:
                break

        if contained:
            #print(tiles[i], tiles[j])
            x = abs(tiles[i][0] - tiles[j][0])
            y = abs(tiles[i][1] - tiles[j][1])
            max_square = max(max_square, (x+1)*(y+1))
        
print(max_square)
