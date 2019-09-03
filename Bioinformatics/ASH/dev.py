# hydrophiles are positive, hydrophobic is negative, neutral is 0
hydro_weight = { "L":-0.5, "A":-0.5, "F":-0.5, "Y":-0.5, "W":-0.5,
                 "I":-0.5, "V":-0.5, "H":+0.0, "N":+0.0, "C":+0.0,
                 "G":+0.0, "M":+0.0, "Q":+0.0, "P":+0.0, "S":+0.0,
                 "T":+0.0, "D":+0.5, "E":+0.5, "R":+0.5, "K":+0.5 }

def hydro_score(residue1, residue2):

    # matches can't have distance
    if residue1 == residue2:
        return 0

    if residue1 == "-" or residue2 == "-":
        return 2.0
    # subscore is the abs value of the scores
    subscore = abs(hydro_weight[residue1] - hydro_weight[residue2])
    # same group returns 0.25
    if subscore == 0:
        return 0.25
    else:
        return subscore

print(hydro_score("-", "-"))
