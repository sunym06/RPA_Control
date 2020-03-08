import json

import yaml


class ReadParams(object):

    def read_yaml(self, file, a , b):
        y = yaml.load(open(file, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        s = y[a][b]
        return s


if __name__ == '__main__':
    yaml_path = r'E:\workspaces\RPA_Control\api\common\config.yaml'
    a = ReadParams()
    r = a.read_yaml(yaml_path, 'Model', 'debug')
    print(r)
    print(type(r))





