
# Problem 1: LRU Cache
# Least Recently Used Cache
# We have briefly discussed caching as part of a practice problem while studying hash maps.
#
# The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
#
# While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.
#
# When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.
#
# For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.
#
# Your job is to use an appropriate data structure(s) to implement the cache.
#
# In case of a cache hit, your get() operation should return the appropriate value.
# In case of a cache miss, your get() should return -1.
# While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
# All operations must take O(1) time.
#
# For the current problem, you can consider the size of cache = 5.
#
# Here is some boiler plate code and some example test cases to get you started on this problem:

class DoubleLinkedNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_key(self):
        return self.key

    def __str__(self):
        return "("+str(self.key)+","+str(self.value)+")"

    def __repr__(self):
        return "("+str(self.key)+","+str(self.value)+")"

#===================================================================================
class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, new_node):
        new_node.prev = None
        new_node.next = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        return self.head

    def move_to_front (self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.prev
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next=node.next
        if next_node:
            next_node.prev=prev_node
        return self.insert(node)

    def remove_tail(self):
        removed_key = self.tail.key
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return removed_key
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return removed_key

    def display(self):
        #Node current will point to head
        current = self.head
        if(self.head == None):
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while(current != None):
            #Prints each node by incrementing pointer.
            print(current),
            current = current.next
#===================================================================================

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.dict = dict()
        self.doubleList = DoubleLinkedList()
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key is None or key == "":
            print(f"Invalid key !!")
            return -1
        elif self.dict.get(key) is None:
            return -1
        else:
            node = self.dict[key]
            self.doubleList.move_to_front(node)
            return node.get_value()
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity <= 0:
            print(f"Can't insert, cache capacity <{self.capacity}> !!")
            return
        elif key is None or key == "":
            print(f"Invalid key !!")
            return
        elif value is None or value == "":
            print(f"Invalid value !!")
            return
        elif self.dict.get(key) is None:
            if len(self.dict) == self.capacity:
                removed_key = self.doubleList.remove_tail()
                #print(f"removed_key = {removed_key}")
                del self.dict[removed_key]
            self.dict[key] = self.doubleList.insert(DoubleLinkedNode(key,value))
        else:
            node = self.dict[key]
            node.set_value(value)
            self.doubleList.move_to_front(node)

        pass

    def display_cache(self):
        #print("=========================================================")
        print("** The Hashmap::")
        print(self.dict)
        self.doubleList.display()
        print("")
#===================================================================================
if __name__ == "__main__":
    print("\n")

    print("********************* < Test case 1: Cache Size = 5 > *********************")
    our_cache = LRU_Cache(5)
    print("#Step1: Insert the values (1,1), (2,2), (3,3), (4,4):")
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    our_cache.display_cache()
    print("#Step2: Read the values (1,1) then (2,2) then (9,9) respectively:")
    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))     # returns -1 because 9 is not present in the cache
    our_cache.display_cache()
    print("#Step3: Insert the values (5, 5), (6, 6) :")
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    our_cache.display_cache()
    print("#Step4: Read the value (3) :")
    print(our_cache.get(3))     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
    our_cache.display_cache()
    print("\n")

    print("********************* < Test case 2: Cache Size = 0 > *********************")
    our_cache2 = LRU_Cache(0)
    print("#Step1: Insert the values (8,8), (12,12):")
    our_cache2.set(8, 8)
    our_cache2.set(12, 12)
    our_cache2.display_cache()
    print("#Step2: Read the values (8,8), (12,12) respectively:")
    print(our_cache2.get(8))
    print(our_cache2.get(12))
    our_cache2.display_cache()

    print("\n")
    print("********************* < Test case 3: Cache Size = -1 > *********************")
    our_cache3 = LRU_Cache(-1)
    print("#Step1: Insert the values ('a', 'A'):")
    our_cache3.set('a', 'A')
    our_cache3.display_cache()
    print("#Step2: Read the value ('a', 'A')")
    print(our_cache3.get('a'))

    print("\n")
    print("********************* < Test case 4: Cache Size = 3 > *********************")
    our_cache4 = LRU_Cache(3)
    print("#Step1: Insert the values ('a', 'A'), ('b', 'B'), ('c', 'C'):")
    our_cache4.set('a', 'A')
    our_cache4.set('b', 'B')
    our_cache4.set('c', 'C')
    our_cache4.display_cache()
    print("#Step2: Insert the values ('d', 'D')")
    our_cache4.set('d', 'D')
    our_cache4.display_cache()
    print("#Step3: Read the values ('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D') respectively:")
    print(our_cache4.get('a'))
    print(our_cache4.get('b'))
    print(our_cache4.get('c'))
    print(our_cache4.get('d'))
    our_cache4.display_cache()
    print("#Step4: Read the value  ('b', 'B') Then insert ('e','E'):")
    print(our_cache4.get('b'))
    our_cache4.set('e', 'E')
    our_cache4.display_cache()
    print("#Step5: Insert a null key:")
    our_cache4.set(None, 'F')
    our_cache4.display_cache()
    print("#Step6: Insert an empty key:")
    our_cache4.set(None, 'G')
    our_cache4.display_cache()
    print("#Step7: Insert a null value:")
    our_cache4.set('h', None)
    our_cache4.display_cache()
    print("#Step8: Insert an empty value:")
    our_cache4.set('i', "")
    our_cache4.display_cache()
    print("#Step9: get a None key:")
    print(our_cache4.get(None))
    print("#Step10: get an empty key:")
    print(our_cache4.get(''))
    our_cache4.display_cache()

    print("\n")
    print("********************* < Test case 5: Cache Size = 1 > *********************")
    our_cache5 = LRU_Cache(1)
    print("#Step1: Insert the values (1,1), (2,2), (3,3), (4,4):")
    our_cache5.set(1, 1)
    our_cache5.set(2, 2)
    our_cache5.set(3, 3)
    our_cache5.set(4, 4)
    our_cache5.display_cache()
    print("#Step2: Read the values (1,1) then (2,2) then (3,3) then (4,4) respectively:")
    print(our_cache5.get(1))       # returns -1
    print(our_cache5.get(2))       # returns -1
    print(our_cache5.get(3))     # returns -1
    print(our_cache5.get(4))     # returns 4
    our_cache5.display_cache()
    print("#Step3: Insert the values (5, 5), (6, 6) :")
    our_cache5.set(5, 5)
    our_cache5.set(6, 6)
    our_cache5.display_cache()
    print("#Step4: Read the value (5), (6):")
    print(our_cache5.get(5))     # returns -1
    print(our_cache5.get(6))
    our_cache5.display_cache()
    print("\n")
