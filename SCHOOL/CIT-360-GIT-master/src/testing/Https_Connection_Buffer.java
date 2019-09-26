package testing;
import java.net.*;
import java.io.*;
public class Https_Connection_Buffer {

		//For the sake of simplicity I did a throw statement
		public static void main(String[] args) throws Exception{
			//Creates an object that will attempt to retrieve the data
			//https is necessary to connect
			URL webpagename = new URL("https://www.lds.org");
			
			//creates the connection to said web page
			HttpURLConnection testconnection = (HttpURLConnection) webpagename.openConnection();
			//establish connection buffer and prep it to display
			BufferedReader displaydata = new BufferedReader(new InputStreamReader(testconnection.getInputStream()));
			//here is the string object that the data will display in
			String ldscode;
			//loop while there is data left and display in the string
			while((ldscode = displaydata.readLine())!= null){
				System.out.println(ldscode);
				
			}
      }
		
}
