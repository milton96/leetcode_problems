class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_tail(head: ListNode, val: int) -> ListNode:
    if not head:
        return ListNode(val)
    aux = head
    while aux.next:
        aux = aux.next

    aux.next = ListNode(val)
    return head
    
def imprimir(node: ListNode) -> None:
    while node:
        print(node.val, end=", ")
        node = node.next

def reverse(head: ListNode) -> ListNode:
    curr = head
    prev = None

    while curr:
        aux = curr.next
        curr.next = prev
        prev = curr
        curr = aux

    return prev
