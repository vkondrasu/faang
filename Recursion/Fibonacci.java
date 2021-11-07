import java.io.*;
import java.util.Date;

public class Fibonacci{

    public long recursiveFib(int n){
        
        if(n <= 1){
            return 1;
        }
        
        return n * recursiveFib(n-1);
    }

    public long tailRecursiveFib(int n, long fibSofar){
        if(n == 1){
            return fibSofar;
        }
        
        return tailRecursiveFib(n-1, fibSofar*n);
    }

}


class Solution{

    public static void main(String[] args){
        Fibonacci f = new Fibonacci();

        int n = Integer.parseInt(args[0]);

        System.out.println(n);

        Date d1 = new Date();
        System.out.println( f.recursiveFib(n) );
        Date d2 = new Date();

        System.out.println("Recursive took : " + (d2.getTime()-d1.getTime()));

        d1 = new Date();
        System.out.println( f.tailRecursiveFib(n, 1 ) );
        d2 = new Date();

        System.out.println("Tail Recursive took : " + (d2.getTime()-d1.getTime()));
    }
    
}