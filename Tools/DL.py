# coding=utf-8
def singleton(cls,*args,**kw):
    _instances = {}
    def _singleton():
        if cls not in _instances:
            _instances[cls] = cls(*args,**kw)
        return _instances[cls]
    return _singleton