import sys
# importing "heapq" to implement heap queue
import heapq

#===============================================================================
class Huffman_Tree_Node(object):
    """
    Each row in the table above can be represented as a node having a character, frequency, left child, and right child.
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return "(char = {}, freq = {})".format(self.char,self.freq)
    def __repr__(self):
        return "(char = {}, freq = {})".format(self.char,self.freq)

    def __lt__(self, other):
        """
        Less than method used in the heap comparison
        """
        return self.freq < other.freq

#=================================================================================
#==================== #Phase I - << Build the Huffman Tree >> ====================
def get_frequencies(data):
    """
    Phase I - << Build the Huffman Tree >> - Step 1: Calculate frequencies

     First, determine the frequency of each character in the message.

     Time Complexity is O(n), where n is the number of characters in the given data.
     Space Complexity is O(n)
    """
    frequencies_dict = {}
    for char in data:
        if frequencies_dict.get(char) is None:
            frequencies_dict[char] = 1
        else:
            frequencies_dict[char] += 1
    return frequencies_dict


def build_heap(frequencies):
    """
    Phase I - << Build the Huffman Tree >> - Step 2: Creating a priority queue using a min-heap

     Using heapify function to convert list of nodes into heap (priority queue)

     Time Complexity is O(n), since from the documentation-->
        heapq.heapify(x): Transform list x into a heap, in-place, in linear time
     Space Complexity is O(n)
    """
    huffman_heap = []
    for k in frequencies:
        huffman_heap.append(Huffman_Tree_Node(k,frequencies[k]))
    heapq.heapify(huffman_heap)
    return huffman_heap


def build_tree(huffman_heap):
    """
    Phase I - << Build the Huffman Tree >> - Step 3: Build The huffman tree

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
    """
    while len(huffman_heap) > 1:
        min_node_1 = heapq.heappop(huffman_heap)
        min_node_2 = heapq.heappop(huffman_heap)
        merged_node = Huffman_Tree_Node(None, (min_node_1.freq + min_node_2.freq))
        merged_node.left_child = min_node_1
        merged_node.right_child = min_node_2
        heapq.heappush(huffman_heap, merged_node)
    return heapq.heappop(huffman_heap)


def build_huffman_tree(data):
    """
    Phase I - << Build the Huffman Tree >> -
        Step 1: Calculate frequencies
        Step 2: Creating a priority queue using a min-heap
        Step 3: Build The huffman tree

    Time Complexity O(n * log(n))
    Space Complexity O(n)
    """
    frequencies_dict = get_frequencies(data)
    huffman_heap = build_heap(frequencies_dict)
    huffman_tree_root = build_tree(huffman_heap)
    return huffman_tree_root

#===============================================================================
#============== #Phase II - << Generate the Encoded Data >> ===========


def get_codes(huffman_tree_root, codes_dict):
    """
    Phase II - << Generate the Encoded Data >> Step 1: get binary codes corresponding to each character.

    Based on the Huffman tree, generate unique binary code for each character of our string message.
     For this purpose, you'd have to traverse the path from root to the leaf node.

    Points to Notice
    1) Notice that the whole code for any character is not a prefix of any other code. Hence, the Huffman code is called a Prefix code.
    2) Notice that the binary code is shorter for the more frequent character, and vice-versa.
    3) The Huffman code is generated in such a way that the entire string message would now require a much lesser amount of memory in binary form.
    4) Notice that each node present in the original priority queue has become a leaf node in the final Huffman tree.

     Time Complexity analysis: ~= O(n)
     Space Complexity is O(n)
    """
    # Handling the special case when the string consists of only 1 character like 'a' or 'aaaaa' so no merged nodes
    if huffman_tree_root.char:
        codes_dict[huffman_tree_root.char] = '1'
    else:
        add_codes_recursive(huffman_tree_root, "" , codes_dict)
    return codes_dict


def add_codes_recursive(node, curr_code , codes_dict):
    if node is None:
        return
    elif node.char is None: #merged node
        add_codes_recursive(node.left_child, curr_code+"0" , codes_dict)
        add_codes_recursive(node.right_child, curr_code+"1", codes_dict)
    else: #leaf node so add its binary code
        codes_dict[node.char] = curr_code

def encode_data(data, codes_dict):
    """
    Phase II - << Generate the Encoded Data >> Step 2: encode data.
     Time Complexity analysis: ~= O(n)
     Space Complexity is O(n)
    """
    encoded_data = ""
    for char in data:
        encoded_data += codes_dict[char]
    return encoded_data

def generate_encoded_data(data, huffman_tree_root, codes_dict):
    """
    Phase II - << Generate the Encoded Data >>
        Step 1: get binary codes corresponding to each character.
        Step 2: encode data.
         Time Complexity analysis: ~= O(n)
         Space Complexity is O(n)
    """
    codes_dict = get_codes(huffman_tree_root, codes_dict)
    return encode_data(data, codes_dict)

#===============================================================================
def huffman_encoding(data):
    """
    Time Complexity O(n * log(n))
    Space Complexity O(n)
    """
    if len(data) == 0:
        return "", None
    huffman_tree_root = build_huffman_tree(data)
    codes_dict = {}
    encoded_data = generate_encoded_data(data, huffman_tree_root, codes_dict)
    return encoded_data, huffman_tree_root

#===============================================================================
def huffman_decoding(data,tree):
    """
    1. Declare a blank decoded string
    2. Pick a bit from the encoded data, traversing from left to right.
    3. Start traversing the Huffman tree from the root.
        If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
        If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    4. Repeat steps #2 and #3 until the encoded data is completely traversed.

     Time Complexity analysis: ~= O(n)
     Space Complexity is O(n)

    """
    decoded_data = ""
    node = tree
    if len(data)==0:
        return decoded_data
    elif tree.char:
        for i in range(len(data)):
            decoded_data += tree.char
    else:
        for i in range(len(data)):
            if data[i] == '0':
                node = node.left_child
            else:
                node = node.right_child
            if node.char:
                decoded_data += node.char
                node = tree
    return decoded_data

#===============================================================================
def test(a_great_sentence):
    print(f" The Input String : << '{a_great_sentence}' >>\n")
    if a_great_sentence:
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence) if len(a_great_sentence)>0 else 0))
        print ("The content of the data is: '{}'\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2)) if len(encoded_data)>0 else 0))
        print ("The content of the encoded data is: '{}'\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data) if len(decoded_data)>0 else 0))
        print ("The content of the decoded data is: '{}'\n".format(decoded_data))

        if a_great_sentence == decoded_data:
            print("No data loss, since the decoded data is same as the original data.")
    else:
        print("The input string is empty !!")
#===============================================================================

if __name__ == "__main__":
    codes = {}
    print("\n")
    print("************** < Test case 1 >*******************")
    test(None)
    print("\n")
    print("************** < Test case 2 >*******************")
    test("")
    print("\n")
    print("************** < Test case 3 >*******************")
    test("The bird is the word")
    print("\n")
    print("************** < Test case 4 >*******************")
    test("AAAAAAABBBCCCCCCCDDEEEEEE")
    print("\n")
    print("************** < Test case 5 >*******************")
    test("a")
    print("\n")
    print("************** < Test case 6 >*******************")
    test("aaaaaaa")
    print("\n")
