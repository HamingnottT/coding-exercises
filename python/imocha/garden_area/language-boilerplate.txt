# Python

def gardenArea(N, M, A):
    # this is default OUTPUT. You can change it.
    result = -404

    # write your Logic here:

    return result


# INPUT [uncomment & modify if required]
N, M = input().split()
N = int(N)
M = int(M)

A = []
for i in range(N):
    a = []
    temp = input().split()
    for j in range(M):
        a.append(int(temp[j]))
    A.append(a)
# OUTPUT [uncomment & modify if required]
print(gardenArea(N, M, A))

# Scala

object Solution extends App {
	//INPUT [uncomment & modify if required]
	var sampleInput = scala.io.StdIn.readLine();
	var result = -404;
	//write your Logic here:

	//OUTPUT [uncomment & modify if required]
	System.out.println(result);
	
}

# Java

import java.util.*;
import java.io.*;
import java.lang.Math;
 
public class Main 
{
    public static int gardenArea(int N,int M,int[][] A){
        
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
        int M = sc.nextInt();
        
        int[][] A = new int[N][1000];
        for (int i = 0; i < N; i++)  
        {
            for (int j = 0; j < M; j++)
            {
                A[i][j] = sc.nextInt();
            }
        }
        sc.close();

        //OUTPUT [uncomment & modify if required]
        System.out.print(gardenArea(N,M,A));
    }
}