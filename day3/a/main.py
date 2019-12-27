from shapely.geometry import LineString

with open('input.txt') as input_file:
    inputs = input_file.readlines()

# testing, should equal 159
inputs = ['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']

wires = [w.split(",") for w in inputs]
wires = [[i.strip() for i in w] for w in wires]

def get_next_point(current_point, instruction):
    direction = instruction[0]
    length = int(instruction[1:])

    if direction == 'U': change = (0,length)
    if direction == 'D': change = (0,-length)
    if direction == 'R': change = (length, 0)
    if direction == 'L': change = (-length, 0)

    return tuple([sum(x) for x in zip(current_point,change)])

wire_1 = []
current_point = (0,0)
for instruction in wires[0]:
    next_point = get_next_point(current_point, instruction)
    wire_1.append((current_point, next_point))
    current_point = next_point

wire_2 = []
for instruction in wires[1]:
    next_point = get_next_point(current_point, instruction)
    wire_2.append((current_point, next_point))
    current_point = next_point

def cross(w1, w2):


for w1 in wire_1:
    for w2 in wire_2:
        crossover = cross(w1, w2)
        if (crossover is not None):
            print(crossover)
