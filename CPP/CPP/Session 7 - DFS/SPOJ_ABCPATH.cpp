//  Problem from SPOJ
//  http://www.spoj.com/problems/ABCPATH/

#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

int dx[] = {1, 0, -1, 0, 1, -1, 1, -1};
int dy[] = {0, -1, 0, 1, 1, -1, -1, 1};
vector<vector<bool>> visited;

char dfs(int H, int W, vector<string> matrix, char current, int position_x, int position_y) {
    if(current == 'Z') {
        return current;
    }
    char asciiCode = current;
    // cout << "Current char: " << asciiCode << endl;
    for (int i = 0; i < 8; i++) {
         int neighbor_x = dx[i] + position_x;
        int neighbor_y = dy[i] + position_y;
        if(neighbor_x >= 0 && neighbor_x < H && neighbor_y >= 0 && neighbor_y < W) {
            // cout << "Visisted: " << neighbor_x << " " << neighbor_y << ": " << visited[neighbor_x][neighbor_y] << endl;
            if(matrix[neighbor_x].at(neighbor_y) == current + 1 and !visited[neighbor_x][neighbor_y]) {
                visited[neighbor_x][neighbor_y] = true;
                // cout << "Next char at: " << neighbor_x << " " << neighbor_y << endl;
                char currentAsciiCode = dfs(H, W, matrix, current + 1, neighbor_x, neighbor_y);
                if (currentAsciiCode > asciiCode) {
                    asciiCode = currentAsciiCode;
                    // cout << "current max: " << asciiCode << endl;
                }
            }
        }
    }

    return asciiCode;
}

string calcMax(int index, int H, int W, vector<string> matrix) {
    int longestPath = 0;
    visited = vector<vector<bool>>();
    for(int i = 0; i < H; i++) {
        visited.push_back(vector<bool>());
        for(int j = 0; j < W; j++) {
            visited[i].push_back(false);
        }
    }
    for(int i = 0; i < H; i++) {
        for(int j = 0; j < W; j++) {
            if(matrix[i].at(j) == 'A') {
                // cout << "A at: " << i << " " << j << endl;
                visited[i][j] = true;
                int currentLong = dfs(H, W, matrix, 'A', i, j);
                if (currentLong > longestPath) {
                    longestPath = currentLong;
                }
            }
        }
    }
    return "Case " + to_string(index) + ": " + to_string(longestPath - 64 > 0 ? longestPath - 64 : 0);
}

int main()
{
    int t;
    vector<string> results = vector<string>();
    int caseIndex = 1;
    while(true) {
        int H, W;
        cin >> H >> W;
        // cout << H << W << endl;
        if (H == 0 || W == 0) {
            break;
        }
        
        vector<string> matrix;
        for(int i = 0; i < H; i++) {
            string row;
            cin >> row;
            // cout << row << endl;
            matrix.push_back(row);
        }
        results.push_back(calcMax(caseIndex++, H, W, matrix));
    }

    for(int i = 0; i < results.size() - 1; i++) {
        cout << results[i] << std::endl;
    }
    if (results.size() > 0) {
        cout << results[results.size() - 1];
    }
    return 0;
}

