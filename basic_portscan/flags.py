import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest="min_port", action="store", help="Define the low port", type=int, default=1)
parser.add_argument('-pe',dest="max_port", action="store", help = "Define the high port", type=int, default=1000)
if len(sys.argv) > 1 and sys.argv[1] == '-h' or len(sys.argv) > 1 and sys.argv[1] == "--help":
    args = parser.parse_args()
elif __name__ == '__main__':
    args = parser.parse_args()
    print("This is the file who contains the flags of the Port Scan")
    print(f"The min port is {args.min_port}, the max port is {args.max_port}")
else:
    args = parser.parse_args(sys.argv[2:])
