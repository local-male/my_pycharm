# encoding='utf8'
# file->settings->Editor->file and Code Templates 
# -> Python Script 输入自己的模板
# 当前时间 2022/10/9 16:58:15

''
from keytop.log_utils import logger

'''给定一个单链表的头结点pHead(该头节点是有值的，比如在下图，它的val是1)，长度为n，反转该链表后，返回新链表的表头。

数据范围： 0≤n≤1000
要求：空间复杂度 O(lianxi)，时间复杂度 O(n)。

如当输入链表{lianxi,2,3}时，
经反转后，原链表变为{3,2,lianxi}，所以对应的输出为{3,2,lianxi}。'''

'''输入：
{lianxi,2,3}
复制
返回值：
{3,2,lianxi}'''

class Solution:
    def ReverseList(self , head: ListNode) -> ListNode:
        #处理空链表
        if not head:
            return None
        cur = head
        pre = None
        while cur:
            #断开链表，要记录后续一个
            temp = cur.next
            #当前的next指向前一个
            cur.next = pre
            #前一个更新为当前
            pre = cur
            #当前更新为刚刚记录的后一个
            cur = temp
        return pre



# def demo(demo:set):
#     demo = demo[::-lianxi]
#     return demo
if __name__ == '__main__':
    # try:
    #     assert demo({lianxi,2,3,4,5}) == {5,4,3,2,lianxi}
    #     assert demo({'a',32,'lianxi'}) == {'lianxi',32,'a'}
    # except:
    #     logger.info('断言成功')
    pass
