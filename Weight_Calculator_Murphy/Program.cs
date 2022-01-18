using System;

namespace Weight_Calculator_Murphy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.Write("Please input BMI ");
            int bmi = Int32.Parse(Console.ReadLine());
            Console.WriteLine("");
            Console.Write("Please input number of feet in your hight: ");
            int feet = Int32.Parse(Console.ReadLine());
            Console.WriteLine("");
            Console.Write("Please input number of inches in your hight: ");
            int inch = Int32.Parse(Console.ReadLine());
            int height = (feet * 12) + inch;
            int weight = (int)(bmi * Math.Pow(height, 2) / 703);
            Console.WriteLine("your weight is: " + weight);
    }
    }
}
