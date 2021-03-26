Problem 6: Union And Intersection Of Two LinkedLists
*********************************************************************************************
Design Decisions:
Using the set data structure because it is efficient in both lookup and removing the duplicates.

Time complexity-Union:
Step 1: Convert the linked lists to a Set to handle the duplicates and be ready for the union operation.
    This step takes O(n1+n2), where n1 is the number of elements in the list1 and n2 is the number of elements in list_2.
    Hence the adding operation in Sets is O(1), so the overall time in this step = O(n), where n is the total number of elements in both lists.

Step2: Define a new linked list to return the union result as a linked list
    Time Complexity for this step is O(n), where n is the number of total elements in the union set without any duplicates, since I updated the append function in the linked list class to be O(1) by adding a tail pointer.

The overall time complexity is O(n), where n is the total number of items in the 2 lists,.
The space complexity is O(n), where n is the total number of items in the 2 lists.


Time complexity-Intersection:
Step1: convert both list 1 and list 2 to 2 Sets because the <Set> data structure is efficient to handle lookups in O(1).
This step takes O(n1+n2), where n1 is the number of elements in the list1 and n2 is the number of elements in list_2.

Step2: do the intersection by iterating over the first set and checks if the number exists in the other set.
    The time complexity in this step is O(n), where n is the length of the list 1, since the search in set 2 takes O(1).

Step3: Define a new linked list to return the intersection result as a linked list
    Time Complexity for this step is O(n), where n is the number of total elements in the intersection set without any duplicates.

The overall time complexity is O(n), where n is the total number of items in the 2 lists,.
The space complexity is O(n), where n is the total number of items in the 2 lists.
