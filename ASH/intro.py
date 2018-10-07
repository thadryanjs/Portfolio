from ASH import Analysis

test_obj = Analysis("test/test1.fasta", "test/test2.fasta", 1)

for i in test_obj.results:
    print(i.seq)
