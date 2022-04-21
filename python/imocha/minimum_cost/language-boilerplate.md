# Python

def getMinCost(N, X, A, B):
    
    #this is default OUTPUT. You can change it.
    result=-404
    
    #write your Logic here:
    
    
    return result

#INPUT [uncomment & modify if required]
N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#OUTPUT [uncomment & modify if required]
print(getMinCost(N, X, A, B))

# Scala

import java.io._
import scala.util.control.Breaks._
import scala.collection.immutable.Vector._

object Main 
{ 
    def getMinCost(N: Int,X: Int, A: Array[Int], B: Array[Int]): Int = {
        //this is default OUTPUT. You can change it.
        val result: Int = -404
        
        //write your LOGIC here:
        
        
        return result
    }
    
    def main(args: Array[String]) 
    {
        // INPUT [uncomment & modify if required]
	    val N: Int = scala.io.StdIn.readLine.toInt
	    val X: Int = scala.io.StdIn.readLine.toInt
        
        val A: Array[Int] = readLine.split(" ").map(_.toInt)
        val B: Array[Int] = readLine.split(" ").map(_.toInt)

        // OUTPUT [uncomment & modify if required]
        print(getMinCost(N,X,A,B))
	}
}

# Java

import java.util.*; 
import java.lang.*;
import java.io.*;
import java.lang.Math;

public class Main {
    public static int getMinCost(int N, int X, int[] A, int[] B) {
        
        //this is default OUTPUT. You can change it.
        int result=-404;
        
        //write your Logic here:
        
        
        return result;
    }
    public static void main(String[] args) {
        // INPUT [uncomment & modify if required]
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int[] A = new int[N];
        int[] B = new int[N];
        for(int i=0; i<N; i++) {
            A[i] = sc.nextInt();
        }
        for(int i=0; i<N; i++) {
            B[i] = sc.nextInt();
        }
        
        // OUTPUT [uncomment & modify if required]
        System.out.print(getMinCost(N, X, A, B));
        sc.close();
    }
}