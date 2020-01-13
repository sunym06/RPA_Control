import yaml


class ReadYaml(object):
    _yaml = r'../data/Pages.yaml'

    def get_data(self, page, value):
        with open(self._yaml, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        s_locator = content[page][value]
        locator = tuple(s_locator.split(', '))
        return locator


if __name__ == "__main__":
    a = ReadYaml()
    b = a.get_data('LoginPage', '_user')
    print(b)