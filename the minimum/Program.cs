using System;

namespace the_minimum
{
    class Program
    {
        //J Murphy
        //14/10/2021
        //this program asks the user for three numbers then it outputs the minimum number
        static void minimum3(double x, double y, double z)
        {
            Console.WriteLine(Math.Min(z, Math.Min(x, y)));
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.WriteLine();
            Console.Write("please input the first number: ");
            double num1 = double.Parse(Console.ReadLine());
            Console.Write("please input the second number: ");
            double num2 = double.Parse(Console.ReadLine());
            Console.Write("please input the third number: ");
            double num3 = double.Parse(Console.ReadLine());
            Console.Write("the smallest number is: ");
            minimum3(num1, num2, num3);
        }
    }
}
