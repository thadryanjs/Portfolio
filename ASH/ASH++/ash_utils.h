//#include "Entry.h"
using namespace std;


// the weights use for the algorith stored in a map
map <char, float> weight =
{
    {'L', -0.5}, {'A', -0.5}, {'F', -0.5}, {'Y', -0.5},
    {'W', -0.5}, {'I', -0.5}, {'V', -0.5}, {'H', -0.0},
    {'N', -0.0}, {'C', -0.0}, {'G', -0.0}, {'M', -0.0},
    {'Q', -0.0}, {'P', -0.0}, {'S', -0.0}, {'T', -0.0},
    {'D',  0.5}, {'E',  0.5}, {'R',  0.5}, {'K',  0.5}
};



// function that gets distance between two residues
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
    bit to make sense of is the for-loop. it ititerates through the
    sequences, and compares the resides at each index. If they match,
    it doesnothing. this allows fewer function calls and allows us to
    preserve the simple scale. Calling the scale on every pair results
    in residues in the same catagory being scored identically, even
    though they are not (D -> D, D -> E). they are similar but D -> E
    warrants some degree of mismatch while D -> is clearly identical  */

// function score the entire string
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



// function that gets a vector of custom Entry objects (see Entry.h)
// for each kmer in string as compared to its match in the other string
vector<Entry> seq_to_seq(string seq1, string seq2, int length)
{
    // empty vector of entry objects
    vector<Entry> results;

    // start at index 0
    int position = 0;

    // while incrementing won't exceed length of strings
    while( position + length <= seq1.length() ) {
        // collect substrings at each position
        string current_peptide = seq1.substr(position, length);
        string compare_peptide = seq2.substr(position, length);

        // call mismatch to score the two compare_peptides
        double entry = mismatch(current_peptide, compare_peptide);

        // create and Entry object capturing the score, position,
        // the sequence, and what it was compared to
        Entry results_obj = Entry
        (
                current_peptide,    // seq
                position,           // pos
                entry,              // score
                compare_peptide     // match
        );
        
        // capture the onject and advance the counter
        results.push_back(results_obj);
        position++;
    }
    return results;
}
