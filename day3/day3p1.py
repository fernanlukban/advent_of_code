class LineSegment:
    def __init__(self, start, end, is_horizontal = True):
        self.start = start
        self.end = end
        self.is_horizontal = is_horizontal

    def __str__(self):
        return f"{self.start} {self.end} {self.is_horizontal}"

    __repr__ = __str__

x, y = 0, 0

lines = []

with open("input3.txt", "r") as input_file:
    for line in input_file:
        lines.append([])
        current_x, current_y = x, y
        for path in line.split(","):
            direction = path[0]
            length = int(path[1:])
            if direction == "U":
                lines[-1].append(LineSegment(current_y, current_y + length, False))
                current_y += length
            elif direction == "D":
                lines[-1].append(LineSegment(current_y, current_y - length, False))
                current_y -= length
            elif direction == "R":
                lines[-1].append(LineSegment(current_x, current_x + length))
                current_x += length
            elif direction == "L":
                lines[-1].append(LineSegment(current_x, current_x - length))
                current_y -= length

for line in lines:
    print(line)