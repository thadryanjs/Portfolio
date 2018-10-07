import sys

# add to path so tests can be run from home directory
sys.path.append(".")
from ASH import Analysis

test_obj = Analysis("test/test1.fasta", "test/test2.fasta", 15)

### testing get seq
def test_get_seq_first():
    print("testing get_seq, first sequence")
    assert(test_obj.first_fasta == "MRVKGIRRNYQHWWGWGTMLLGLLMICSATEKLWVTVYYGVPVWKEATTTLFCASDAKAY")

def test_get_seq_second():
    print("testing get_seq, second sequence")
    assert(test_obj.second_fasta == "MRVRGMQRNWQHLGKWGLLFLGILIICNAADNLWVTVYYGVPVWKEATTTLFCASDAKAY")

### hydro_precent
def test_hydro_percent_positive():
    assert(test_obj.hydro_percent("DDDDD") == 1)

def test_hydro_percent_negative():
    assert(test_obj.hydro_percent("LLLLL") == 0)

### hydro_score

# test residue vs underscore
def test_hydro_score_on_underscore():
    # highest distance is a residue to a gap
    assert(test_obj.hydro_score("A", "-") == 2)

# test phile to no-identical phile
def test_hydro_score_on_same_group_phile():
    assert(test_obj.hydro_score("D", "E") == 0.25)

# test on identical
def test_hydro_score_on_identical_residue():
    assert(test_obj.hydro_score("D", "D") == 0)

# test phobe vs phobe
def test_hydro_score_on_same_group_phobe():
    assert(test_obj.hydro_score("L", "Y") == 0.25)

# test on phile vs phobe
def test_hydro_score_on_opposite():
    assert(test_obj.hydro_score("D", "Y") == 1)

# a hydrophile vs a neutral residue
def test_phile_vs_neutral():
    assert(test_obj.hydro_score("D", "H") == 0.5)

# a hydrophobe vs a neutral residue
def test_phile_vs_neutral():
    assert(test_obj.hydro_score("L", "H") == 0.5)

# a neutral vs a neutral residue
def test_phile_vs_neutral():
    assert(test_obj.hydro_score("T", "H") == 0.25)
