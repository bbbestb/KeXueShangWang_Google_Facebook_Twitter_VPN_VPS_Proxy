'''
just have a try with argparse.
e.g. python try_argparse.py -v -c 10
'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("-c", "--copy", help="use * copies")
args = parser.parse_args()
if args.verbose:
    print "verbosity turned on"
else:
    print "No --verbose arg"
if args.copy:
    copies = int(args.copy)
    for i in range(0, copies):
        print '%d copy' % i
