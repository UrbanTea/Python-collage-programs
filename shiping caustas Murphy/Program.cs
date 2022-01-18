using System;

namespace shiping_caustas_Murphy
{
    class Program
    {
        //Murphy
        //20/09/2021 (dd/mm/yyyy)
        //Program asks for items(iterations) then then displays the shiping charge for each number of items upto the inputed number
        public static double RoundUp(double input, int places)
        {
            double multiplier = Math.Pow(10, Convert.ToDouble(places));
            return Math.Ceiling(input * multiplier) / multiplier;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.Write("Please input a number of iderations: ");
            int items = int.Parse(Console.ReadLine());
            double total = 0;
            for (int x = 1; x < items+1; x++)
            {
                total = 0;
                for (int i = 1; i < x + 1; i++)
                {
                    if (i < 2)
                    {
                        total += 2.99;
                        //Console.WriteLine(i+" 2.99");
                    }
                    else if (i >= 2 & i <= 5)
                    {
                        total += 1.99;
                        //Console.WriteLine(i+" 1.99");
                    }
                    else if (i > 5 & i < 15)
                    {
                        total += 1.49;
                        //Console.WriteLine(i+" 1.49");
                    }
                    else if (i >= 15)
                    {
                        total += .99;
                        //Console.WriteLine(i+" .99");
                    }
                    else
                    {
                        Console.WriteLine("==SOMETHING WENT WRONG==");
                    }

                }
                


                    Console.WriteLine("The shiping charges for " + x + " item(s) are " + "$" + RoundUp(total, 2));
                
            }
           
        }
    }
}
