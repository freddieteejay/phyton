import java.util.Scanner;
public class PassMarkDeterminator{
public static void main(String... args){
Scanner input = new Scanner(System.in);

int pass = 0;
int fail = 0;
for(int i = 1; i <= 15; i++){
System.out.print("Enter student score"); 
int userInput = input.nextInt();

if(userInput >= 45){
pass =  pass + 1;
}
else{
fail = fail + 1;
}

}
System.out.print("passed : " + pass);
System.out.print("\nfailed : " + fail);





}
}