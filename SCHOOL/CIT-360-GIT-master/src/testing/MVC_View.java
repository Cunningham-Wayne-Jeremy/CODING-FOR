package testing;
import javax.swing.*;
import java.awt.event.ActionListener;
public class MVC_View extends JFrame{
	//text box and Buttons
	
	private JTextField inches = new JTextField(10);
	private JLabel convertlabel = new JLabel("Convert to Feet!");
	private JButton convertbutton = new JButton("Convert!");
	private JTextField conversionsolution = new JTextField(15);

	
	MVC_View(){
		JPanel conversionpanel = new JPanel();
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setSize(500,200);
		conversionpanel.add(inches);
		conversionpanel.add(convertlabel);
		conversionpanel.add(convertbutton);
		conversionpanel.add(conversionsolution);
	
		this.add(conversionpanel);
	}		
		public double getInches(){
			return Double.parseDouble(inches.getText());
		}
		
		public double getConversionSolution(){
			return Double.parseDouble(conversionsolution.getText());
		}
	
		public void setCoversionSolution(double conversion){
			conversionsolution.setText(Double.toString(conversion));
		}
		
	void addConvertListener(ActionListener listenforconvertbutton){
		convertbutton.addActionListener(listenforconvertbutton);
		
		
	}
}
