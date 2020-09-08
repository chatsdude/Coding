/*Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
*/
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        str+=" ";
        map<char,string>Map;
        map<string,char>Map2;
        vector<string>s;
        string temp= "";
        int j = 0;
        for(int i = 0;i<str.size();i++){
            if(str[i] == ' ' || i == str.size() - 1){
                s.push_back(temp);
                temp = "";
                j++;
            }
            else temp +=str[i];
        }
        if (j != pattern.size())return false;
        
        for(int i = 0;i<pattern.size();i++){
            if (Map.count(pattern[i])){
                if(Map[pattern[i]] != s[i]){
                    return false;
                }
            }else{
                if (Map2.count(s[i])){
                    return false;
                }
                Map2[s[i]] = pattern[i];
                Map[pattern[i]] = s[i];
                
            }
        }
        return true;
    }
};
