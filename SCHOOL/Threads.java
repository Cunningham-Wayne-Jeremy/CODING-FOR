package testing;
import java.util.*;
public class Threads implements Runnable { 

	    private String acommand;
	    
	    public Threads(String astring) {
		this.acommand = astring;
		}


	    @Override
	    public void run() {
	        System.out.println(Thread.currentThread().getName()+" Start. Command = "+acommand);
	        processCommand();
	        System.out.println(Thread.currentThread().getName()+" End.");
	    }

	    private void processCommand() {
	        try {
	            Thread.sleep(5000);
	        } catch (InterruptedException e) {
	            e.printStackTrace();
	        }
	    }

	    @Override
	    public String toString(){
	        return this.acommand;
	    }
	}
		

