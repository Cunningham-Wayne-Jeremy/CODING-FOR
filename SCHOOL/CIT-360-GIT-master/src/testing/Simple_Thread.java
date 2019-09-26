package testing;

public class Simple_Thread implements Runnable {

	

	@Override
	public void run() {
		System.out.println("Hello from a thread");
	
	}
	 public static void main(String args[]) {
		//To declare a thread  
		 (new Thread(new Threads_and_Executors())).start();
}
	
	 
}	
	
	
	

	

