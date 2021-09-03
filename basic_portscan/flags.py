import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-p', dest="min_port", action="store", help="Define the low port", type=int, default=1)
parser.add_argument('-pe',dest="max_port", action="store", help = "Define the high port", type=int, default=1000)
if len(sys.argv) > 1 and sys.argv[1] == '-h':
    args = parser.parse_args()
else:
    args = parser.parse_args(sys.argv[2:])

if __name__ == '__main__':
    print("This is the file who contains the flags of the Port Scan")
    print(args.min_port, args.max_port)
