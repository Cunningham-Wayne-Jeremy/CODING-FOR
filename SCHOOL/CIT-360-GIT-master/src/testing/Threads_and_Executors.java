package testing;

public class Threads_and_Executors implements Runnable {
	private String nameofstring;
	
public void Thread(String nameofstring)
{
this.nameofstring = nameofstring;
}
	@Override
	public void run() {
		System.out.println("Hello from a thread");
	
	}
	 public static void main(String args[]) {
		//To declare a thread  
		 (new Thread(new Threads_and_Executors())).start();
}
	
	 
}	
	
	
	
	
/*SingleThreadPoolExceutor The Single Executor executes one task at a time sequentially.*/
	
/*FixedThreadPoolExceutor Is a fixed amount*/
	
/*ScheduledThreadPoolExceutor schedules execution time*/	
	

