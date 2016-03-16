import zipfile
import os
import sys
import time

'''Back up files v0.2'''

source = []

backList = open("H:\\list.txt", "r")
while True:
    line = backList.readline()
    if len(line) == 0:
        break
    source.append(line.replace('\n', ''))
    print(line, end='')

targetDir = r'H:\BackUps'
timeString = time.strftime('%Y%m%d_%H%M')

# 利用'-c'来comment
if len(sys.argv) > 1 and sys.argv[1] == '-c':
    print(sys.argv[1])
    comment = input("Enter a comment：")
    targetZip = targetDir + os.sep + comment.replace(' ', '_') + '.zip'
else:
    targetZip = targetDir + os.sep + timeString.replace(' ', '_') + '.zip'

# 'r'表示打开一个存在的只读ZIP文件；
# 'w'表示清空并打开一个只写的ZIP文件，或创建一个只写的ZIP文件；
# 'a'表示打开一个ZIP文件，并添加内容。
f = zipfile.ZipFile(targetZip, 'w', zipfile.ZIP_DEFLATED)

for file in source:
    # if os.path.isfile(file):
    f.write(file)

print('\nBackup succeed to', targetZip, end='')
f.close()
