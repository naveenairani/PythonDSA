class Solution {
public:
    string reverseVowels(string s) {
        vector<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int len = s.length();
        int left = 0, right = len -1;;
        while(left < right){
            if(find(vowels.begin(), vowels.end(), s[left])== vowels.end()){
                left++;
            }
            else if(find(vowels.begin(), vowels.end(), s[right]) == vowels.end()){
                right--;
            }
            else{
                swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};