package com.company;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;
//j murphy
//23/09/2021
//this program first askes the user if they want to encrypt or decrypt a 4 digit number, then it eather encryts or decrypts the number
public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Revak rah daar rot los fah hi gein");
        System.out.println("__________________________________");
        System.out.println();
        System.out.println("would you like to encrypt or decrypt");
        System.out.println("1.encrypt");
        System.out.println("2.decrypt");
        int input = 0;
        while(input!=1||input!=2){
            input=in.nextInt();
            //encrypting
            if(input==1){
                String number="";
                while(number.length()!=4){
                    System.out.print("please input a number: ");
                    number=in.next();
                    if(number.length()!=4){
                        System.out.println("that number isn't 4 digits long.");
                    }
                }

                int[] anumber=new int[number.length()];

                for (int i = 0; i < number.length(); i++)
                {
                    anumber[i] = number.charAt(i) - '0';
                }
                for(int i=0;i<anumber.length;i++){
                    anumber[i]+=7;
                    anumber[i]%=10;
                }
                int temp=0;
                for(int x=0;x<2;x++) {
                    for (int i = 0; i < anumber.length; i++) {
                        if(i<anumber.length-1){
                            temp=anumber[i];
                            anumber[i]=anumber[i+1];
                            anumber[i+1]=temp;
                        }
                    }
                }
                String output="";
                for (int i=0;i<anumber.length;i++){
                    output+=Integer.toString(anumber[i]);
                }
                System.out.println(output);



//decrypting
            }else if(input==2){


                String number="";
                while(number.length()!=4){
                    System.out.print("please input a number: ");
                    number=in.next();
                    if(number.length()!=4){
                        System.out.println("that number isn't 4 digits long.");
                    }
                }

                int[] anumber=new int[number.length()];

                for (int i = 0; i < number.length(); i++)
                {
                    anumber[i] = number.charAt(i) - '0';
                }

                int temp=0;
                for(int x=0;x<2;x++) {
                    for (int i = 0; i < anumber.length; i++) {
                        if(i<anumber.length-1){
                            temp=anumber[i];
                            anumber[i]=anumber[i+1];
                            anumber[i+1]=temp;
                        }
                    }

                }

                for(int i=0;i<anumber.length;i++){
                    if(anumber[i]<7){
                        anumber[i]+=10;
                    }
                    anumber[i]-=7;

                }
                String output="";
                for (int i=0;i<anumber.length;i++){
                    output+=Integer.toString(anumber[i]);
                }
                System.out.println(output);
            }else{
                System.out.println("input not excepted, inputs can only be 1 or 2");
            }
        }

    }
}
