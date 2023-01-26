import os

root_dir = input("Enter the path to the root directory: ")

def list_dirs(root_dir):
    dirs = sorted([d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))])
    for d in dirs:
        print(os.path.join(root_dir, d))
        list_dirs(os.path.join(root_dir, d))

list_dirs(root_dir)
