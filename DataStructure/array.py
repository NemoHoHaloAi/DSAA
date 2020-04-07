import sys,random

class Array(object):
    _list = None

    def __init__(self,data=None):
        if data:
            self._list = data
        else:
            self._list = []

    def append(self,val):
        self._list.append(val)

    def insert(self,val,idx):
        self._list.insert(idx,val)

    def pop(self):
        return self._list.pop()

    def remove_by_val(self,val):
        idx = self._list.index(val)
        del self._list[idx]
        return idx

    def remove_by_idx(self,idx):
        tmp = self._list[idx]
        del self._list[idx]
        return tmp

    def print(self):
        print(self._list)

if __name__ == "__main__":
    array = Array()
    array.append(0)
    array.append(1)
    array.append(2)
    array.insert(5,1)
    array.insert(6,3)
    array.print()
    print(array.pop())
    array.print()
    array.remove_by_val(1)
    array.remove_by_idx(0)
    array.print()
    
