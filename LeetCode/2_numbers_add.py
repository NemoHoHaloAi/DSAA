class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        num1 = ''.join(num1[::-1])
        num2 = []
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        num2 = ''.join(num2[::-1])
        count_ = str(int(num1)+int(num2))[::-1]
        root = ListNode(int(count_[0]))
        tmp = root
        count_ = count_[1:]
        while len(count_)>0:
            print(count_[0])
            tmp.next = ListNode(int(count_[0]))
            tmp = tmp.next
            count_ = count_[1:]
        return root

Solution().addTwoNumbers(ListNode(1), ListNode(2))