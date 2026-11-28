import os

print()
print("Find directory tree using path and directory name")
# Get user input for the directory name to search for
# Default to cwd if no input is provided
directory_name = input("Enter the directory name to search for: ")
if not directory_name:
    directory_name = os.getcwd()
# Get user input for the path to search in
search_path = input("Enter the path to search in: ")
if not search_path:
    search_path = os.getcwd()
# Use os.walk to traverse the directory tree
# Note: os.walk returns a generator that yields a tuple of (root, dirs, files) for each directory in the tree
# This can use a lot of memory if the directory tree is large, so be careful when using it on large directories or drive roots.
for root, dirs, files in os.walk(search_path):
    if directory_name in dirs:
        print("Directory found at:", os.path.join(root, directory_name))
    # print list of subdirectories in the directory_name directory if it exists
    if directory_name in dirs:
        # get subdirectories in the directory_name directory
        directory_name = os.path.join(root, directory_name)
        print("Subdirectories:", os.listdir(directory_name))
        # print("Files:", files)python_PCAP_exercises
    # exit the loop
        break


