using System;

namespace Shapes_areas_Murphy
{
    //j murphy
    //23/09/2021 (dd/mm/yyyy)
    //this program first gives the user a choice between a circle, a rectangle, and a cyliender, then it asks for the spesific mesurements, then it returns the area
    class Program
    {
        public static double RoundUp(double input, int places)
        {
            double multiplier = Math.Pow(10, Convert.ToDouble(places));
            return Math.Ceiling(input * multiplier) / multiplier;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");

            Console.WriteLine("this program alows you to calculate the area of a circle, the area of a rectangle, and the area of a cylinder.");
            Console.WriteLine("first I will ask you if you want to find the area of a circle, rectangle, or a cylinder ");
            Console.WriteLine();
            Console.WriteLine("circle=C");
            Console.WriteLine("rectangle=R");
            Console.WriteLine("cylender=Y");
            string shape = Console.ReadLine();
            shape = shape.ToUpper();
            if (shape == "C")
            {
                Console.Write("please input the radius of the circle: ");
               double radius = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("the area is: " + RoundUp(Math.PI * Math.Pow(radius, 2),2));
            }else if (shape == "R")
            {
                Console.Write("please input the length of the rectangle: ");
                double length = Convert.ToDouble(Console.ReadLine());
                Console.Write("please input the width of the rectangle: ");
                double width = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("the area of the rectangle is: " + RoundUp(length * width,2));

            }else if (shape == "Y")
            {
                Console.Write("please input the radius of the cylender's semicircles: ");
                double radius = Convert.ToDouble(Console.ReadLine());
                Console.Write("please input the height of the Cylender: ");
                double height = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("the Surface area of the cylinder is: " + RoundUp((2 * Math.PI * radius * height + Math.PI * Math.Pow(radius, 2)), 2));
            }


        }
    }
}
