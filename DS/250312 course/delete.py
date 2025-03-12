class Node:
    def delete_begging(head):
        if head is None:
            return None
        del_node = head
        head = head.next #更新head 為下一個節點
        return head

    #ex: before:22 ->33 ->44 ->55 ; run head = delete_begin_node(head) ; result: 33 ->44 ->55
    #time_complexity: O(1) ; 只需更新head 為下一個節點

    def delete_given_pos(head,pos):
        temp = head # 遍歷鏈結串列
        prev = None # 記錄前一個節點
        if temp is None or pos <=0:
            return head
        if pos == 1:
            head = temp.next
            return head
        for i in range(1,pos):
            prev = temp
            temp = temp.next
            if temp is None:
                print("位置超出範圍")
                return head
        if temp is not None: #找到要刪除的節點
            prev.next = temp.next #跳過要刪除的節點
            temp = None
        return head

    #ex : before:22 ->33 ->44 ->55 ; run head = delete_given_pos(head,3) ; result: 22->33->55
    #time_complexity: O(n) ; 需遍歷到目標節點