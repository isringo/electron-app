# -*- coding: utf-8 -*-

import glob
import subprocess
import os
import sys

# TypeScript コンパイル
def TSC():
    # JS 削除
    for js in glob.glob('src/**/*.js', recursive=True):
        os.remove(js)

    # TS コンパイル
    p = subprocess.run('npm run tsc', shell=True)
    if p.returncode != 0:
        print('ts compile failed!')
        sys.exit(1)

# メイン
def main():
    TSC()

    # メイン起動
    subprocess.run('start cmd /c npm run start', shell=True)

if __name__ == '__main__':
    main()
