class LineSegment:
    def __init__(self, place, start, end, is_horizontal = True):
        self.place = place
        self.start = start
        self.end = end
        self.is_horizontal = is_horizontal

    def __str__(self):
        horizontal_str = "HORIZONTAL" if self.is_horizontal else "VERTICAL"
        return f"{self.start:5} {self.end:5} {horizontal_str:15} {self.place:5}"

    __repr__ = __str__

x, y = 0, 0

lines = []

VERTICAL = 0
HORIZONTAL = 1

closest_x, closest_y = None, None

intersections = []  

with open("input3.txt", "r") as input_file:
    for num, line in enumerate(input_file):
        lines.append([dict() , dict()])
        current_x, current_y = x, y
        for path in line.split(","):
            direction = path[0]
            length = int(path[1:])
            # print(direction, length)
            if direction == "U":
                segment = LineSegment(current_x, current_y, current_y + length, False)
                lines[num][VERTICAL][current_x] = segment
                current_y += length
            elif direction == "D":
                segment = LineSegment(current_x, current_y - length, current_y, False)
                lines[num][VERTICAL][current_x] = segment
                # print("SLKDFJLSDKJF", segment)
                current_y -= length
            elif direction == "R":
                segment = LineSegment(current_y, current_x, current_x + length)
                lines[num][HORIZONTAL][current_y] = segment
                current_x += length
            elif direction == "L":
                segment = LineSegment(current_y, current_x - length, current_x )
                lines[num][HORIZONTAL][current_y] = segment
                current_x -= length

            if num == 1:
                # print("SEGMENT", segment)
                for i in range(segment.start + 1, segment.end):
                    if lines[0][not segment.is_horizontal].get(i, 0) != 0:
                        intersecting_segment = lines[0][not segment.is_horizontal][i]
                        # print("\tPOSSIBLE_SEGMENT", intersecting_segment)
                        # print(intersecting_segment.start, segment.place, intersecting_segment.end)
                        if intersecting_segment.start <= segment.place <= intersecting_segment.end:
                            # print("INTERSECTING_SEGMENT", intersecting_segment)
                            if not intersecting_segment.is_horizontal:
                                new_x = segment.place
                                new_y = intersecting_segment.place
                            else:
                                new_x = intersecting_segment.place
                                new_y = segment.place
                            # print(new_x, new_y, closest_x, closest_y)
                            if closest_x == None or (abs(new_y) + abs(new_x)) < (abs(closest_x) + abs(closest_y)):
                                closest_x, closest_y = new_x, new_y
                                # print(closest_x, closest_y)
                            intersections.append((new_x, new_y))
                # print()
# print(closest_x + closest_y)
print(intersections)
print(min(intersections, key=lambda x: abs(x[0]) + abs(x[1])))
print(abs(closest_x) + abs(closest_y))
# for line in lines:
#     print(line)