import java.util.Scanner;
public class DiscountJ{
public static void main(String[] args){
Scanner freddie = new Scanner(System.in);


System.out.print("Enter price: ");
int price = freddie.nextInt();

double discount =(double)10 / 100;
double X =price * discount;
double New = price - X;
System.out.printf("the discount is %.2f%n", New);


}

}