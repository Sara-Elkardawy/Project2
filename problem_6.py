class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

#===================================================================================

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = "[ "
        while cur_head:
            out_string += str(cur_head.value)
            cur_head = cur_head.next
            if cur_head:
                out_string += " -> "

        out_string += " ]"
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
#===================================================================================

def union(llist_1, llist_2):
    # Step 1: Convert the linked lists to a Set to handle the duplicates and be ready for the union operation.
    # This step takes O(n1+n2), where n1 is the number of elements in the list1 and n2 is the number of elements in list_2.
    # Hence the adding operation in Sets is O(1), so the overall time in this step = O(n), where n is the total number of elements in both lists.
    AUB = set()
    if llist_1:
        node = llist_1.head
        while node:
            AUB.add(node.value)
            node = node.next
    if llist_2:
        node = llist_2.head
        while node:
            AUB.add(node.value)
            node = node.next


    #Step2: Define a new linked list to return the union result as a linked list
    #Time Complexity for this step is O(n), where n is the number of total elements in the set without any duplicates
    AUB_ll = LinkedList()
    for val in AUB:
        AUB_ll.append(val)
    return AUB_ll
#===================================================================================

def intersection(llist_1, llist_2):
    #Step1: convert both list 1 and list 2 to 2 Sets because Set data structure is the most efficient to handle these kind of operations
    set1 = set()
    if llist_1:
        node = llist_1.head
        while node:
            set1.add(node.value)
            node = node.next

    set2 = set()
    if llist_2:
        node = llist_2.head
        while node:
            set2.add(node.value)
            node = node.next

# Step2: do the intersection by iterating over the first set and checks if the number exists in the other set.
#     The time complexity in this step is O(n), where n is the length of the list 1, since the search in set 2 takes O(1).
    result = set()
    for val1 in set1:
        if val1 in set2:
            result.add(val1)

    #Step3: Define a new linked list to return the intersection result as a linked list
    #Time Complexity for this step is O(n), where n is the number of total elements in the set without any duplicates
    AB_ll = LinkedList()
    for val in result:
        AB_ll.append(val)
    return AB_ll



#===================================================================================

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)
print("\n************************ < Test case 1 > ************************")
print(f"The First List: {linked_list_1} \nThe second List: {linked_list_2}")
print ("Union: {}".format(union(linked_list_1,linked_list_2)))
print ("Intersection: {}".format(intersection(linked_list_1,linked_list_2)))
print("*****************************************************************")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print("\n************************ < Test case 2 > ************************")
print(f"The First List: {linked_list_3} \nThe second List: {linked_list_4}")
print ("Union: {}".format(union(linked_list_3,linked_list_4)))
print ("Intersection: {}".format(intersection(linked_list_3,linked_list_4)))
print("*****************************************************************")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = [1,6]
element_2 = [1,1,1,1,1,1]
for i in element_1:
    linked_list_5.append(i)
for i in element_2:
    linked_list_6.append(i)
print("\n************************ < Test case 3 > ************************")
print(f"The First List: {linked_list_5} \nThe second List: {linked_list_6}")
print ("Union: {}".format(union(linked_list_5,linked_list_6)))
print ("Intersection: {}".format(intersection(linked_list_5,linked_list_6)))
print("*****************************************************************")


linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
element_1 = [30,15]
element_2 = []
for i in element_1:
    linked_list_7.append(i)
for i in element_2:
    linked_list_8.append(i)
print("\n************************ < Test case 4 > ************************")
print(f"The First List: {linked_list_7} \nThe second List: {linked_list_8}")
print ("Union: {}".format(union(linked_list_7,linked_list_8)))
print ("Intersection: {}".format(intersection(linked_list_7,linked_list_8)))
print("*****************************************************************")
print("\n")
