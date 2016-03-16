import fileinput

f = open("H:\\list.txt", "r")

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')

# 输入输出，EOF:End Of File
