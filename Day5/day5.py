def getData():
    with open('input.txt') as file:
       data = file.read()
    
    lines = [x.split('->') for x in data.split('\n') if x != '']

    result = []
    for line in lines:
        p1 = tuple([int(c) for c in line[0].split(',')])
        p2 = tuple([int(c) for c in line[1].split(',')])
        result.append((p1, p2))

    return result

def part1():
    data = getData()
    covered_points = {}
    
    for points in data:
        x1 = points[0][0]
        x2 = points[1][0]
        y1 = points[0][1]
        y2 = points[1][1]

        if x1 == x2:
            if y1 > y2:
                inc = y2
                while inc <= y1:
                    point = (x1, inc)
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1

            elif y2 > y1:
                inc = y1
                while inc <= y2:
                    point = (x1, inc)
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1

        elif y1 == y2: 
            if x1 > x2:
                inc = x2
                while inc <= x1:
                    point = (inc, y1)
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1

            elif x2 > x1:
                inc = x1
                while inc <= x2:
                    point = (inc, y1)
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1

        else:
            slope = (y2 - y1) / (x2 - x1)
            b = y1 - (slope * x1)

            if x2 > x1:
                inc = x1
                while inc <= x2:
                    point = (inc, int(abs((slope * inc) + b)))
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1
            else:
                inc = x2
                while inc <= x1:
                    point = (inc, int(abs((slope * inc) + b)))
                    if point in covered_points:
                        covered_points[point] += 1
                    else:
                        covered_points[point] = 1
                    inc += 1

    overlaps = 0
    for val in covered_points.values():
        if val >= 2:
            overlaps += 1
    print(overlaps)

if __name__ == "__main__":
    part1()
