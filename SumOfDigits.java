import java.util.Scanner;

public class SumOfDigits{
public static void main(String... args){
Scanner scanner = new Scanner(System.in);

System.out.print("Enter a number between 0 and 1000 : ");
int userInput1 = scanner.nextInt();
int digitOne = userInput1 % 10;

int userInput2 = userInput1 / 10;
int  digitTwo = userInput2 % 10;

int userInput3 = userInput2 / 10;
int digitThree = userInput3 % 10;

int sumOfDigits = digitOne + digitTwo + digitThree;
System.out.print("  ");
System.out.printf("The sum of digits in %d is : %d", userInput1, sumOfDigits);


}
}