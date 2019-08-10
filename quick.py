


image_file = open("image_file.txt", "r+")

for line in image_file.readlines():
    l_name = line[:line.find("=") - 1]
    array_text = line[line.find("=") + 3:-2]

    joined_array = [int(x) for x in array_text.split(',')]

    matrix = []
    black = [0, 0, 0]

    for i in range(16):
        matrix.append([])
    for j in range(16):
        for rep in range(16):
            matrix[j].append(black)

    if len(joined_array) == 16 * 16 * 3:
        for i in range(16):
            for j in range(16):
                if i % 2 == 1:
                    r = 15 - j
                else:
                    r = j
                p = []
                for c in range(3):
                    p.append(joined_array[i * 16 * 3 + r * 3 + c])
                matrix[i][j] = p


    if l_name != None:
        formatted = l_name + " = " + "["
        for row in range(16):
            for col in range(16):
                for rgb in range(3):
                    formatted += str(matrix[row][col][rgb]) + ","

        formatted = formatted[:-1] + "]\n"
        image_file.write(formatted)
    print(l_name," completed")