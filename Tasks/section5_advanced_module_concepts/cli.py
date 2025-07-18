import sys
from helpers import greet
if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "User"
    print(greet(name))
