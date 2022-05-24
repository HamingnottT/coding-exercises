import scala.io.StdIn.readLine
import scala.annotation.tailrec

object PaintersDilemma1 {

    // def watercolor(n: Int, accumulator: Int): Int = {
    //     if (n < 2) accumulator
    //     else watercolor(n - 2, n + accumulator)
    // }

    // def watercolor(n: Int): Int = {
    //     @tailrec
    //     def watercolorHelper(i: Int, accumulator: Int): Int = {
    //         if (i < 2) accumulator
    //         else watercolorHelper(i - 2, i + accumulator)
    //     }
    //     watercolorHelper(n, 0)
    // }

    def paintersDilemma(t: Int, n: List): Unit = {
       println(n)
       println(t)
    }


    def main(args: Array[String]): Unit = {
        paintersDilemma(2, (2, 3))
    }
}