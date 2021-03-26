Problem 4: Active Directory
*************************************************
Design Decisions:

Only use an additional Set() data structure to keep track of the visited groups to avoid manipulating the same group multiple times.

Time complexity:

	Step 1: search in users list:
this search takes O(n) , where n is the number of elements in the list, either by iterating over the list item by item or the second choice is to use the 'in' operation which also takes O(n) or the third choice by converting the list to set() in O(n) then searches in the set in O(1). The third choice using the set() increases the space complexity to O(n). So I decided to use ‘in’ operator.
If it is flexible to change the users data type in the Group class, the best choice for it is a Set().

  Step 2: search in groups list
Search in the nested groups and skip any group visited before, to improve the searching and avoid repeated work. This search is considered DFS.
    Time complexity is O(m), where m is the number of subgroups.

The overall time complexity is O(n) where n is the number of files & folders under the parent root.
The space complexity is according to the depth of the tree. The overall space complexity is O(n) where n is the number of files & folders under the parent root.
