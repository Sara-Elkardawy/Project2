Problem 1: LRU Cache (Least Recently Used Cache) analysis:
**************************************************************************************************************

Design Decisions:

The data structures used are:
1) Python’s dictionary (hash map): stores the keys and the values. The values are Double linked list nodes.
The choice of dictionary is to maintain O(1) in both the insertion and deletion operations.
2) Double Linked list: stores the tuple (key, value) and 2 pointers for previous node and next node to make moving and deleting operations in O(1) because we should not traverse the whole list each time we move a node to the front.

Time complexity:

[1] GET operation:
	First it checks if the key exists in the hash map, if not return -1. Otherwise retrieve the value from the hash map (both lookup and retrieval has O(1)).
	Second In case the value exists we should move the last accessed node to the front of the double linked list by just adjusting the pointers with no need to traverse the whole list in the worst case.
So both the operations done in the hash map and the doubly linked list take O(1) because it is independent of the cache size.

[2] SET operation:
	First it checks if the key exists before so only update the value in the hash map which takes O(1) then move the node to the front in the doubly linked list and also takes O(1) because it only change the pointers of the current node and its previous and next node besides the list’s head and the list’s tail pointers.
	In this case no need to check the cache capacity for overflow

	Second If the key doesn’t exist we should check the cache capacity in order to remove the list tail in case of overflow. The removing tail takes O(1) and deleting also the same key from the hash map takes O(1). Then after confirming the cache ability for inserting the new node we add the new node to both the hash map in O(1) and to the front of the doubly linked list which also takes O(1).

So the key implementation for this problem is to avoid traversing the whole cache while manipulating its capacity and make all the operations independent from the number of items in it.

Time complexity is O(1)
Space complexity is O(n)
