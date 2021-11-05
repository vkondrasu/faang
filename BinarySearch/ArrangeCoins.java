class ArrangeCoins {
    public int arrangeCoins(int n) {
        
        long left = 0, right = n;
        long mid;
        long filling;
        
        while(left <= right){
            mid = left + (right-left)/2;
            
            filling = mid * (mid+1)/2;
            
            if(filling == n)
                return (int)mid;
            if(filling < n)
                left = mid+1;
            else
                right = mid-1;
        }
        
        return (int)right;
        
    }

    
}

class Solution{
    public static void main(String[] args){
        ArrangeCoins coinsObject = new ArrangeCoins();
        System.out.println(coinsObject.arrangeCoins(Integer.parseInt(args[0])));
    }
}