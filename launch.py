# -*- coding: utf-8 -*-

import glob
import subprocess
import os
import sys

optTsc = 0b0001
optStart = 0b0010
optSass = 0b0100

# CSS 作成


def SassC():
    print("--------- SassC ---------")

    # css 削除
    for css in glob.glob('src/**/*.css', recursive=True):
        os.remove(css)

    # scss コンパイル
    for scss in glob.glob('src/**/[a-zA-Z]*.scss', recursive=True):
        css = os.path.splitext(scss)[0] + '.css'

        cmd = 'npm run sassc ' + scss + ' ' + css
        subprocess.run(cmd, shell=True)

        assert os.path.exists(css), '[FAILD] build css: ' + cmd

# TypeScript コンパイル


def TSC():
    print("--------- TSC ---------")

    # JS 削除
    for js in glob.glob('src/**/*.js', recursive=True):
        os.remove(js)

    # TS コンパイル
    p = subprocess.run('npm run tsc', shell=True)
    if p.returncode != 0:
        print('ts compile failed!')
        sys.exit(1)

# メイン


def main(mask):
    if mask & optTsc:
        TSC()

    # メイン起動
    if mask & optStart:
        print("--------- Start ---------")
        subprocess.run('start cmd /c npm run start', shell=True)

    if mask & optSass:
        SassC()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        main(~0b0000)
    else:
        mask = 0b0000
        for arg in sys.argv:
            a = arg.lower()
            if a == "tsc":
                mask |= optTsc
            elif a == "start":
                mask |= optStart
            elif a == "sass":
                mask |= optSass
        main(mask)
