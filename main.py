import json

jls_extract_var = 'datafile.json'
with open(jls_extract_var, 'r') as f:

    data = json.load(f)


width = data["width"]

height = data["height"]

obstacles = data["obstacles"]

bot = data["bot"]

y_bot = bot[0]

x_bot = bot[1]
coin = data["coin"]

y_coin = coin[0]

x_coin = coin[1]


k = len(data["obstacles"])

obstacles_list = []
i: int

for i in range(k):

    obstacles_list.append(obstacles[i])



def check_eating_coin(xbot, ybot, xcoin, ycoin):

    if xbot == xcoin & ybot == ycoin:

        return True
    else:

        return False



print(check_eating_coin(x_bot, y_bot, x_coin, y_coin))


print(width)

print(height)

for i in range(1, width + 1):

    if i == 1 or i == width:

        for j in range(1, height + 1):

            print("*", end='')
        print()
    else:

        for j in range(1, height + 1):

            if j == 1 or j == height:

                print("*", end='')
            else:

                print(" ", end='')
        print()


path = [[5, 8], [6, 8], [6, 7], [7, 7], [7, 6], [6, 6], [6, 5], [5, 5], [5, 6], [4, 6], [4, 7], [3, 7], [2, 7], [1, 7],

        [1, 6], [1, 5], [2, 5], [3, 5], [4, 5], [4, 4], [4, 3], [3, 3], [2, 3], [2, 4], [1, 4], [1, 3], [1, 4]]

x = path[-1][1] - path[-2][1]

y = path[-1][0] - path[-2][0]

if not (-1 <= x, y <= 1):

    print("ERROR")

R = "Right\n"

L = "Left\n"

U = "Up\n"

D = "Down\n"

if y == 0:

    if x == 1:

        f = open("G:\Tính-HKII\PRTE\OUTPUT_coordinate.txt", "a")

        f.writelines(R)

        f.close()

    elif x == -1:

        f = open("G:\Tính-HKII\PRTE\OUTPUT_coordinate.txt", "a")

        f.writelines(L)

        f.close()

if x == 0:

    if y == 1:

        f = open("G:\Tính-HKII\PRTE\OUTPUT_coordinate.txt", "a")

        f.writelines(D)

        f.close()

    elif y == -1:

        f = open("G:\Tính-HKII\PRTE\OUTPUT_coordinate.txt", "a")

        f.writelines(U)

        f.close()

f = open("G:\Tính-HKII\PRTE\OUTPUT_coordinate.txt", "r")

print(f.read())

