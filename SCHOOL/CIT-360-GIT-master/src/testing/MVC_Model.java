package testing;

public class MVC_Model {
	//display phone number in text box!
	public double convertinchestofeet;
	
	public void Conversion(double inches){
		convertinchestofeet = inches *.083333;
		
		}

	public double getConversionValue(){
		return convertinchestofeet;
	}
}
