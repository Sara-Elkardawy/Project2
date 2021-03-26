Problem 5: Blockchain
*********************************************
Design Decisions:

The blockchain represented as a linked list and each block has a previous pointer to the previous chain. Linked list maintain that the insertion time complexity is O(1).

Time complexity:

	Method 1 <add_block>: takes O(1) by just updating the linked list head and tail pointers.
	Method 2 <get_chain_size>: takes O(1).
	Method 3 <to_list>: takes O(n) to traverse the blockchain, where n is the number of blocks.
	Method 4 <display>: takes O(n).
