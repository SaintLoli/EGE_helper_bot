import requests


class Parser:
    URL = 'http://os.fipi.ru/home/1'

    def get_subject_list(self):
        data = requests.get('http://os.fipi.ru/api/dictionaries').json()
        return '\n'.join(['--> ' + sub['name'] for sub in data['subjects'] if int(sub['id']) <= 22])


if __name__ == '__main__':
    parse = Parser()
    print(parse.get_subject_list())