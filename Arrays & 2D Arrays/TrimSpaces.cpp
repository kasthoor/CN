#include <bits/stdc++.h>
using namespace std;

int main(){
    string s = "abc def g hi";

    string ans;
    for(int i=0;i<s.size();i++){
        if(s[i] != ' '){
            ans.push_back(s[i]);
        }
    }

    cout << "Output :"<< ans<< endl;
    return 0;
}