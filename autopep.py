import glob
import os
import autopep8


def autopep() -> None:
    py_files = glob.iglob('./**/*.py', recursive=True)
    options = '-i -a -a'
    for py_file in py_files:
        os.system(f'python -m autopep8 {options} {py_file}')


if __name__ == '__main__':
    autopep()
