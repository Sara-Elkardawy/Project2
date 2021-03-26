Problem 3: Huffman Coding
**************************************************
Design Decisions:

The data structure used is min-Heap, referring to https://docs.python.org/3/library/heapq.html.

Time complexity:

#Time analysis for each step in the encoding process:
*****************************************************

#Phase I - << Build the Huffman Tree >>:
	Step 1: Calculate frequencies: First, determine the frequency of each character in the message.
     Time Complexity is O(n), where n is the number of characters in the given data.
     Space Complexity is O(n)
	Step 2: Creating a priority queue using a min-heap
     Using heapify function to convert list of nodes into heap (priority queue)
     Time Complexity is O(n), since from the documentation-->    heapq.heapify(x): Transform list x into a heap, in-place, in linear time
     Space Complexity is O(n)
	Step 3: Build The huffman tree
     Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
     Create a new node with a frequency equal to the sum of the two nodes picked in the above step.
     This new node would become an internal node in the Huffman tree, and the two nodes would become the children.
     The lower frequency node becomes a left child, and the higher frequency node becomes the right child.
     Reinsert the newly created node back into the priority queue.
     Do you think that this reinsertion requires the sorting of priority queue again? If yes, then a min-heap could be a better choice due to the lower complexity of sorting the elements, every time there is an insertion.
     Repeat steps above until there is a single element left in the priority queue.
     Since the heapq is a binary heap, the push/pop operations time complexity is O(log n)
     Time Complexity analysis: (n * (3 log(n))) + Log (n)) ~= O(n*log(n))
     Space Complexity is O(n)

So the overall Time Complexity O(n * log(n)) and Space Complexity O(n) in Phase I.


#Phase II - << Generate the Encoded Data >>:
	Step 1: get binary codes corresponding to each character.
    Based on the Huffman tree, generate unique binary code for each character of our string message.
     For this purpose, you'd have to traverse the path from root to the leaf node.
     Time Complexity analysis: ~= O(n)
     Space Complexity is O(n)
	Step 2: encode data.
     Time Complexity analysis: ~= O(n)
     Space Complexity is O(n)
So the overall Time Complexity analysis: ~= O(n) and Space Complexity is O(n) in Phase II.

The total Time Complexity = O(n * log(n)) and  the  Space Complexity = O(n) in the encoding process
========================================================================================================================

#Time analysis for each step in the decoding process:
*****************************************************
    1. Declare a blank decoded string
    2. Pick a bit from the encoded data, traversing from left to right.
    3. Start traversing the Huffman tree from the root.
        If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
        If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    4. Repeat steps #2 and #3 until the encoded data is completely traversed.

     Time Complexity analysis: ~= O(n), where n is the number of bits in the encoded string
     Space Complexity is O(n)
