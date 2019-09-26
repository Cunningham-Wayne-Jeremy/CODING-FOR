package testing;
import java.util.*;
public class Main_App {
private static Scanner input;

public static void main(String[] args){
	
		input = new Scanner(System.in);
		Integer input1;
		Integer input2;
		String operator;
		
		System.out.println("Enter an integer:");
				input1 = Integer.parseInt(input.nextLine());
		
		System.out.println("Enter another integer:");
				input2 = Integer.parseInt(input.nextLine());
				
		System.out.println("What type of calculation Addition '+', Subrtaction '-', Division '/' or Miltiplication '*'?:");
				operator = input.nextLine();
				
		System.out.println("The result is");
		//calling the calculate new appcontroller 
		AppController.controls(operator,input1,input2);

	
}
}
