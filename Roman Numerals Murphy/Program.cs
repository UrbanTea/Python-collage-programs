﻿using System;

namespace Roman_Numerals_Murphy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.WriteLine();
            string input="";
            int number;
            int num=0;



            while (num == 0)
            {
                

                Console.Write("please input a number between 1 and 10: ");
                input = Console.ReadLine();
                if (Int32.TryParse(input, out number) == true) { num = Convert.ToInt32(input); } else { num = 0; }
                switch (input)
                {
                    case "1":
                        Console.WriteLine("I");
                        break;
                    case "2":
                        Console.WriteLine("II");
                        break;
                    case "3":
                        Console.WriteLine("III");
                        break;
                    case "4":
                        Console.WriteLine("IV");
                        break;
                    case "5":
                        Console.WriteLine("V");
                        break;
                    case "6":
                        Console.WriteLine("VI");
                        break;
                    case "7":
                        Console.WriteLine("VII");
                        break;
                    case "8":
                        Console.WriteLine("VIII");
                        break;
                    case "9":
                        Console.WriteLine("IX");
                        break;
                    case "10":
                        Console.WriteLine("X");
                        break;

                    default:
                        Console.WriteLine("the input is not a number between 1 and 10");
                        num = 0;
                        break;
                }
            }
        }
    }
}
