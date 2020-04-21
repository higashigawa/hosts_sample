import os
import glob
from time import sleep

def main():
    os.chdir(r'C:\windows\system32\drivers\etc')
    fdata_files = glob.glob('hosts')

    for file_name in fdata_files:
        fa = open('hosts', 'a').write('\n172.28.***.***    servername')

    print('hostsファイルに追記しました。')
    sleep(3)

if __name__ == '__main__':
    main()
