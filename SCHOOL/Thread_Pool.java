package testing;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
public class Thread_Pool {

	public static void main(String[] args){
		//Create a thread pool
		ExecutorService executorname = Executors.newFixedThreadPool(5);
		for (int i = 0; i < 10; i++) {
			Runnable runnablename = new Threads("" + i);
			executorname.execute(runnablename);
		}
		//you need to shut down the executor after use
		executorname.shutdown();
		while  (!executorname.isTerminated()){
				}
		System.out.println("Finished running all 15 Threads");
	}
	
	
	
}
