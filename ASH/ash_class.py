from skbio.alignment import StripedSmithWaterman

class ASH(object):


    def __init__(self, first_seq_in, second_seq_in, kmer):
        self.kmer_size    = kmer
        self.first_fasta  = self.get_seq(first_seq_in)
        self.second_fasta = self.get_seq(second_seq_in)

        self.aligned      = self.align(self.first_fasta,
                                       self.second_fasta)

        self.sequence1    = self.aligned[0]
        self.sequence2    = self.aligned[1]

        self.results      = self.seq_to_seq(self.sequence1,
                                            self.sequence2,
                                            self.kmer_size)
        self.output       = self.report(self.results)


    class Entry(object):


        def __init__(self, seq, pos, score, match, antg):
            self.seq   =   seq   # the peptide
            self.pos   =   pos   # what index is appears
            self.score = score   # the mismatch score
            self.match = match   # what it was compared to
            self.antg  = antg    # the simple antigenicty score


    def get_Entries(self):
        return self.results


    def get_seq(self, filename):
        seq = ''
        data = open(filename, 'r').readlines()
        for line in data:
            if not line.startswith('>'): # skips header
                line = line.replace('\n', '')
                seq += line
        return seq


    def align(self, seq1, seq2):
        aligned_seqs = []
        query = StripedSmithWaterman(seq1)
        align = query(seq2)
        aligned_seqs.append(align.aligned_query_sequence)
        aligned_seqs.append(align.aligned_target_sequence)
        return aligned_seqs


    def weighted_score(self, residue1, residue2):
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


    def mismatch(self, input_seq1, input_seq2):
        score = 0
        for i in range(len(input_seq1)):
            if input_seq1[i] == input_seq2[i]:
                score += 0
            else:
                score += self.weighted_score(input_seq1[i], input_seq2[i])
        return score


    def antigenicity(self, seq):
        simple_scores = ["D","E","R","K"]
        score = 0
        for item in seq:
            if item in simple_scores:
                score += 1
        return round(score/len(seq), 2)


    def seq_to_seq(self, seq1, seq2, length):
        results = []
        position = 0
        while position + length <= len(seq1):
            current_peptide = seq1[position:position+length]
            compare_peptide = seq2[position:position+length]
            entry = self.mismatch(current_peptide, compare_peptide)
            results_obj = self.Entry(
                seq   = current_peptide,
                pos   = position,
                score = entry,
                match = compare_peptide,
                antg  = self.antigenicity(current_peptide))
            results.append(results_obj)
            position += 1
        return results

    def report(self, records):
        outfile = open("results.csv", "w")

        outfile.write("index,sequence,ash_score,antigenicty,analog_sequence\n")

        for item in records:
            outfile.write(str(item.pos)   + "," +
                          item.seq        + "," +
                          str(item.score) + "," +
                          str(item.antg)  + "," +
                          item.match      + "\n")

        outfile.close()



test = ASH("ENV_HV1MN.fasta", "ENV_HV1VI.fasta", 15)
