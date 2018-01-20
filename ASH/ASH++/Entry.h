#include <iostream>
#include <string>

using namespace std;

class Entry
{
    public:
        string seq;
        int pos;
        double score;
        string match;

        Entry(string iseq, int ipos, double iscore, string imatch)
        {
            seq = iseq;
            pos = ipos;
            score = iscore;
            match = imatch;
        }
};
