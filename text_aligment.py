thickness = 5

width = thickness * 2 - 1
for i in range(1, thickness*2, 2):
    line = ('H' * i).center(width, ' ')
    print(line)

line = ('H' * thickness).center(width, ' ')
line = line.ljust(4 * thickness, ' ') + line
for i in range(thickness+1):
    print(line)

line_2 = ('H' * (5 * thickness)).center(5 * thickness + 4)
for i in range(thickness-2):
    print(line_2)

for i in range(thickness + 1):
    print(line)

for i in range(thickness * 2 - 1, 0, -2):
    line = (('H' * i).center(width, ' ')).rjust(3* width + 2, ' ')
    print(line)
