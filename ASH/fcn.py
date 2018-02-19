# # longest without being twice in a row.
# # should I make this 3
# def no_repeat2(seq):
#     longest = ""
#     length = len(seq)
#     i = 0
#     for i in range(len(seq)-1):
#         current = seq[i]
#         while i < length-1:
#             if seq[i+1] != seq[i]:
#                 current += seq[i+1]
#             else:
#                 break
#             i += 1
#         if len(current) > len(longest):
#             longest = current
#     return longest
# print(no_repeat2("Thadryddan"))


def structural_mismatch(input_seq1, input_seq2):
    score = 0
    for i in range(len(input_seq1)):
        if input_seq1[i] == input_seq2[i]:
            score += 0
        else:
            score += structure_score(input_seq1[i], input_seq2[i])
    return score


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
        return 0.5
    else:
        return subscore
print(structural_mismatch("PEPWIDE",
                          "PEPHIDE"))
