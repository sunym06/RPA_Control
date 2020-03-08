import yaml


class ReadYaml(object):

    _par = r'../data/pages.yaml'

    def get_datas(self):
        with open(self._par, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        return content

    def get_location(self, pages, value):
        with open(self._par, 'r', encoding='utf-8') as f:
            content = yaml.load(f, Loader=yaml.FullLoader)
        d = tuple(content[pages][value].split(', '))
        return d


if __name__ == "__main__":
    a = ReadYaml()
    e = a.get_data('BaiduPagesss', 'input')
    print(e)
    print(type(e))
