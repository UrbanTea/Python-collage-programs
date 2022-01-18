using System;

namespace Exam_Score_Program_Murphy
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Revak rah daar rot los fah hi gein");
            Console.WriteLine("----------------------------------");
            Console.WriteLine("");
            Console.Write("Please input the number of exams:");
            int numOfExams = Int32.Parse(Console.ReadLine());
            int[] Scores = new int[numOfExams];
            double averageScore = 0;
            Console.WriteLine("There are "+ numOfExams+ " Number of exams.");
            for(int i = 0; i < numOfExams; i++)
            {
                Console.Write("Please input percent score for exam #" + (i+1)+":");
                Scores[i] = Int32.Parse(Console.ReadLine());
            }
            for (int i = 0; i < numOfExams; i++)
            {
                Console.WriteLine("Exam #" + (i + 1)+":"+Scores[i]+"%");
                if (i > 0)
                {
                    averageScore = (averageScore + Scores[i]) / 2;
                }
                else
                {
                    averageScore = Scores[0];
                }
            }
            Console.WriteLine("Average exam score:" + averageScore+"%");
        }
    }
}
