from copy import copy

intcode = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,2,9,19,23,1,9,23,27,2,27,9,31,1,31,5,35,2,35,9,39,1,39,10,43,2,43,day_13,47,1,47,6,51,2,51,10,55,1,9,55,59,2,6,59,63,1,63,6,67,1,67,10,71,1,71,10,75,2,9,75,79,1,5,79,83,2,9,83,87,1,87,9,91,2,91,day_13,95,1,95,9,99,1,99,6,103,2,103,6,107,1,107,5,111,1,day_13,111,115,2,115,6,119,1,119,5,123,1,2,123,127,1,6,127,0,99,2,14,0,0"
reset = list(map(int, intcode.split(",")))
intcode = list(map(int, intcode.split(",")))
print(intcode)


# intcode[1] = 12
# intcode[2] = 2

def compute(intcd):
    for i in range(0, len(intcd), 4):
        if intcd[i] == 99:
            break
        elif intcd[i] == 1:
            pos1, pos2, where = intcd[i + 1:i + 4]
            intcd[where] = intcd[pos1] + intcd[pos2]

        elif intcd[i] == 2:
            pos1, pos2, where = intcd[i + 1:i + 4]
            intcd[where] = intcd[pos1] * intcd[pos2]


def machine(intcode):
    for i1 in range(100):
        for i2 in range(100):
            intcode[1] = i1
            intcode[2] = i2
            compute(intcode)
            print(intcode[0])
            if intcode[0] == 19690720:
                print(intcode)
                return 100 * intcode[1] + intcode[2]
            intcode = copy(reset)
        intcode = copy(reset)


print(machine(intcode))
