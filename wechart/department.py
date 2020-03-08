import jsonpath

from wechart.base import Base
from wechart.common import Common


class Department(Base):
    uid = Common.uid()

    def create(self, name=None, name_en=None, parentid=None, order=None, id=None, dic=None):
        path = 'department/create'
        if dic is None:
            dic = {
                "name": name,
                "name_en": name_en,
                "parentid": parentid,
                "order": order,
                "id": id
            }
        r = self.post_response(path, **dic)
        return r.json()

    def update(self, id=None, name=None, name_en=None, parentid=None, order=None, dic=None):
        path = 'department/update'
        if dic is None:
            dic = {
                "id": id,
                "name": name,
                "name_en": name_en,
                "parentid": parentid,
                "order": order
            }
        self.post_response(path, **dic)

    def delete(self, id=None):
        path = 'department/delete'
        if id is None:
            self.get_response(path, debugs=True)
        if isinstance(id, int):
            dic = {'id': id}
            self.get_response(path, **dic)
        elif isinstance(id, list):
            for i in id:
                self.get_response(path, **{'id': i})

    def list(self, id=True):
        path = 'department/list'
        if id:
            dic = {'id': id}
            r = self.get_response(path, **dic).json()
        else:
            r = self.get_response(path).json()
        return r


if __name__ == "__main__":
    a = Department()
    a.delete()
    # # a.create('t1', 'to11', 1, 1, 2)
    # dic2 = {
    #     "id": 9,
    #     "name": "广州研发中心",
    #     "name_en": "RDGZ",
    #     "parentid": 1,
    #     "order": 1
    # }
    # # a.create(dic=dic2)
    # a.update(dic=dic2)
    # # dic2 = {
    # #    "id": 2,
    # #    "name": "广州研发中心22",
    # # }
    # # a.create(dic)
    # # a.update(dic2)
    # # a.delete(2)
    # # r = a.list(id=False)
    # # l = jsonpath.jsonpath(r, '$..id')
    # # print(l)
    # # for i in range(l):
    # # a.delete(l)