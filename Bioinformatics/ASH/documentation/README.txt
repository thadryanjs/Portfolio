This program analyzes FASTA sequences to find regions of chemical and amino acid distinctness. It takes in two FASTA files, a name for an output file, and a desired Kmer length via the command line. It scores them on simple scales based one structurally complex residues and hydrophilicity given their frequent use as predictors for antigenicity. More on the thought process behind the ASH scale can be found on the ASH github. The intent is that this tool can help users analyze protein sequence for epitope/antigen selection by automating the search for epitopes that are distinct to their protein or, conversely, find regions that are well conserved in both. The output is a csv file containing information on all the epitopes in the first protein, and the following pieces of information:

	Position in the sequence
	Hydrophilicity distinctness rating
	Percentage of Hydrophilic residues
	Structural complexity distinctness rating
	Percentage of structurally distinct residues
	Analog sequences, ie the kmer it is aligned to in sequence 2

The script was written using Python 3.5, with the additional dependency of scikit-bio.

The test_package includes two FASTA files for testing purposes, so main the program, run_ash.py, could be run as follows:

$ python3 run_ash.py --fasta1 sample_data/ENV_HV1MN.fasta --fasta2 sample_data/ENV_HV1VI.fasta --kmer 12 --outfile test_out.csv

to run the unit tests, run the following command from the ASH directory, substituting your path to pytests
$ /home/bbbuser/.local/bin/pytest test/testASH.py
