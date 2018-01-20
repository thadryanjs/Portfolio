using namespace std;

map <char, float> weight =
{
    {'L', -0.5}, {'A', -0.5}, {'F', -0.5}, {'Y', -0.5},
    {'W', -0.5}, {'I', -0.5}, {'V', -0.5}, {'H', -0.5},
    {'N', -0.0}, {'C', -0.0}, {'G', -0.0}, {'M', -0.0},
    {'Q', -0.0}, {'P', -0.0}, {'S', -0.0}, {'T', -0.0},
    {'D',  0.5}, {'E',  0.5}, {'R',  0.5}, {'K',  0.5}
};

// gets distance between two residues
double score_residues(char residue1, char residue2)
{
    // get absolute value
    float subscore = abs(weight[residue1] - weight[residue2]);
    // same type, no match (evaluated prior) gives smallest mismatch
    if ( subscore == 0 ) {
        return 0.25;
    }
    // or else just give the score
    else {
        return subscore;
    }
}

/*  This function will iterate though the sequences and score their
    mismatch using the scale and functions above. The only tricky
    bit to make sense of is the for-loop. it Ititerates through the
    sequences, and compares the resides at each index. If they match,
    it doesnothing. this allows fewer function calls and allows us to
    preserve the simple scale. Calling the scale on every pair results
    in residues in the same catagory being scored identically, even
    though they are not (D -> D, D -> E). they are similar but D -> E
    warrants some degree of mismatch while D -> is clearly identical  */

// score the entire string
double mismatch(string input_seq1, string input_seq2)
{
    double score = 0.0;

    // length of sequences for iterations
    int size = input_seq1.length();

    // perform iteration and scoring detailed above
    for ( int i = 0; i < size ; i++ ) {
        if ( input_seq1[i] == input_seq2[i] ) {
            score = score + 0.0;
        }
        else {
            // score the pair of residues in question
            score = score + score_residues(input_seq1[i], input_seq2[i]);
        }
    }
    return score;
}
