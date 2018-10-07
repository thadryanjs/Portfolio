#----------------------------------------------------------------------#
#               Antigen Selection Heuristic {ASH}                      #
#----------------------------------------------------------------------#
#                                                                      #
#                  Written by Thadryan J. Sweeney                      #
#                      with Python 3.5.3                               #
#                           2/13/18                                    #
#                                                                      #
#                     Usage Dependencies:                              #
#                        -Python 3.5.3                                 #
#                        -Scikit-bio                                   #
#                                                                      #
# This program analyzes FASTA sequences to find regions of chemical    #
# distinctness and antigenicty. It takes in two fasta files, a name    #
# for an output file,and a desired Kmer length via the command line.   #
# It scores them on a simple hydrophilicity-based scale developed for  #
# this script. More on the thought process behind the ASH scale can be #
# foond on the ASH github. It also implements a simple hydrophilicity  #
# -based antigenicty metric that is currently under development at the #
# time of tis writing (2/13/18). The intent is that this tool can help #
# users analyze protein sequence for epitope/antigen selection by      #
# automating the search for eptitopes that are distinct to their       #
# protein or, conversly, find regions that are well conserved in       #
# both. The output is a csv file containing information on all the     #
# eptitopes in the first protein, it's ASH score, it's index in the    #
# sequence, it's antigenicty rating, and the sequence it's analog in   #
# the second sequence.                                                 #
#----------------------------------------------------------------------#


import sys
from skbio.alignment import StripedSmithWaterman
from models.Entry import Entry

class Analysis(object):

    # hydrophiles are positive, hydrophobic is negative, neutral is 0
    hydro_weight = {  "L":-0.5, "A":-0.5, "F":-0.5, "Y":-0.5, "W":-0.5,
                      "I":-0.5, "V":-0.5, "H":+0.0, "N":+0.0, "C":+0.0,
                      "G":+0.0, "M":+0.0, "Q":+0.0, "P":+0.0, "S":+0.0,
                      "T":+0.0, "D":+0.5, "E":+0.5, "R":+0.5, "K":+0.5 }

    struct_weight = {  "L":+0.0, "A":+0.0, "F":+1.0, "Y":+1.0, "W":+1.0,
                       "I":+0.0, "V":+0.0, "H":+1.0, "N":+0.0, "C":+0.0,
                       "G":+0.0, "M":+0.0, "Q":+0.0, "P":+1.0, "S":+0.0,
                       "T":+0.0, "D":+0.0, "E":+0.0, "R":+0.0, "K":+0.0 }

#----------------------------------------------------------------------#
#                            constructor                               #
#----------------------------------------------------------------------#
# The constructor takes 3 arguments: two .fasta files and an integer   #
# of the desired kmer length. It calls functions to get the sequences  #
# out of the files(get_seq), align the sequences (align), compare them #
# using the scale(seq_to_seq), and writes the data to a csv            #
#----------------------------------------------------------------------#
    def __init__(self, first_seq_in, second_seq_in, kmer):
        # the kmer size
        self.kmer_size    = kmer
        # get the two sequences
        self.first_fasta  = self.get_seq(first_seq_in)
        self.second_fasta = self.get_seq(second_seq_in)
        # call the skikit bio alignmnt function
        self.aligned      = self.align(self.first_fasta,
                                       self.second_fasta)
        # get the two sequences from the alignment
        self.sequence1    = self.aligned[0]
        self.sequence2    = self.aligned[1]
        # implement the ASH proceedure on the two sequences
        self.results      = self.seq_to_seq(self.sequence1,
                                            self.sequence2,
                                            self.kmer_size)


#----------------------------------------------------------------------#
#                            get_entries                               #
#----------------------------------------------------------------------#
# Member of ASH class, not Entry. Basic getter method returns list of  #
# Entry objects created when a new ASH object is created.              #                                 #
#----------------------------------------------------------------------#
    def get_entries(self):
        return self.results


#----------------------------------------------------------------------#
#                            get_seq                                   #
#----------------------------------------------------------------------#
# This is a vanilla fasta parser for solo fasta files. Skips header,   #
# strips newlines, and concatenates sequences. Returns sequence        #
#----------------------------------------------------------------------#
    def get_seq(self, filename):
        # will store the sequence
        seq = ""
        # bail if file is not valid
        data = open(filename, "r").readlines()
        # get the sequence
        for line in data:
            if not line.startswith(">"):      # skips header
                line = line.replace("\n", "") # removes newlines
                seq += line
        return seq


#----------------------------------------------------------------------#
#                               align                                  #
#----------------------------------------------------------------------#
# Takes the parsed fasta files from get_seq (called by contructor) and #
# passes them to scikit bio's StripedSmithWaterman function. Returns   #
# an array with the sequences. We need to access the sequences         #
# individually now that the gaps have been filled in appropiately      #
#----------------------------------------------------------------------#
    def align(self, seq1, seq2):
        # store sequences
        aligned_seqs = []
        # make initial query
        query = StripedSmithWaterman(seq1)
        # align second seq against initial query
        align = query(seq2)
        # add individual sequences to results
        print(align.aligned_query_sequence)
        print(align.aligned_target_sequence)

        aligned_seqs.append(align.aligned_query_sequence)
        aligned_seqs.append(align.aligned_target_sequence)
        return aligned_seqs


#----------------------------------------------------------------------#
#                           hydro__score                               #
#----------------------------------------------------------------------#
# This implements the scale on a pair of residues. It is called by the #
# mismatch function to score pairs of peptides at an index             #
#----------------------------------------------------------------------#
    def hydro_score(self, residue1, residue2):
        if residue1 == "-" or residue2 == "-":
            return 2.0
        # matches can't have distance
        if residue1 == residue2:
            return 0
        # subscore is the abs value of the scores
        subscore = abs(self.hydro_weight[residue1] - self.hydro_weight[residue2])
        # same group returns 0.25
        if subscore == 0:
            return 0.25
        else:
            return subscore


#----------------------------------------------------------------------#
#                       hydro_ mismatch                                #
#----------------------------------------------------------------------#
# This takes two kmers and iterates through them. It calls the         #
# weighted_score function on the two residues at each index and        #
# returns the total "mismatch" score for the kmer                      #
#----------------------------------------------------------------------#
    def hydro_mismatch(self, input_seq1, input_seq2):
        score = 0
        # iterate through length
        for i in range(len(input_seq1)):
            # excact match == no mismatch score
            if input_seq1[i] == input_seq2[i]:
                score += 0
            else:
                # call the weighted_score score method
                score += self.hydro_score(input_seq1[i], input_seq2[i])
        return score


#----------------------------------------------------------------------#
#                           structure_score                            #
#----------------------------------------------------------------------#
# Takes two residues. It calls the structure_score function on the two #
# residues at each index and returns the total subscore based of the   #
# structurally complex residues                                        #
#----------------------------------------------------------------------#
    def structure_score(self, residue1, residue2):
        # a gap is given a score of two in our system
        if residue1 == "-" or residue2 == "-":
            return 2.0
        # subscore is the abs value of the scores
        subscore = abs(self.struct_weight[residue1] -self.struct_weight[residue2])
        # same group returns 0.25
        if subscore == 0:
            return 0.5
        else:
            return subscore

#----------------------------------------------------------------------#
#                         structural_mismatch                          #
#----------------------------------------------------------------------#
# This takes two kmers and iterates through them. It calls the         #
# structure_score function on the two residues at each index and       #
# returns the total "mismatch" score for the kmer                      #
#----------------------------------------------------------------------#
    def structural_mismatch(self, input_seq1, input_seq2):
        struct = ["F","Y","W","P","H"]
        score = 0
        for i in range(len(input_seq1)):
            # ignore if it they're both not a complex residue
            if input_seq1[i] not in struct and input_seq2[i] not in struct:
                score += 0
            # match is nothing
            elif input_seq1[i] == input_seq2[i]:
                score += 0
            # else use the weights to give score
            else:
                score += self.structure_score(input_seq1[i], input_seq2[i])
        return score


#----------------------------------------------------------------------#
#                           hydro_percent                              #
#----------------------------------------------------------------------#
# This function takes a simple measure of antigenicty based on the     #
# percent of residues that are hydrophiles                             #
#----------------------------------------------------------------------#
    def hydro_percent(self, seq):
        simple_scores = ["D","E","R","K"]
        score = 0
        for item in seq:
            if item in simple_scores:
                score += 1
        return round(score/len(seq), 2)


#----------------------------------------------------------------------#
#                           struct_percent                             #
#----------------------------------------------------------------------#
# This function takes a simple measure of antigenicty based on the     #
# percent of residues that are hydrophiles                             #
#----------------------------------------------------------------------#
    def struct_percent(self, seq):
        simple_scores = ["F","Y","W","P","H"]
        score = 0
        for item in seq:
            if item in simple_scores:
                score += 1
        return round(score/len(seq), 2)


#----------------------------------------------------------------------#
#                            seq_to_seq                                #
#----------------------------------------------------------------------#
# This function is the driver of the tool. It acts on the whole        #
# protein sequence of the files entered into the contructor. It also   #
# takes the kmer length argument. It iterates through the whole        #
# of both sequences in steps equal to the kmer size. It asses the two  #
# kmers at that region in both proteins, and scores them. It builds an #
# Entry object for each kmer, and returns a list of Entry objects      #
#----------------------------------------------------------------------#
    def seq_to_seq(self, seq1, seq2, length):
        # to store Entry objects
        results = []
        # start at zero
        position = 0
        # while move along the sequence won't put us over the edge
        while position + length <= len(seq1):
            # the current_peptide is the kmer is seq one, it
            # starts at the currrent position, ends at position + kmer length
            current_peptide = seq1[position:position+length]
            compare_peptide = seq2[position:position+length]
            # call hydro mismatch on the current kmers
            hydro_entry     = self.hydro_mismatch(current_peptide,
                                                  compare_peptide)
            # get percent hydrophiles
            hydro_entry_pct = self.hydro_percent(current_peptide)
            # get structural mismatch of current kmers
            struct_entry    = self.structural_mismatch(current_peptide,
                                                       compare_peptide)
            # find percent structurally complex residues
            struct_entry_pct = self.struct_percent(current_peptide)

            # store results is an Entry object
            results_obj   = Entry(
                seq       = current_peptide,
                pos       = position,
                hy_score  = hydro_entry,
                hy_pct    = hydro_entry_pct,
                str_score = struct_entry,
                str_pct   = struct_entry_pct,
                analog    = compare_peptide)
            # store object, increment
            results.append(results_obj)
            position += 1
        return results


#-----------------------------------------------------------------------#
'''
main = analyze("ENV_HV1MN.fasta", "ENV_HV1VI.fasta", 15)

e = main.get_entries()

for i in e:
    print(i.seq)
'''
