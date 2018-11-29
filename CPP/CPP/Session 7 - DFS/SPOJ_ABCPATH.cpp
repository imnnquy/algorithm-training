//  Problem from SPOJ
//  http://www.spoj.com/problems/ABCPATH/

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int main()
{
    int t;
    vector<string> results = vector<string>();

    for(int i = 0; i < results.size() - 1; i++) {
        cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1];
    }
    return 0;
}

