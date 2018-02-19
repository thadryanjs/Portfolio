"""
index,  sequence,      hy_score  str_score hy_pct    str_pct    analog,
0,GIRRNYQHWWGWGTMLLG   3.75      6.0       0.11      0.28   GMQRNWQHLGKWGLLFLG
1,IRRNYQHWWGWGTMLLGL   4.0       6.5       0.11      0.28   MQRNWQHLGKWGLLFLGI
2,RRNYQHWWGWGTMLLGLL   3.5       6.0       0.11      0.28   QRNWQHLGKWGLLFLGIL
3,RNYQHWWGWGTMLLGLLM   3.5       6.0       0.06      0.28   RNWQHLGKWGLLFLGILI
4,NYQHWWGWGTMLLGLLMI   3.5       6.0       0.0       0.28   NWQHLGKWGLLFLGILII
5,YQHWWGWGTMLLGLLMIC   3.5       6.0       0.0       0.28   WQHLGKWGLLFLGILIIC

G I R R N Y Q H W W G W G T M L L G
G M Q R N W Q H L G K W G L L F L G
"""
a = "GIRRNYQHWWGWGTMLLG"
b = "GMQRNWQHLGKWGLLFLG"

class test(object):
#----------------------------------------------------------------------#
#                         weighted_score                               #
#----------------------------------------------------------------------#
# This implements the scale on a pair of residues. It is called by the #
# mismatch function to score pairs of peptides at an index             #
#----------------------------------------------------------------------#
    def hydro_score(residue1, residue2):
        # hydrophiles are positive, hydrophobic is negative, neutral is 0
        weight = {  "L":-0.5, "A":-0.5, "F":-0.5, "Y":-0.5, "W":-0.5,
                    "I":-0.5, "V":-0.5, "H":+0.0, "N":+0.0, "C":+0.0,
                    "G":+0.0, "M":+0.0, "Q":+0.0, "P":+0.0, "S":+0.0,
                    "T":+0.0, "D":+0.5, "E":+0.5, "R":+0.5, "K":+0.5 }
        # a gap is given a score of two in our system
        if residue1 == "-" or residue2 == "-":
            return 2.0
        # subscore is the abs value of the scores
        subscore = abs(weight[residue1] - weight[residue2])
        # same group returns 0.25
        if subscore == 0:
            return 0.25
        else:
            return subscore


#----------------------------------------------------------------------#
#                              mismatch                                #
#----------------------------------------------------------------------#
# This takes two kmers and iterates through them. It calls the         #
# weighted_score function on the two residues at each index and        #
# returns the total "mismatch" score for the kmer                      #
#----------------------------------------------------------------------#
    def hydro_mismatch(input_seq1, input_seq2):
        score = 0
        # iterate through length
        for i in range(len(input_seq1)):
            # excact match == no mismatch score
            if input_seq1[i] == input_seq2[i]:
                score += 0
            else:
                # call the weighted_score score method
                score += test.hydro_score(input_seq1[i], input_seq2[i])
        return score


#----------------------------------------------------------------------#
#                           structure_score                            #
#----------------------------------------------------------------------#
# Takes two residues. It calls the structure_score function on the two #
# residues at each index and returns the total subscore based of the   #
# structurally complex residues                                        #
#----------------------------------------------------------------------#
    def structure_score(residue1, residue2):
        weight = {  "L":+0.0, "A":+0.0, "F":+1.0, "Y":+1.0, "W":+1.0,
                    "I":+0.0, "V":+0.0, "H":+1.0, "N":+0.0, "C":+0.0,
                    "G":+0.0, "M":+0.0, "Q":+0.0, "P":+1.0, "S":+0.0,
                    "T":+0.0, "D":+0.0, "E":+0.0, "R":+0.0, "K":+0.0 }

        # a gap is given a score of two in our system
        if residue1 == "-" or residue2 == "-":
            return 2.0
        # subscore is the abs value of the scores
        subscore = abs(weight[residue1] - weight[residue2])
        # same group returns 0.25
        if subscore == 0:
            subscore = 0.5
            return subscore
        else:
            return subscore
#----------------------------------------------------------------------#
#                         structural_mismatch                          #
#----------------------------------------------------------------------#
# This takes two kmers and iterates through them. It calls the         #
# structure_score function on the two residues at each index and       #
# returns the total "mismatch" score for the kmer                      #
#----------------------------------------------------------------------#
    def structural_mismatch(input_seq1, input_seq2):
        struct = ["F","Y","W","P","H"]
        score = 0
        for i in range(len(input_seq1)):
            if input_seq1[i] not in struct and input_seq2[i] not in struct:
                score += 0
                print(input_seq1[i], input_seq2[i], score)
            elif input_seq1[i] == input_seq2[i]:
                score += 0
                print(input_seq1[i], input_seq2[i], score)
            else:
                score += test.structure_score(input_seq1[i], input_seq2[i])
                print(input_seq1[i], input_seq2[i], score)

        return score


#----------------------------------------------------------------------#
#                           hydro_percent                              #
#----------------------------------------------------------------------#
# This function takes a simple measure of antigenicty based on the     #
# percent of residues that are hydrophiles                             #
#----------------------------------------------------------------------#
    def hydro_percent(seq):
        simple_scores = ["D","E","R","K"]
        score = 0
        for item in seq:
            if item in simple_scores:
                score += 1
        return round(score/len(seq), 2)

print(test.structural_mismatch(a,b))
"""
Y W 0.5
W L 1.0
W G 1.0
L F 1.0
"""
