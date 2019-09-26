package testing;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
public class MVC_Controller {
private MVC_View theview;
private MVC_Model themodel;

public MVC_Controller (MVC_View theview, MVC_Model themodel){
	this.theview = theview;
	this.themodel = themodel;
	this.theview.addConvertListener(new ConvertListener());
	
}
class ConvertListener implements ActionListener{


	@Override
	public void actionPerformed(ActionEvent arg0) {
	
double inches = 0;
		
		inches = theview.getInches();
		themodel.Conversion(inches);
		theview.setCoversionSolution(themodel.getConversionValue());
	}
}
public class MVC_Conversion {


public void main(String[] args) {

	         

	        MVC_View theview = new MVC_View();

	         
	        MVC_Model themodel = new MVC_Model();

	         

	        
	         

	        theview.setVisible(true);

         

	    }

	}

}

