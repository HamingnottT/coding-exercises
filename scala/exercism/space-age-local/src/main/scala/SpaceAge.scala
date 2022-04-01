// format should be in (x.xx +- x.xx) - pending way to achieve this
import scala.math

object SpaceAge {
  def pow(x:Double, y:Double) = math.pow(x,y)

  def onEarth(seconds: Double): Unit = {

    // days to seconds - found by squaring 60 min to 60 sec, then multiplying the exponential product by 24 hours
    val secondsInYear = 365.25 * ((pow(60,2)) * 24)

    // format the result to return rounded double
    // val solution = "%.2f".format(seconds/secondsInYear).toDouble
    val solution = seconds/secondsInYear

    print(solution)
  }

//   def main(args:Array[String]) : Unit = {
//     onEarth(1000000000)
//   }
}