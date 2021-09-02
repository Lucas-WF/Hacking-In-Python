import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-p', action="store", help="Define the low port", type=int, default=1)
parser.add_argument('-pe', action="store", help = "Define the high port", type=int, default=1000)
args = parser.parse_args()
