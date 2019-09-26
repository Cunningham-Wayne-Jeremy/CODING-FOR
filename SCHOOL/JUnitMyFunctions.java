package testing;

import java.util.ArrayList;
import java.util.Arrays;
public class JUnitMyFunctions {

	public int IntSubtraction(int one, int two){
		return  one -  two;
	}
	public void PrintJTest(int n){
		for(int i = 0;i < n; i++){
			System.out.println("This is a JUnit test message");
		}
	}
	public String nullForJeremy(String name){
		if(name == "Jeremy"){
			return null;
		}
return name;
}
	public int square(int number){
		return number*number;
}
	public Object returnSameObject(Object obj){
		return obj;
}
	public void arrayIndexOutofBounds(){
		ArrayList<String> array = new ArrayList<String>(Arrays.asList("Littleton", "Boulder", "Rexburg"));
		System.out.println(array.get(5));		
}
}
