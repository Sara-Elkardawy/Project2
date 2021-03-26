Problem 2: File Recursion analysis:
**************************************************************

Design Decisions:

The data structure used is List()

Time complexity:

Time complexity is O(n) when n is the number of all files under the targeted directory and its nested folders also, because the used function from OS module “listdir” takes a linear time and for each nested directory another linear time counted.
So Overall time complexity is O(n).

Space complexity is O(depth of the directories tree under the parent directory)
