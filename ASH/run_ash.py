
import argparse
import sys
import ASH


 """   |get flagged commandline arguments|   """

parser = argparse.ArgumentParser()

parser.add_argument("-f1", "--fasta1")
parser.add_argument("-f2", "--fasta2")
parser.add_argument("-k, ", "--kmer")
parser.add_argument("-o, ", "--outfile")

# parse them
args = parser.parse_args()


"""   |handle exceptions|   """

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


"""   |main|   """

ash_obj = ASH.Analysis(args.fasta1, args.fasta2, args.kmer)

# open outfile
with open(args.outfile, "w") as outfile:
    # write header
    outfile.write("\t".join(["seq", "pos", "hy_score", "str_score", "analog", "hy_pct", "str_pct\n"]))
    # iterate entries in ASH report
    for e in ash_obj.get_entries():
        # get entries attributes as strings, write them to csv 
        out_data = map(str, [e.seq, e.pos, e.hy_score, e.str_score, e.analog, e.hy_pct, e.str_pct, "\n"])
        outfile.write("\t".join(out_data))
    outfile.close()
