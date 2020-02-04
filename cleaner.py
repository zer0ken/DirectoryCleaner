from os import listdir, rmdir
from os.path import isdir


class Cleaner():
    def __init__(self):
        self.found = []

    def start(self):
        path = input('청소할 위치를 입력하세요.\n>>> ')
        print('\n빈 폴더를 찾고 있습니다...')
        self.find(path)
        print('검사가 끝났습니다.\n\n<삭제될 폴더>')
        print('\n'.join(self.found))
        if not self.found:
            print('삭제할 폴더가 없습니다.')
            return
        while True:
            check = input('\n빈 폴더를 삭제할까요? (y/n)\n>>> ')
            if check.strip() in 'yY':
                print('\n빈 폴더를 삭제합니다...')
                self.clean()
                print('\n삭제가 완료되었습니다.')
            elif check.strip() in 'nN':
                print('\n삭제가 취소되었습니다.')
            else:
                continue
            break

    def find(self, path):
        if not isdir(path):
            return
        for d in listdir(path):
            self.find(f'{path}\\{d}')
        if self.is_empty(path):
            self.found.append(path)

    def is_empty(self, path):
        dirs = listdir(path)
        for d in self.found:
            try:
                dirs.remove(d.split('\\')[-1])
            except ValueError:
                pass
        return not dirs

    def clean(self):
        for d in self.found:
            rmdir(d)
            print('삭제됨: ' + d)


Cleaner().start()
