#include <iostream>
#include <string>

using namespace std;

// class for results of ASH
class Entry
{
    public:

        // seq itself as kmer
        string seq;

        // where in the sull seq it is located
        int pos;

        // what score it is given by the algorith
        double score;

        // kmer in second sequence it was compared to
        string match;

        // constructor to set values from within program
        Entry(string iseq, int ipos, double iscore, string imatch)
        {
            seq = iseq;
            pos = ipos;
            score = iscore;
            match = imatch;
        }
};
