# Python

def gameWinner(N, A, B):
    # this is default OUTPUT. You can change it.
    result = -404

    # write your Logic here:

    return result


# INPUT [uncomment & modify if required]

N = int(input())

temp = input().split()
A = []
for i in range(N):
    A.append(int(temp[i]))

temp_1 = input().split()
B = []
for i in range(N):
    B.append(int(temp_1[i]))

# OUTPUT [uncomment & modify if required]
print(gameWinner(N, A, B))

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
  public static int gameWinner(int N,int[] A, int[] B)
  {

    //this is default OUTPUT. You can change it.
    int result = -404;

    //write your Logic here:


      return result;
  }
  public static void main (String[]args)
  {
    Scanner sc = new Scanner (System.in);

    //INPUT [uncomment & modify if required]
    int N = sc.nextInt ();

    int[] A = new int[N];
    for (int i = 0; i < N; i++)
    {
        A[i] = sc.nextInt ();
    }
    
    int[] B = new int[N];
    for (int i = 0; i < N; i++)
    {
        B[i] = sc.nextInt ();
    }
    
    sc.close ();

    //OUTPUT [uncomment & modify if required]
    System.out.print(gameWinner(N,A,B));
  }
}