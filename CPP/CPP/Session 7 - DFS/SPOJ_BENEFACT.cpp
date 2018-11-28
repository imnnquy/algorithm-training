//  Problem from SPOJ
//  http://www.spoj.com/problems/BENEFACT/

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int findMaximum(int places, vector<vector<vector<int>>> graph) {
    int maxiMum = 0;
    stack<vector<int>> s;
    vector<bool> visited;
    for(int i = 0; i <= places; i++) {
        visited.push_back(false);
    }
    vector<int> rootTree;
    rootTree.push_back(1);
    rootTree.push_back(0);
    s.push(rootTree);
    visited[1] = true;
    while(!s.empty()) {
        int u = s.top()[0];
        int currentLength = s.top()[1];
        s.pop();
        if(graph[u].size() == 0) {
            if(maxiMum < currentLength) {
                // cout << "Change max to: " << currentLength << endl;
                maxiMum = currentLength;
            }
        }
        for(int i = 0; i < graph[u].size(); i++) {
            int v = graph[u][i][0];
            int length = graph[u][i][1];
            if(!visited[v]) {
                vector<int> nextPoint;
                visited[v] = true;
                nextPoint.push_back(v);
                nextPoint.push_back(currentLength + length);
                s.push(nextPoint);
                // cout << "v: " << v << " currentLength: " << currentLength + length << endl;
            }
        }
    }
    return maxiMum;
}

int main()
{
    int t;
    vector<int> results = vector<int>();
    cin >> t;
    for(int i = 0; i < t; i++) {
        int places;
        cin >> places;
        vector<vector<vector<int>>> graph;
        for(int i = 0; i <= places; i++) {
            graph.push_back(vector<vector<int>>());
        }
        for(int i = 0; i < places - 1; i++) {
            int start, end, length;
            cin >> start >> end >> length;
            vector<int> endLength;
            endLength.push_back(end);
            endLength.push_back(length);
            graph[start].push_back(endLength);
        }
        results.push_back(findMaximum(places, graph));
    }
    for(int i = 0; i < results.size() - 1; i++) {
        cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1];
    }
    return 0;
}

