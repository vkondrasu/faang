import java.io.*;

public class PathCompression{

    int root[];
    public PathCompression(int size){
        root = new int[size];

        for(int i = 0; i<size; ++i){
            root[i] = i;
        }
    }

    public int find(int x){
        if(x == root[x]){
            return x;
        }

        return root[x] = find(root[x]);
    }

    public void union(int x, int y){
        int root_x = find(x);
        int root_y = find(y);

        if(root_x != root_y){
            root[root_y] = root_x;
        }
    }


    public boolean connected(int x, int y){
        return find(x) == find(y);
    }


    public static void main(String[] args){
        PathCompression uf = new PathCompression(10);

        uf.union(1, 2);
        uf.union(2, 5);
        uf.union(5, 6);
        uf.union(6, 7);
        uf.union(3, 8);
        uf.union(8, 9);
        System.out.println(uf.connected(1, 5)); // true
        System.out.println(uf.connected(5, 7)); // true
        System.out.println(uf.connected(4, 9)); // false
        // 1-2-5-6-7 3-8-9-4
        uf.union(9, 4);
        System.out.println(uf.connected(4, 9)); // true
    }
} 