using System;

namespace smallest_number
{
    class Program
    {
        //j Murphy
        //04/10/2021(dd/mm/yyyy)
        //the program asks for the amount of numbers, then is asks for the numbers, then the program outputs the smallest number
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");
            Console.Write("Please input the number of inputs: ");
            int[] inputs = new int[Int32.Parse(Console.ReadLine())];
            int smallest_number=0;
            for(int i = 0; i < inputs.Length; i++)
            {
                Console.Write("Please input Number " + (i+1) + ": ");
                inputs[i] = Int32.Parse(Console.ReadLine());
                if (i == 0)
                {
                    smallest_number = inputs[i];
                }else if (inputs[i] < smallest_number)
                {
                    smallest_number = inputs[i];
                }
            }
            Console.Write("out of the numbers " );
            Console.WriteLine("[{0}]", string.Join(", ", inputs));
            Console.WriteLine(smallest_number + " Was the smallest");
        }
    }
}
