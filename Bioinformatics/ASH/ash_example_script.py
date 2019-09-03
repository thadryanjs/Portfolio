
### example script of a simple use case for ASH

# import the class
import ASH

# call the function on two files, select kmer size
hiv_ash_obj = ASH.Analysis("sample_data/ENV_HV1MN.fasta", "sample_data/ENV_HV1VI.fasta", 15)

# print alignment
print("Aligned Sequences:")
print(hiv_ash_obj.aligned)

hiv_entries = hiv_ash_obj.get_entries()

# look at the first 15 kmers and thier score
print("\nFirst 15 entries:")
for record in hiv_entries[:5]:
    print(record.seq, record.str_score)

# conditional filtration to find distinct regions with good antigenicty
print("\nFiltered Results:")
for record in hiv_entries:
    if record.hy_score > 10 and record.str_score > 2:
        print(record.seq, record.hy_score, "at", record.pos)
