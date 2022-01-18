using System;

namespace Election_Statistics
{
    //murphy
    //21/09/2021(dd/mm/yyyy)
    //This program first asks how manny partys there are then it asks for each party's names and votes, then displays the partys name there votes out of the total then there percentage of votes
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("__________________________________");

            Console.Write("Pleas intput the number of Political Partys: ");
            int partys = Int32.Parse(Console.ReadLine());
            string[] PartysNames = new string[partys];
            double[] partysVotes = new double[partys];
            for(int i = 0; i < partys; i++)
            {
                Console.WriteLine("");
                if ((i + 1) % (10) == 1)
                {
                    Console.Write("Please input the " + (i + 1) + "st party's name: ");
                    PartysNames[i] = Console.ReadLine();
                    Console.Write("Please input the " + (i + 1) + "st party's number of votes: ");
                    partysVotes[i] = Int32.Parse(Console.ReadLine());
                }else if ((i + 1) % (10) == 2)
                {
                    Console.Write("Please input the " + (i + 1) + "nd party's name: ");
                    PartysNames[i] = Console.ReadLine();
                    Console.Write("Please input the " + (i + 1) + "nd party's number of votes: ");
                    partysVotes[i] = Int32.Parse(Console.ReadLine());
                }else if ((i + 1) % (10) == 3)
                {
                    Console.Write("Please input the " + (i + 1) + "ed party's name: ");
                    PartysNames[i] = Console.ReadLine();
                    Console.Write("Please input the " + (i + 1) + "ed party's number of votes: ");
                    partysVotes[i] = Int32.Parse(Console.ReadLine());
                }else 
                {
                    Console.Write("Please input the " + (i + 1) + "th party's name: ");
                    PartysNames[i] = Console.ReadLine();
                    Console.Write("Please input the " + (i + 1) + "th party's number of votes: ");
                    partysVotes[i] = Int32.Parse(Console.ReadLine());
                }
            }
            double total = 0;
            Array.ForEach(partysVotes, delegate (double i) { total += i; });
            Console.WriteLine("total number of votes is: " + total);
            for (int i = 0; i < partys; i++)
            {
                Console.WriteLine("");
                if ((i + 1) % (10) == 1)
                {
                    Console.WriteLine("The "+(i+1)+"st party's name is "+PartysNames[i]+" with "+partysVotes[i] +"/"+total+" votes or "+ Math.Round((partysVotes[i]/total ) *100) +"% of the vote");
                    
                    
                }
                else if ((i + 1) % (10) == 2)
                {
                    Console.WriteLine("The " + (i + 1) + "nd party's name is " + PartysNames[i] + " with " + partysVotes[i] + "/" + total + " votes or " + Math.Round((partysVotes[i] / total) * 100) + "% of the vote");
                }
                else if ((i + 1) % (10) == 3)
                {
                    Console.WriteLine("The " + (i + 1) + "ed party's name is " + PartysNames[i] + " with " + partysVotes[i] + "/" + total + " votes or " + Math.Round((partysVotes[i] / total) * 100) + "% of the vote");
                }
                else
                {
                    Console.WriteLine("The " + (i + 1) + "th party's name is " + PartysNames[i] + " with " + partysVotes[i] + "/" + total + " votes or " + Math.Round((partysVotes[i] / total) * 100) + "% of the vote");
                }
            }

        }
    }
    
}
