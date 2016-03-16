import os
import time

source = [r'H:\ceshi.txt', r'H:\测试2.txt']

target_dir = r'H:\BackUps'

# os.sep : 系统的目录分隔符，wimdows默认是'\\',print结果是\
target = target_dir + os.sep + time.strftime('%Y%m%d_%H%M') + '.zip'
# -t:设置文件类型为zip；-r：递归子目录
zip_command = 'HaoZipC a -tzip {0} {1} -r'.format(target, ' '.join(source))
print(zip_command)

if os.system(zip_command) == 0:
    print('Successful back to', target)
else:
    print("Failed")
