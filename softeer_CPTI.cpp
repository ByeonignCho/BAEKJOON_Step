#include<bits/stdc++.h>
using namespace std;
// 12점 받음
int main(){
  int n ;
  int m;
  cin >> n >> m ;
  cin.ignore();
  string in_put ;
  vector<vector<int>> cptis;

  for (int i =0 ; i<n ; i++){
    getline(cin,in_put);
    vector<int> cpti;
    for (int k = 0; k < in_put.size() ; k++){
      int num = stoi(string(1,in_put[k]));
      cpti.push_back(num);
    }
     cptis.push_back(cpti);
  }
  
  
  int cnt = 0;
  for (int i = 0 ; i<n-1 ; i++){
    vector<int> row = cptis[i];

    for (int k = i+1; k<n;k++){
      int differ = 0;
      for (int j =0; j<m;j++){
  
        if (row[j]!= cptis[k][j]){
          differ++;
        }
        if ((j==m-1)&&(differ<3)){
        
          cnt++;
          
        }
      }
    }
  }
  cout << cnt <<endl;
  return 0;
}



