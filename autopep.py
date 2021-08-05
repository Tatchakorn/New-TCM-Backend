import glob
import os


def check_import():
    try:
        import autopep8
    except ModuleNotFoundError or ImportError:
        print('install autopep8')
        exit(1)


def autopep():
    py_files = glob.iglob('./**/*.py', recursive=True)
    options = '-i -a -a'
    for py_file in py_files:
        os.system(f'autopep8 {options} {py_file}')


if __name__ == '__main__':
    check_import()
    autopep()
