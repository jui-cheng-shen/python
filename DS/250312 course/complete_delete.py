class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_begin_node(head):
    if head is None:
        return None
    del_node = head
    head = head.next
    del del_node
    return head

def delete_given_pos(head,pos):
    temp = head
    prev = None
    if temp is None or pos <=0:
        return head
    if pos == 1:
        head = temp.next
        return head
    for i in range( 1,pos):
        prev = temp
        temp = temp.next
        if temp is None:
            print("位置超出範圍")
            return head
    if temp is not None:
        prev.next = temp.next
        temp = None
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}",end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    # make begining linked list 22 -> 33 -> 44 -> 55
    head = Node(22)
    head.next = Node(33)
    head.next.next = Node(44)
    head.next.next.next = Node(55)

    print("原始鏈結串列：")
    print_list

    # delete begining node
    head = delete_begin_node(head)
    print("刪除最前面後：")
    print_list(head)

    #delet given position
    head = delete_given_pos(head,3)
    print("刪除第三個節點後：")
    print_list(head)

'''
output:
原始鏈結串列：
22 -> 33 -> 44 -> 55 -> None
刪除開頭節點後：
33 -> 44 -> 55 -> None
刪除第 3 個節點後：
33 -> 44 -> None
'''
