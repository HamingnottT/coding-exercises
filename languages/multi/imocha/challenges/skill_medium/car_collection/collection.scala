// working demo using scala

import java.io._
import scala.util.control.Breaks._
import scala.collection.immutable.Vector._

object Main{
    def carCollection(N: Int,X: Array[Int],K: Int,M: Array[Int]): String = {
        var result = ""
        var count = 0
        for (i <- 0 to K - 1) {  // Loop through each of the months (the M array)
            count = 0  // Initialize the count for this month
            for (j <- 0 to N - 1)  // Loop through each of the showrooms (the X array)
                if (X(j) <= M(i))  // Count the showrooms which are less than or equal to this month's coins
                    count += 1
            if (result == "")  // Add the count to the result string
                result += count
            else
                result += " " + count
        }
        result  // Return the result
    }

    def main(args: Array[String]): Unit =
    {
        //INPUT [uncomment & modify if required]
        var N: Int = scala.io.StdIn.readLine.toInt
		var X: Array[Int]=readLine.split("\n").map(_.toInt)
	    var K: Int = scala.io.StdIn.readLine.toInt
		var M: Array[Int]=readLine.split("\n").map(_.toInt)
	

        // OUTPUT [uncomment & modify if required]
        println(carCollection(N,X,K,M))

    }
}