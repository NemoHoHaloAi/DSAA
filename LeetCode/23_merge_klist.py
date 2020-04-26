#合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
#示例:
#
#输入:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#输出: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def answer1(self, lists):
        '''
        解题思路：暴力法

        不出意外的超时了；
        '''
        new_root = ListNode(-999)
        point = new_root
        while sum([1 if _list else 0 for _list in lists]) > 0:
            print('sum', sum([1 if _list else 0 for _list in lists]) > 0)
            min_val = None
            min_idx = -1
            for i in range(len(lists)):
                _list = lists[i]
                if _list and (((min_val is None)) or (_list.val < min_val)):
                    min_val = _list.val
                    min_idx = i
                    print('if', min_idx, min_val)
            # tmp = ListNode(min_val)
            # if not new_root:
            #     new_root = tmp
            # else:
            #     new_root.next = tmp
            point.next = ListNode(min_val)
            point = point.next
            lists[min_idx] = lists[min_idx].next
        return new_root.next

    def merge(self, list_):
        '''
        归并排序的递归实现
        思路：将数据划分到每两个为一组为止，将这两个排序后范围，2个包含2个元素的组继续排序为1个4个元素的组，
        直到回溯到整个序列，此时其实是由两个有序子序列组成的，典型的递归问题
        '''
        if len(list_)<=1:
            return list_
        if len(list_)==2:
            return list_ if list_[0]<=list_[1] else list_[::-1]
        len_ = len(list_)
        left = self.merge(list_[:int(len_/2)])
        right = self.merge(list_[int(len_/2):])
        tmp = []
        left_idx,right_idx = 0,0
        while len(tmp)<len(list_):
            if left[left_idx]<=right[right_idx]:
                tmp.append(left[left_idx])
                left_idx+=1
                if left_idx==len(left):
                    tmp += right[right_idx:]
                    break
            else:
                tmp.append(right[right_idx])
                right_idx+=1
                if right_idx==len(right):
                    tmp += left[left_idx:]
                    break
        return tmp 

    def answer2(self, lists):
        '''
        解题思路：N路归并排序，利用归并排序的思路实现，归并排序复杂度为O(n log n)，要优于暴力法
        '''
        lists_ = []
        for list_ in lists:
            while list_:
                lists_.append(list_.val)
                list_ = list_.next
        lists_ = self.merge(lists_)
        root = ListNode(lists_[0])
        tmp = root
        for node in lists_[1:]:
            tmp.next = ListNode(node)
            tmp = tmp.next
        return root


    def mergeKLists(self, lists):
        '''
        题目链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
        '''
        return self.answer2(lists)

root1 = ListNode(1)
tmp = ListNode(4)
root1.next = tmp
tmp.next = ListNode(5)

root2 = ListNode(1)
tmp = ListNode(3)
root2.next = tmp
tmp.next = ListNode(4)

root3 = ListNode(2)
tmp = ListNode(6)
root3.next = tmp

root4 = ListNode(0)
root5 = ListNode(1)

answer = Solution().mergeKLists([root1,root2,root3])
print('-----------------------')
while answer:
    print(str(answer.val)+'\t')
    answer = answer.next

answer = Solution().mergeKLists([root4,root5])
print('-----------------------')
while answer:
    print(str(answer.val)+'\t')
    answer = answer.next

answer = Solution().mergeKLists([root5,root4])
print('-----------------------')
while answer:
    print(str(answer.val)+'\t')
    answer = answer.next