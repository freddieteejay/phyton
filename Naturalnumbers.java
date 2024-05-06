import java.util.Scanner;
public class Naturalnumbers{
public static void main(String... args){
Scanner freddie = new Scanner(System.in);


int largest = 0;
int smallest = 0;

System.out.print("How many numbers do you want to enter? ");
int numbersOfTimes = freddie.nextInt();


for (int i = 1; numbersOfTimes >= i; i++){

System.out.println("Enter numbers : " + i);
int num = freddie.nextInt();


if (num > i ){
largest = num;
}
 else if (num > num){
smallest = num;
}
System.out.println("largest "+ largest);
System.out.println("Smallest "+ smallest);

}


}



}






} 