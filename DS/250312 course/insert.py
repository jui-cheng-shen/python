class Node:
#insert_at_biginning
    def insert_at_beginning(head,new_data):
        new_node = Node(new_data)
        new_node.next = head
        return new_node #回傳新的節點,new head

    #ex: before: 22 ->33 ->44 ; after add 55: 55 ->22 ->33 ->44

#insert_at_end
    def insert_at_end(head,new_data): #head 是一個節點, new_data 是要插入的資料
        new_node =Node(new_data)
        if head is None:
            return new_node
        last = head #如果head不是空的，找到最後一個節點
        while last.next:
            last = last.next # last.next 是下一個節點
        last.next = new_node #將新節點插入到最後一個節點的後面
        return head

    #ex: before: 22 ->33 ->44 ; after add 55: 22 ->33 ->44 ->55


#insert_Before_Given
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
            prev.next = new_node
            new_node.next = curr
            prev.next = new_node
        return head

    #ex: before: 22 ->33 ->44 ; after add 33 before 11 : 22 ->11 ->33 ->44