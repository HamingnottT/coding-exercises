# Python

def subStrings(A,B):
    
    #this is default OUTPUT. You can change it.
    result=-404
    
    #write your Logic here:
    
    
    return result

#INPUT [uncomment & modify if required]
A=str(input())
B=str(input())

#OUTPUT [uncomment & modify if required]
print(subStrings(A,B))

# Scala

object Solution extends App {
    //INPUT [uncomment & modify if required]
	var pattern = scala.io.StdIn.readLine();
	var para = scala.io.StdIn.readLine();
	
	//write your Logic here
	
	
	//OUTPUT [uncomment & modify if required]
	//println(pattern)
	//println(para)
}

# Java

import java.util.*;
import java.lang.*;
import java.io.*;

public class Main 
{ 
	public static void substrings(String pattern,String[] lines)
	{
	    //this is default OUTPUT. You can change it.
		String present=new String("");
		int noofsubstring=-1;
		
		//write your Logic here:
		
		
		//OUTPUT [uncomment & modify if requires]
		System.out.println(present);
		if(present=="YES")
		{
			System.out.print(noofsubstring);
		}
		
	}

	public static void main(String[] args)
	{
		//INPUT [uncomment & modify if required]
        String[] lines=new String[100];
        String pattern=new String("");
		Scanner sc=new Scanner(System.in);
		int i=0;
		
		pattern=sc.nextLine();
		
		while(sc.hasNext()==true)
		{
			lines[i]=sc.nextLine();
			i++;
		}
        	
        sc.close();
		
        substrings(pattern,lines);
	}
}
