# Python

def mergedArray(N,A,B):
    #this is default OUTPUT. You can change it
    result=-404
    
    # WRITE YOUR LOGIC HERE:
    

    return result

#INPUT [uncomment & modify if required]
N=int(input())
A=[]
B=[]

temp=input().split()
for i in range(N):
    A.append(int(temp[i]))    

temp=input().split()
for j in range(N):
    B.append(int(temp[i]))
#OUTPUT [uncomment & modify if required]
print(mergedArray(N,A,B))

# Scala

object Solution extends App  { 
  def logicFuncn(X: Int): Int = {
    val result: Int = -404
    //write your LOGIC here:
    
    
    return result
  }


//INPUT [uncomment & modify if required]
    var Y: Int = scala.io.StdIn.readInt()
    
// OUTPUT [uncomment & modify if required]
    System.out.print(logicFuncn(Y))
}

# Java

import java.lang.*;
import java.io.*;
import java.util.*;

public class Main
{   
    public static int mergedArray(int N,int[] A,int[] B){
        //this is default OUTPUT. You can change it
        int result=-404;
        
        //WRITE YOUR LOGIC HERE:


        return result;
    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        //INPUT [uncomment & modify if required]
        int N=sc.nextInt();
        int[] A=new int[N];
        int[] B=new int[N];

        for(int i=0;i<N;i++){
            A[i]=sc.nextInt();
        }
        for(int i=0;i<N;i++){
            B[i]=sc.nextInt();
        }

        //OUTPUT [uncomment & modify if required]
        System.out.println(mergedArray(N,A,B));
    
    }
}