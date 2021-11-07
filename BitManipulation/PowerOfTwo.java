class PowerOfTwo {
    public boolean isPowerOfTwo(int n) {
       //Loop
        /*int count = 0;
        
        while(n > 0){
            if( (n & 1) == 1){
                if(count == 0){
                    count++;
                }else{
                    return false;
                }
            }
                
            n=n>>1;
        }
        
        if(count == 1)
            return true;
        
        return false;
        
        */
        
        //Recursion
        
        /*
        
        if(n <= 0)
            return false;
        if((n&1) == 1 ){
            if(n == 1)
                return true;
            return false;
        }
        
        return isPowerOfTwo(n>>1);
        */
        
        //without loop or Recursion
        
        if( n < 1 ) return false;
        return (n & n-1) == 0;
        
    }
}