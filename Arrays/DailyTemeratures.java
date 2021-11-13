//LC739

class Solution {
    public int[] DailyTemeratures(int[] temperatures) {
        
        int n = temperatures.length;
        int result[] = new int[n];
        result[n-1] = 0;
        int j = 0;
        
        for(int i = n-2; i >= 0; --i){
            j = i+1;
            
            while(true){
                if(temperatures[j] > temperatures[i]){
                    result[i] = j-i;
                    break;
                }else if(result[j] == 0){
                    break;
                }else{
                    j = j+result[j];
                }
            }
            
        }
        
        return result;
        
    }
}