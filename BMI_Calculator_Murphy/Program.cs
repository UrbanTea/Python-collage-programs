using System;

namespace BMI_Calculator_Murphy
{
    //Murphy
    //21/09/2021 (dd/mm/yyyy)
    //This program asks for the users weight in pounds then there height in inchs then gives the user ther bmi
   
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.Write("Please input weight in pounds: ");
            int weight = Int32.Parse(Console.ReadLine());
            Console.WriteLine("");
            Console.Write("Please input number of feet in your hight: ");
            int feet = Int32.Parse(Console.ReadLine());
            Console.WriteLine("");
            Console.Write("Please input number of inches in your hight: ");
            int inch = Int32.Parse(Console.ReadLine());
            int height = (feet * 12) + inch;
            int bmi = (int)((weight*703)/Math.Pow(height,2));
            if (bmi < 18.5)
            {
                Console.WriteLine("Your BMI is " + bmi + " which is underweight");
            }else if (bmi >= 18.5 & bmi < 25)
            {
                Console.WriteLine("Your BMI is " + bmi + " which is normal weight");
            }else if (bmi >= 25)
            {
                Console.WriteLine("Your BMI is " + bmi + " which is overwight");
            }
            Console.WriteLine("");
            Console.WriteLine("Underweight = <18.5");
            Console.WriteLine("Normal = >=18.5 to <25");
            Console.WriteLine("Overweight = >=25");
        }
    }
    
}
