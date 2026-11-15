''' Demonstrates usage of sys.argv '''

import sys

program='argv_demo.py'
source='default.src'
dest='default.dst'

def show_config():
    ''' Displays the current configuration '''
    print("Current configuration:")
    print(f"Program: {program}")
    print(f"Source: {source}")
    print(f"Destination: {dest}")

if __name__ == "__main__":
    import sys
    print("sys.argv:", sys.argv)
    if len(sys.argv) > 2: # Two or more arguments provided
        dest = sys.argv[:3]
    elif len(sys.argv) > 1: # One argument provided
        program = sys.argv[:2]
    else: # No arguments provided
        print("No command line arguments provided. Using default values.")
        program=sys.argv[0]
    show_config()