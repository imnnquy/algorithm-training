//  Problem from SPOJ
//  http://www.spoj.com/problems/ALLIZWEL/

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

string ALLIZZWELL = "ALLIZZWELL";
int AIW_LENGTH = 10;

int dx[] = {1, 0, -1, 0, 1, -1, 1, -1};
int dy[] = {0, -1, 0, 1, 1, -1, -1, 1};

bool dfs(int R, int C, vector<string> matrix, vector<vector<bool>> visited, int index, vector<int> position) {
    if(index >= AIW_LENGTH) {
        return true;
    }
    visited[position[0]][position[1]] = true;
    for(int i = 0; i < 8; i++) {
        int neighbor_x = dx[i] + position[0];
        int neighbor_y = dy[i] + position[1];
        if(neighbor_x >= 0 && neighbor_x < R && neighbor_y >= 0 && neighbor_y < C) {
            if(!visited[neighbor_x][neighbor_y] && matrix[neighbor_x].at(neighbor_y) == ALLIZZWELL[index]) {
                vector<int> nextPosition;
                nextPosition.push_back(neighbor_x);
                nextPosition.push_back(neighbor_y);
                if(dfs(R, C, matrix, visited, index+1, nextPosition)){
                    return true;
                }
            }
        }
    }

    return false;
}

string checkMatrix(int R, int C, vector<string> matrix) {
    for(int i = 0; i < R; i++) {
        for(int j = 0; j < C; j++){
            if(matrix[i].at(j) == 'A') {
                vector<vector<bool>> visited;
                for(int ii = 0; ii < R; ii++) {
                    visited.push_back(vector<bool>());
                    for(int jj = 0; jj < C; jj++) {
                        visited[ii].push_back(false);
                    }
                }
                vector<int> position;
                position.push_back(i);
                position.push_back(j);
                if(dfs(R, C, matrix, visited, 1, position)) {
                    return "YES";
                }
            }
        }
    }
    return "NO";
}

int main()
{
    int t;
    vector<string> results = vector<string>();
    cin >> t;
    for(int i = 0; i < t; i++) {
        int R, C;
        cin >> R;
        cin >> C;
        int column = C;
        vector<string> matrix;
        for(int i = 0; i < R; i++) {
            string row;
            cin >> row;
            matrix.push_back(row);
        }
        results.push_back(checkMatrix(R, C, matrix));
    }
    for(int i = 0; i < results.size() - 1; i++) {
        cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1];
    }
    return 0;
}

