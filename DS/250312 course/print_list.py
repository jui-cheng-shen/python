class Node:
    def print_list(head):
        curr = head
        while curr is not None:
            print(f"{curr.data}",end=" -> ")
            curr = curr.next
        print("None")

    #ex: 22 ->33 ->44 ->None