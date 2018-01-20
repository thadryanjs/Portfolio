#include <iostream>
#include <string>
#include <vector>
#include <map>              // for weights
#include <stdlib.h>         // for abs() function
#include "Entry.h"          // contains Entry class. Req for ash_utils
#include "ash_utils.h"      // contains ASH functions

using namespace std;

int main(void)
{
    // two strings to analyze
    string x = "CDSVVVHVLKLQGAVPFVHTNVPQSMFSYDCSNPLFGQTVNPWKSSKSPGGSSGGEGALI";
    string y = "TDATVVALLKGAGAIPLGITNCSELCMWYESSNKIYGRSNNPYDLQHIVGGSSGGEGCTL";

    // desired kmer length
    int kmer = 15;
    vector <Entry> test_results = seq_to_seq(x, y, kmer);

    // iterate though vector of objects and display results
    // with a mistmatch score above, say, 4
    for( Entry item : test_results) {
        if (item.score > 4 ) {
            cout << item.pos << "\t";
            cout << item.seq << "\t";
            cout << item.score << "\t";
            cout << item.match << "\t" << endl;
        }
    }
return 0;
}
