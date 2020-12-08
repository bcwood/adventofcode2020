with open("8/input.txt", "r") as file:
    data = file.read().split('\n')

changed = []
has_changed = False
executed = []
accumulator = 0
i = 0

while i < len(data):
    # reset if we execute an instruction again, that means we changed the wrong jmp/nop
    if i in executed:
        has_changed = False
        executed = []
        accumulator = 0
        i = 0

    parts = data[i].split(" ")
    instruction = parts[0]
    value = int(parts[1])

    executed.append(i)

    # change one jmp/nop instruction per try
    if (instruction == "jmp" or instruction == "nop") and has_changed == False and not i in changed:
        changed.append(i)
        has_changed = True
        if instruction == "jmp":
            instruction = "nop"
        else:
            instruction = "jmp"

    # execute instruction
    if instruction == "acc":
        accumulator += value

    if instruction == "jmp":
        i += value
    else:
        i += 1

print(accumulator)
