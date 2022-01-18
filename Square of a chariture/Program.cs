using System;

namespace Square_of_a_chariture
{
    class Program
    {
        //J Murphy
        //14/10/2021 (dd/mm/yyyy)
        //this program asks the user for a size of a square then asks the user for the chariture that the square should be filled by
        static void squareChar(int size, char fillChar)
        {
            for(int x = 0; x < size; x++)
            {
                
                for(int y=0; y < size-1; y++)
                {
                    Console.Write(fillChar);
                }
                Console.WriteLine(fillChar);
            }
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.WriteLine();
            Console.Write("please enter size of the square: ");
            int big =Int32.Parse( Console.ReadLine());
            Console.Write("please enter the filling chariture: ");
            char slim = char.Parse(Console.ReadLine());
            squareChar(big, slim);
        }
    }
}
