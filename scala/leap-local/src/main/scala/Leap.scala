object Leap {
  def leapYear(year: Int): Boolean = {

      def divisibleBy(i: Int): Boolean = {
        year % i == 0
      }

    /* because there are 366 days in a leap year there needs to be a something to account for divisibility */
      if (divisibleBy(400)) {
        true
      } else if (divisibleBy(100) && divisibleBy(400)) { //for years both divisible by 100 and 400
        true
      } else if (divisibleBy(100) && !divisibleBy(400)) {
        false
      } else if (divisibleBy(4)) {
        true
      } else {
        false
      }
  }

//  def main(args: Array[String]): Unit ={
//    println(
//      leapYear(2015),
//      leapYear(1996),
//      leapYear(2100),
//      leapYear(2000),
//      leapYear(16),
//      leapYear(4000)
//      )
//  }
}
