class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def insert_at_beginning(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    return new_node

def insert_at_end(head, new_data):
    new_node = Node(new_data)
    if head is None:
        return new_node
    last = head
    while last.next:
        last = last.next
    last.next = new_node
    return head

def insert_before_given(head, given, new_data):
    if head is None:
        return None
    if head.data == given:
        new_node = Node(new_data)
        new_node.next = head
        return new_node
    prev = None
    curr = head
    while curr is not None and curr.data != given:
        prev = curr
        curr = curr.next
    if curr is not None:
        new_node = Node(new_data)
        new_node.next = curr
        prev.next = new_node
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(f"{curr.data}", end=" -> ")
        curr = curr.next
    print("None")


if __name__ == "__main__":
    # 建立初始鏈結串列 22 -> 33 -> 44 -> 55
    head = Node(22)
    head.next = Node(33)
    head.next.next = Node(44)
    head.next.next.next = Node(55)

    print("原始鏈結串列：")
    print_list(head)

    # 插入到最前面
    head = insert_at_beginning(head, 11)
    print("插入 11 到最前面後：")
    print_list(head)

    # 插入到最後面
    head = insert_at_end(head, 66)
    print("插入 66 到最後面後：")
    print_list(head)

    # 插入到 44 之前
    head = insert_before_given(head, 44, 99)
    print("插入 99 到 44 之前後：")
    print_list(head)