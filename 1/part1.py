file = open("1/input.txt", "r")
lines = file.readlines()

for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        val1 = int(lines[i])
        val2 = int(lines[j])
        if (val1 + val2 == 2020):
            print(val1 * val2)
            quit()
