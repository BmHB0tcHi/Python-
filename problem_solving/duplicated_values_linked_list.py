'''
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
    Return the linked list sorted as well.
'''
def deleteDuplicates(head):
    try:
        if head.next == None:
            return head
    except AttributeError:
        return head
            
    head_node = head
    while (head.next != None):
        if head.val == head.next.val:
            next_node = head.next
            next_next_node = next_node.next
            # drop the duplicated node
            head.next = next_next_node
            next_node.next = None
        else:
            head = head.next
    return head_node