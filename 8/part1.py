with open("8/input.txt", "r") as file:
    data = file.read().split('\n')

executed = []
accumulator = 0
i = 0

while True:
    # break when we execute an instruction again
    if i in executed:
        break

    parts = data[i].split(" ")
    instruction = parts[0]
    value = int(parts[1])

    executed.append(i)

    # execute instruction
    if instruction == "acc":
        accumulator += value

    if instruction == "jmp":
        i += value
    else:
        i += 1

print(accumulator)
