import zipfile
import os
import sys
import time

'''Back up files v0.2'''

source = [r'H:\ceshi.txt', r'H:\ceshi2.txt']
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
    f.write(file)

print('Backup succeed to', targetZip)

f.close()
