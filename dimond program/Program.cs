using System;

namespace dimond_program
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("----------------------------------");
            Console.WriteLine("");
            int lines=0 ;
            while (lines % 10 != 1&&lines<1&&lines>19)
            {
                Console.Write("please input a number of lines from 1 to 19:");
                lines = Int32.Parse(Console.ReadLine());
                if(lines % 10 == 0 && lines < 1 && lines > 19)
                {
                    Console.WriteLine("invalid input");
                }
            }
            for(int i = 0; i < lines/2; i++)
            {
                for (int x = 0; x< (lines-1) / 2; x++){
                    Console.Write(" ");
                }
                for(int y = 0; y < i; y++)
                {
                    Console.Write("*");
                }
                for (int x = 0; x < (lines - 1) / 2; x++)
                {
                    Console.Write(" ");
                }

            }

        }
    }
}
