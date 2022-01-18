package com.company;

import java.security.SecureRandom;
import java.util.Scanner;
//j Murphy
//06/10/2021(dd/mm/yyyy)
//this program generates a question then respawnds the user if there answer is correct or incorrect.
public class Main {
    public static SecureRandom random = new SecureRandom();
    public static int anwserNum=0;
    public static int numOfQuestions =10;
    public static void GenerateQuestion(){
        int x=random.nextInt(10);
        int y= random.nextInt(10);
        System.out.println();
        System.out.println("what is "+x+" times "+y);
        anwserNum=x*y;
        System.out.println(anwserNum);
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Revak rah daar rot los fah hi gein");
        System.out.println("__________________________________");
        System.out.println();
        int guess=0;

        for(int i=0;i<numOfQuestions;i++){
            boolean correct=false;
            if(guess!=-1) {
                GenerateQuestion();

            }
            while(guess !=-1&&correct==false){
                System.out.println("Enter your answer(-1 to exit): ");
                 guess=input.nextInt();
                 if(guess==anwserNum){
                     switch (random.nextInt(5)){
                         case 1:
                             System.out.println("very nice");
                             break;
                         case 2:
                             System.out.println("good work");
                             break;
                         case 3:
                             System.out.println("thats correct");
                             break;
                         case 4:
                             System.out.println("looks good");
                             break;
                         default: System.out.println("nice job");
                             break;

                     }
                     correct=true;
                 }else{
                     switch (random.nextInt(5)) {
                         case 1:
                             System.out.println("Incorrect try again");
                             break;
                         case 2:
                             System.out.println("thats not correct");
                             break;
                         case 3:
                             System.out.println("Thats not right");
                             break;
                         case 4:
                             System.out.println("try again");
                             break;
                         default:
                             System.out.println("Incorrect");
                             break;
                     }
                 }
            }
            System.out.println((i+1)+"/"+numOfQuestions);
        }
    }
}
