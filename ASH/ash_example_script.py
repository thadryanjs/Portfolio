# import the class
import ash

# call the function on two files, select kmer size
hiv_ash_obj = ash.analyze("ENV_HV1MN.fasta", "ENV_HV1VI.fasta", 15)


# print alignment
print(hiv_ash_obj.aligned)

hiv_entries = hiv_ash_obj.get_entries()

# look at the first 15 kmers and thier score
for record in hiv_entries[:5]:
    print(record.seq, record.score)

# conditional filtration to find distinct regions with good antigenicty
print("Filtered Results:")
for record in hiv_entries:
    if record.score > 5 and record.antg > 0.4:
        print(record.seq, record.score, "at", record.pos)
