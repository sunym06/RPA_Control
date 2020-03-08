# import yaml
#
#
# class ReadYaml(object):
# <<<<<<< HEAD
#
#     _par = r'../data/pages.yaml'
#
#     def get_datas(self):
#         with open(self._par, 'r', encoding='utf-8') as f:
#             content = yaml.load(f, Loader=yaml.FullLoader)
#         return content
#
#     def get_location(self, pages, value):
#         with open(self._par, 'r', encoding='utf-8') as f:
#             content = yaml.load(f, Loader=yaml.FullLoader)
#         d = tuple(content[pages][value].split(', '))
#         return d
# =======
#     _yaml = r'../data/Pages.yaml'
#
#     def get_data(self, page, value):
#         with open(self._yaml, 'r', encoding='utf-8') as f:
#             content = yaml.load(f, Loader=yaml.FullLoader)
#         s_locator = content[page][value]
#         locator = tuple(s_locator.split(', '))
#         return locator
# >>>>>>> origin/master
#
#
# if __name__ == "__main__":
#     a = ReadYaml()
# <<<<<<< HEAD
#     e = a.get_data('BaiduPagesss', 'input')
#     print(e)
#     print(type(e))
# =======
#     b = a.get_data('LoginPage', '_user')
#     print(b)
# >>>>>>> origin/master
