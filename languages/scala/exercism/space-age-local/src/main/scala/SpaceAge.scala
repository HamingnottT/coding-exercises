// format should be in (x.xx +- x.xx) - pending way to achieve this
import scala.math

object SpaceAge {
  def pow(x:Double, y:Double) = math.pow(x,y)
  // days to seconds - found by squaring 60 min to 60 sec, then multiplying the exponential product by 24 hours
  val secondsInEarthYear = 365.25 * ((pow(60,2)) * 24)

  // predefined year values
  val earthYear = 1.0
  val mercuryYear = 0.2408467
  val venusYear = 0.61519726
  val marsYear = 1.8808158
  val jupiterYear = 11.862615
  val saturnYear = 29.447498
  val uranusYear = 84.016846
  val neptuneYear = 164.79132

  def calcSpaceAge(seconds: Double, planetYear: Double): Double = {
    seconds / (secondsInEarthYear * planetYear)
  }

  def onEarth(seconds: Double): Unit = {
    calcSpaceAge(seconds, earthYear)
    // println(calcSpaceAge(seconds, earthYear))
  }

  def onMercury(seconds: Double): Unit = {
    calcSpaceAge(seconds, mercuryYear)
    // println(calcSpaceAge(seconds, mercuryYear))
  }

  def onVenus(seconds: Double): Unit = {
    calcSpaceAge(seconds, venusYear)
    // println(calcSpaceAge(seconds, venusYear))
  }
  
  def onMars(seconds: Double): Unit = {
    calcSpaceAge(seconds, marsYear)
    // println(calcSpaceAge(seconds, marsYear))
  }

  def onJupiter(seconds: Double): Unit = {
    calcSpaceAge(seconds, jupiterYear)
    // println(calcSpaceAge(seconds, jupiterYear))
  }

  def onSaturn(seconds: Double): Unit = {
    calcSpaceAge(seconds, saturnYear)
    // println(calcSpaceAge(seconds, saturnYear))
  }

  def onUranus(seconds: Double): Unit = {
    calcSpaceAge(seconds, uranusYear)
    // println(calcSpaceAge(seconds, uranusYear))
  }

  def onNeptune(seconds: Double): Unit = {
    calcSpaceAge(seconds, neptuneYear)
    // println(calcSpaceAge(seconds, neptuneYear))
  }

  // for debugging
  def main(args:Array[String]) : Unit = {
    onEarth(1000000000)
    onMercury(2134835688)
    onVenus(189839836)
    onMars(2.329871239E9)
    onJupiter(901876382)
    onSaturn(3.0E9)
    onUranus(3.210123456E9)
    onNeptune(8.210123456E9)
  }
}