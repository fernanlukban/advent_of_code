size = 10000
path = [[0]*size for i in range(size)]

print("done")

x, y = size//2, size//2

with open("input3.txt", "r") as input_file:
    for num, line in enumerate(input_file):
        num += 1
        current_x, current_y = x, y
        for path in line.split(","):
            direction = path[0]
            length = int(path[1:])
            print(direction, length)
            if direction == "U":
                for i in range(length):
                    path[current_y+i][current_x] += num
                current_y += length
            elif direction == "D":
                for i in range(length):
                    path[current_y-i][current_x] += num
                current_y -= length
            elif direction == "R":
                for i in range(length):
                    path[current_y][current_x+i] += num
                current_x += length
            elif direction == "L":
                for i in range(length):
                    path[current_y][current_x-i] += num
                current_y -= length

for row in path:
    print(row)