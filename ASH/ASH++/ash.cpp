#include <iostream>
#include <string>
#include <stdlib.h>     //abs
#include <map>
#include "ash_utils.h"

using namespace std;


int main()
{
    string seq1 = "PEPTYDE";
    string seq2 = "PEPTIDE";

    double ans = mismatch(seq1, seq2);
    cout << ans << endl;

return 0;
}
