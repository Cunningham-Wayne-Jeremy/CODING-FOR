package testing;
import java.net.*;
import java.io.*;
import java.util.logging.*;
public class Https_Connection_Buffer_BadPath {

		
		//For the sake of simplicity I did a throw statement
		public static void main(String[] args) throws Exception{
			//Creates an object that will attempt to retrieve the data
			//https is necessary to connect
				//BAD Path the name needs to have https://www in front	
			
			URL webpagename = new URL("www.lds.org");
			
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
		
		
				public static void main1(String[] args) throws Exception{
					//Creates an object that will attempt to retrieve the data
					//https is necessary to connect
						//BAD Path This code will attept to connect to the server and write Hello World to it.
					//It fails because I do not have the proper permissions
					
					URL webpagename = new URL("https://www.lds.org");
					
					//creates the connection to said web page
					HttpURLConnection urlConnection = (HttpURLConnection) webpagename.openConnection();
					 try {
					     urlConnection.setDoOutput(true);
					     urlConnection.setChunkedStreamingMode(0);

					     OutputStream out = new BufferedOutputStream(urlConnection.getOutputStream());
					     writeStream(out);

					     InputStream in = new BufferedInputStream(urlConnection.getInputStream());
					     readStream(in);
					   } finally {
					     urlConnection.disconnect();
					   }

						
						
						
					}


				private static void readStream(InputStream in) throws IOException {
					// TODO Auto-generated method stub
					URL webpagename = new URL("www.lds.org");
					HttpURLConnection urlConnection = (HttpURLConnection) webpagename.openConnection();
					BufferedReader displaydata = new BufferedReader(new InputStreamReader(urlConnection.getInputStream()));
					//here is the string object that the data will display in
					String ldscode;
					//loop while there is data left and display in the string
					while((ldscode = displaydata.readLine())!= null){
						System.out.println(ldscode);}
				}


				private static void writeStream(OutputStream out) throws IOException {
					// TODO Auto-generated method stub
					
					    String output = "Hello world";

					    out.write(output.getBytes());
					    out.flush();
					}
				
		      
}