# Python

def specialSum(N, Arr,K):
    # this is default OUTPUT. You can change it.
    result = -404

    # write your Logic here:
    
    
    return result


# INPUT [uncomment & modify if required]

N = int(input())
temp = input().split()
Arr = []
for i in range(N):
    Arr.append(int(temp[i]))
K = int(input())

# OUTPUT [uncomment & modify if required]
print(specialSum(N, Arr,K))


# Scala

import java.io._
import scala.util.control.Breaks._
import scala.collection.immutable.Vector._

object Main 
{ 
    def specialSum(N: Int, Arr: Array[Int], K: Int): Int = {
        //this is default OUTPUT. You can change it.
        val result: Int = -404
        //write your LOGIC here:
        
        
        return result
    }
    
    def main(args: Array[String]) 
    {
        // INPUT [uncomment & modify if required]
	    val N: Int = scala.io.StdIn.readLine.toInt
        
        val Arr: Array[Int] = readLine.split(" ").map(_.toInt)
      
        val K: Int = scala.io.StdIn.readLine.toInt
        
        // OUTPUT [uncomment & modify if required]
        print(specialSum(N, Arr, K))
	}
}


# Java

import java.util.*;
import java.io.*;
import java.lang.Math;
 
public class Main
{
    public static int specialSum(int N,int[] Arr,int K) {
        
        //this is default OUTPUT. You can change it.
        int result = -404;

        //write your Logic here:
        
        
        return result;
    }
    public static void main (String[] args)
    {
        Scanner sc=new Scanner(System.in);
            
        //INPUT [uncomment & modify if required]
        int N = sc.nextInt();
        int[] Arr = new int[N];

        for(int i=0;i<N;i++){
            Arr[i]=sc.nextInt();
        }
        int K = sc.nextInt();
        sc.close();

        //OUTPUT [uncomment & modify if required]
        System.out.print(specialSum(N,Arr,K));
    }
}