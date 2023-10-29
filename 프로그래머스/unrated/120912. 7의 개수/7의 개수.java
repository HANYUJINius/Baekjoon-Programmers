class Solution {
    public int solution(int[] array) {
        int answer = 0;
        for(int i = 0 ; i< array.length ; i++){
            if(array[i] > 10){
                while(array[i] >0){
                    int n = array[i] % 10;
                    if(n == 7){
                        answer++;
                    }
                    array[i] = array[i] / 10;
                }
            }
            else if(array[i]== 7){
                answer++;
            }
        }
        return answer;
    }
}