
import argparse
import sys
import ASH


### get flagged commandline arguments

parser = argparse.ArgumentParser()

parser.add_argument("-f1", "--fasta1")
parser.add_argument("-f2", "--fasta2")
parser.add_argument("-k, ", "--kmer")
parser.add_argument("-o, ", "--outfile")

# parse ommand line input
args = parser.parse_args()



### handle exceptions

# fileIO
try:
    test_file = open(args.fasta1, "r")
except FileNotFoundError:
    sys.exit("Cannont open file for --fasta1")

try:
    test_file = open(args.fasta2, "r")
except FileNotFoundError:
    sys.exit("Cannont open file for --fasta2")

# type error for kmer
try:
    args.kmer = int(args.kmer)
except ValueError:
    sys.exit("Please enter an integer for --kmer")



###| main |###
ash_obj = ASH.Analysis(args.fasta1, args.fasta2, args.kmer)

# get entry objects
ash_entries = ash_obj.get_entries()

# inspect their seq attribute
for e in ash_entries:
    print(e.seq)
