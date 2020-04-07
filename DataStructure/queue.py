import sys,random

class Queue(object):
    _list = None

    def __init__(self,data=None):
        if data:
            self._list = data
        else:
            self._list = []

    def push(self,val):
        self._list.append(val)

    def pop(self):
        if len(self._list)<=0:
            return None
        tmp = self._list[0]
        del self._list[0]
        return tmp

    def length(self):
        return len(self._list)

    def print(self):
        print('Queue head:')
        for item in self._list:
            print(item)
        print('Queue tail:')


if __name__ == '__main__':
    queue = Queue([1,2,3])
    queue.print()
    print(queue.pop())
    queue.push(4)
    queue.push(5)
    queue.push(6)
    print(queue.length())
    queue.print()
