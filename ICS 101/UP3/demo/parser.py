import argparse

parser = argparse.ArgumentParser(description='parser example')
parser.add_argument('-i', type=int, default=0)
parser.add_argument('-f', type=float, default=-1.0)
parser.add_argument('-s', type=str)

print(parser.parse_args())
args = parser.parse_args()
my_int = args.i

print('my_int is: ', my_int)
