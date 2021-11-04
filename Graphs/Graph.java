import java.io.*;
import java.util.*;
import java.lang.*;

public class Graph{
    private int vertices;//no of vertices
    private LinkedList<Integer> adjList[];

    public Graph(int number){
        this.vertices = number;

        this.adjList = new LinkedList[vertices];

        for(int i=0; i<vertices; ++i){
            adjList[i] = new LinkedList<>();
        }
    }

    public void addEdge(int source, int dest){
        adjList[source].add(dest);
    }

    public int getVerticesCount(){
        return this.vertices;
    }

    public LinkedList<Integer>[] getAdjacencyList(){
        return adjList;
    }


    public static void main(String args[]){
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 3);
        g.addEdge(3, 0);

        LinkedList<Integer> aList[] = g.getAdjacencyList();

        for (LinkedList<Integer> vertex : aList) {

            for(Integer edge: vertex){
                System.out.println(edge);
            }
            
        }
    }
}