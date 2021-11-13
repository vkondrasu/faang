import java.util.*;
import java.lang.*;
import java.io.*;

class DailyTemperatures {
    public int[] dailyTemperatures(int[] temperatures) {
        
        int n = temperatures.length;
        int result[] = new int[n];
        
        Stack<Integer> s = new Stack();
        s.push(0);
        
        for(int i=1; i<n; ++i){
            
            while(!s.empty()){
                if(temperatures[s.peek()] < temperatures[i]){
                    result[s.peek()] = i-s.peek();
                    s.pop();
                }else{
                    
                    break;
                }
            }
            s.push(i);        
        }
        
        while(!s.empty()){
            result[s.pop()] = 0;
        }
        
        return result;
        
    }
}