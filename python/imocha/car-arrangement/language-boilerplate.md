# Python

def carArrangement(N, A):
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

# OUTPUT [uncomment & modify if required]
print(carArrangement(N,A))

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
  public static int carArrangement(int N,int[] A)
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
    
    sc.close ();

    //OUTPUT [uncomment & modify if required]
    System.out.print(carArrangement(N,A));
  }
}