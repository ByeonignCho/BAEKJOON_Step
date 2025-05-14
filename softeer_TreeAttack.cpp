#include<bits/stdc++.h>
using namespace std;
int main(int argc, char** argv)
{
    int n;
    int m;
    cin >> n>>m;
    cin.ignore();
    string in;
    vector<vector<char>> matrix;
    vector<char> row;
    for (int p=0 ; p<n;p++){
        getline(cin,in);
        for(int i=0 ; i<in.size();i++){
            if (in[i]==' '){
                continue;
            }
            else{
                row.push_back(in[i]);
            }
        }
        matrix.push_back(row);
    }
    int L;
    int R;
    for (int k = 0; k<2;k++){
        cin >>L>>R;
        for (int j =0; j<5;j++){
            for (int it=0; it<m;it++){
                if (matrix[L-1+j][it] == '1'){
                    matrix[L-1+j][it] = '0';
                    break;
                    }
                else
                    continue; 
            }
        }
    } 
    int cnt = 0;
    for (int z = 0; z<n;z++){
        for (int x =0; x<m;x++){
            if (matrix[z][x] == '1'){
                    cnt++;
            }
        }
    }
    cout << cnt << endl;
   return 0;
}