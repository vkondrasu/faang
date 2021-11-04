import java.io.*;

public class UnionByRank{

    int root[];
    int rank[];

    public UnionByRank(int size){
        root = new int[size];
        rank = new int[size];

        for(int i = 0; i<size; ++i){
            root[i] = i;
        }
    }

    public int find(int x){
        if(x == root[x]){
            return x;
        }

        return find(root[x]);
    }

    public void union(int x, int y){
        int root_x = find(x);
        int root_y = find(y);

        if(root_x != root_y){
            if(rank[root_x] > rank[root_y]){
                root[root_y] = root_x;
            }else if(rank[root_x] < rank[root_y]){
                root[root_x] = root_y;
            }else{
                root[root_x] = root_y;
                rank[root_y] += 1;
            }
            
        }
    }


    public boolean connected(int x, int y){
        return find(x) == find(y);
    }


    public static void main(String[] args){
        UnionByRank uf = new UnionByRank(10);

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