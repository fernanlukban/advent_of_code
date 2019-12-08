class LineSegment:
    def __init__(self, place, start, end, is_horizontal = True):
        self.place = place
        self.start = start
        self.end = end
        self.is_horizontal = is_horizontal

    def __str__(self):
        return f"{self.start} {self.end} {self.is_horizontal} {self.place}"

    __repr__ = __str__

x, y = 0, 0

lines = []

VERTICAL = 0
HORIZONTAL = 1

closest_x, closest_y = None, None

intersections = []  

with open("input3_v2.txt", "r") as input_file:
    for num, line in enumerate(input_file):
        lines.append([dict() , dict()])
        current_x, current_y = x, y
        for path in line.split(","):
            direction = path[0]
            length = int(path[1:])
            if direction == "U":
                segment = LineSegment(current_x, current_y, current_y + length, False)
                lines[num][VERTICAL][current_x] = segment
                current_y += length
            elif direction == "D":
                segment = LineSegment(current_x, current_y, current_y - length, False)
                lines[num][VERTICAL][current_x] = segment
                current_y -= length
            elif direction == "R":
                segment = LineSegment(current_y, current_x, current_x + length)
                lines[num][HORIZONTAL][current_y] = segment
                current_x += length
            elif direction == "L":
                segment = LineSegment(current_y, current_x, current_x - length)
                lines[num][HORIZONTAL][current_y] = segment
                current_y -= length

            if num == 1:
                print("SEGMENT")
                print(segment)
                for i in range(segment.start, segment.end + 1):
                    print(lines[0][not segment.is_horizontal])
                    if lines[0][not segment.is_horizontal].get(i, 0) != 0:
                        intersecting_segment = lines[0][not segment.is_horizontal][i]
                        print("INTERSECTING_SEGMENT", intersecting_segment)
                        if not intersecting_segment.is_horizontal:
                            new_x = segment.place
                            new_y = intersecting_segment.place
                        else:
                            new_x = intersecting_segment.place
                            new_y = segment.place
                        print(new_x, new_y, closest_x, closest_y)
                        if closest_x == None or (abs(new_y) + abs(new_x)) < (abs(closest_x) + abs(closest_y)):
                            closest_x, closest_y = new_x, new_y
                            print(closest_x, closest_y)
                        intersections.append((new_x, new_y))
print(intersections)
# for line in lines:
#     print(line)