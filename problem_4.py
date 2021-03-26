class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
##=================================================================================
def is_user_in_group_recursive(user, group, visited_groups):
    visited_groups.add(group.name)

    # Step 1: search in users list:
    # this search takes O(n) , where n is the number of elements in the list, either by iterating over the list item by item or the second choice is to use the 'in' operation which also takes O(n) or the third choice by converting the list to set() in O(n) then searches in the set in O(1). The third choice using the set() increases the space complexity to O(n). So I decided to use ‘in’ operator.
    # If it is flexible to change the users data type in the Group class, the best choice for it is a Set().

    #Step 2: search in groups list
    # search in the nested groups and skip any group visited before to improve the searching and avoid repeated work.
    # Time complexity is O(m), where m is the number of subgroups

    return user in group.users or any(is_user_in_group_recursive(user, sub_group, visited_groups) for sub_group in group.get_groups() if sub_group.name not in visited_groups)

##=================================================================================

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    visited_groups= set()
    exists = is_user_in_group_recursive(user, group, visited_groups)
    return exists


##=================================================================================
dummy_user = "dummy"

parent_user = "sara"
parent = Group("parent")
parent.add_user(parent_user)

child = Group("child")
sub_child = Group("subchild")
sub_child2 = Group("subchild2")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

sub_child2_user = "sub_child_user2"
sub_child2.add_user(sub_child2_user)
sub_child2.add_group(parent)

child.add_group(sub_child)
child.add_group(sub_child2)

parent.add_group(child)

print("\n")
print("************** < Test case 1 >*******************")
print(f"Searching for <{sub_child_user}> in the group <{parent.name}>, the result is = <{is_user_in_group(sub_child_user, parent)}> ")
print("************** < Test case 2 >*******************")
print(f"Searching for <{sub_child_user}> in the group <{child.name}>, the result is = <{is_user_in_group(sub_child_user, child)}> ")
print("************** < Test case 3 >*******************")
print(f"Searching for <{sub_child_user}> in the group <{sub_child.name}>, the result is = <{is_user_in_group(sub_child_user, sub_child)}> ")
print("************** < Test case 4 >*******************")
print(f"Searching for <{sub_child_user}> in the group <{sub_child2.name}>, the result is = <{is_user_in_group(sub_child_user, sub_child2)}> ")
print("\n")

print("************** < Test case 5 >*******************")
print(f"Searching for <{sub_child2_user}> in the group <{parent.name}>, the result is = <{is_user_in_group(sub_child2_user, parent)}> ")
print("************** < Test case 6 >*******************")
print(f"Searching for <{sub_child2_user}> in the group <{child.name}>, the result is = <{is_user_in_group(sub_child2_user, child)}> ")
print("************** < Test case 7 >*******************")
print(f"Searching for <{sub_child2_user}> in the group <{sub_child.name}>, the result is = <{is_user_in_group(sub_child2_user, sub_child)}> ")
print("************** < Test case 8 >*******************")
print(f"Searching for <{sub_child2_user}> in the group <{sub_child2.name}>, the result is = <{is_user_in_group(sub_child2_user, sub_child2)}> ")
print("\n")

print("************** < Test case 9 >*******************")
print(f"Searching for <{parent_user}> in the group <{parent.name}>, the result is = <{is_user_in_group(parent_user, parent)}> ")
print("************** < Test case 10 >*******************")
print(f"Searching for <{parent_user}> in the group <{child.name}>, the result is = <{is_user_in_group(parent_user, child)}> ")
print("************** < Test case 11 >*******************")
print(f"Searching for <{parent_user}> in the group <{sub_child.name}>, the result is = <{is_user_in_group(parent_user, sub_child)}> ")
print("************** < Test case 12 >*******************")
print(f"Searching for <{parent_user}> in the group <{sub_child2.name}>, the result is = <{is_user_in_group(parent_user, sub_child2)}> ")
print("\n")

print("************** < Test case 13 >*******************")
print(f"Searching for <{dummy_user}> in the group <{parent.name}>, the result is = <{is_user_in_group(dummy_user, parent)}> ")
print("************** < Test case 14 >*******************")
print(f"Searching for <{dummy_user}> in the group <{child.name}>, the result is = <{is_user_in_group(dummy_user, child)}> ")
print("************** < Test case 15 >*******************")
print(f"Searching for <{dummy_user}> in the group <{sub_child.name}>, the result is = <{is_user_in_group(dummy_user, sub_child)}> ")
print("************** < Test case 16 >*******************")
print(f"Searching for <{dummy_user}> in the group <{sub_child2.name}>, the result is = <{is_user_in_group(dummy_user, sub_child2)}> ")
print("\n")
