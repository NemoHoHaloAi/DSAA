import sys,random

class Stack(object):
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
        tmp = self._list[-1]
        del self._list[-1]
        return tmp

    def length(self):
        return len(self._list)

    def print(self):
        print('Stack top:')
        for item in self._list[::-1]:
            print(item)
        print('Stack bottom:')

    @staticmethod
    def check(in_list,out_list):
        '''
        检查一个出栈序列与一个入栈序列的顺序是否匹配
        in_list: list
        out_list: list
        return: bool
        '''
        print('in', in_list)
        print('out', out_list)
        for out_i in range(len(out_list)):
            out_item = out_list[out_i]
            print('\tout_item', out_item)
            out_idxs = []
            from_idx = 0
            for c in range(in_list.count(out_item)): # 统计出栈序列的第一个元素在入栈序列中的出现次数
                out_idxs.append(in_list[from_idx:].index(out_item))
                from_idx = out_idxs[-1]+1
            print('\tout_idxs', out_idxs)


if __name__ == '__main__':
    stack = Stack([1,2,3])
    stack.print()
    print(stack.pop())
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.length())
    stack.print()
    Stack.check([1,2,3],[3,2,1])
