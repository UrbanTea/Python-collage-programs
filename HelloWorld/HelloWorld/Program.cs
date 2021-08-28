using System;

namespace HelloWorld
{
    class Program
    {
        static string output = "";
        static void fizzbuzz(int x,int y, string word)
        {
            if (x % y == 0)
            {
                output = output + word;
            }
            
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            for(int i = 0; i < 100; i++)
            {
                fizzbuzz(i, 3, "fizz");
                fizzbuzz(i, 5, "buzz");
                if (output == "")
                {
                    output = i.ToString();
                }
                Console.WriteLine(output);
                output = "";
            }
        }
    }
}
