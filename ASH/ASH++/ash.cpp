#include <iostream>
#include <string>
#include <vector>
#include <map>              // for weights
#include <stdlib.h>         // for abs() function
#include "Entry.h"          // contains Entry class. Req for ash_utils
#include "ash_utils.h"      // contains ASH functions

using namespace std;


int main()
{
    string x = "CDSVVVHVLKLQGAVPFVHTNVPQSMFSYDCSNPLFGQTVNPWKSSKSPGGSSGGEGALI";
    string y = "TDATVVALLKGAGAIPLGITNCSELCMWYESSNKIYGRSNNPYDLQHIVGGSSGGEGCTL";
    int l = 15;
    vector <Entry> test_results = seq_to_seq(x,y,l);

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
