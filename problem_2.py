import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or suffix == '':
        return []
    if path is None or path == '' or not os.path.exists(path):
        print("This path does not exist")
        return []

    all_entries = list()
    find_files_recursive(suffix, path, all_entries)
    return sorted(all_entries)

def find_files_recursive(suffix, path, all_entries):
    current_entries = os.listdir(path)
    for entry in current_entries:
        nestedPath = os.path.join(path, entry)
        if os.path.isdir(nestedPath):
            find_files_recursive(suffix, nestedPath, all_entries)
        elif os.path.isfile(nestedPath) and nestedPath.endswith(suffix):
            all_entries.append(nestedPath)
#===================================================================================
def test_find_files(suffix, current_dir):
    files = find_files(suffix, current_dir)
    print(f"********* The number of files with suffix '{suffix}' in the path '{current_dir}' is = {len(files)} *********")
    if files:
        for file in files:
            print(file)
    else:
        print("No Files !!")
    print(f"******************************************************************************************")
#===================================================================================
if __name__ == "__main__":
    print("\n")
    # Let us print the files in the directory in which you are running this script
    #print (os.listdir("."))
    # Let us check if this file is indeed a file!
    #print (os.path.isfile("./ex.py"))
    # Does the file end with .py?
    #print ("./ex.py".endswith(".py"))
    #custom_dir = os.path.join(os.path.expanduser("~"), "Desktop/sara/NanoDegdree")
    print("\n************** < Test case 1 >*******************")
    current_dir = "."
    suffix = ".c"
    test_find_files(suffix, current_dir)
    print("\n************** < Test case 2 >*******************")
    suffix2 = ".py"
    test_find_files(suffix2, current_dir)
    print("\n************** < Test case 3 >*******************")
    suffix3 = ".md"
    test_find_files(suffix3, current_dir)
    print("\n************** < Test case 4 >*******************")
    suffix4 = ".txt"
    test_find_files(suffix4, current_dir)
    print("\n************** < Test case 5 > Handle None Path *******************")
    current_dir = None
    test_find_files(suffix2, current_dir)
    print("\n************** < Test case 6 > Handle Empty Path *******************")
    current_dir = ""
    test_find_files(suffix3, current_dir)
    print("\n************** < Test case 7 > Handle Wrong Path *******************")
    current_dir = "wrong_path"
    test_find_files(suffix4, current_dir)
    print("\n************** < Test case 8 > Handle Empty suffix *******************")
    current_dir = "."
    suffix5 = ""
    test_find_files(suffix5, current_dir)
    print("\n")
