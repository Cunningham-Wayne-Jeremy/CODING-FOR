package testing;

public class MVC_Conversion {


public static void main(String[] args) {

	         

	        MVC_View theview = new MVC_View();

	         
	        MVC_Model themodel = new MVC_Model();

	         

	        MVC_Controller theController = new MVC_Controller(theview,themodel);
	         

	        theview.setVisible(true);

         

	    }

	}
