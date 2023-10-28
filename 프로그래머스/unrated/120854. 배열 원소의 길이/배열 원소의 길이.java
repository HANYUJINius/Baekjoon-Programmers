import java.util.*;

class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int[strlist.length];
        int k=0;
        int len;
        for(int i = 0 ; i<strlist.length ; i++){
            len = strlist[i].length();
            answer[k++] = len;
        }
        return answer;
    }
}