package JSONSimpleWritingToFileExample;


import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
 
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
 
/*
 * @Author : Jeremy Cunningham
 * This is a simple program but I am proud of it 
 * What this will do is create a JSON object and put three strings into the object 
 * Then the data will be saved in a file in the C:Drive
 */
public class JSONSimpleWritingToFileExample {
 
    public static void main(String[] args) {
 
        JSONObject nationObj = new JSONObject();
        nationObj.put("Name", "United States of America");
        nationObj.put("Population", new Integer(321000000));
        nationObj.put("Monetary Value in Tillions", new Double(17.95));
        nationObj.put("Capitalist Nation?",new Boolean(true));
        
 /*When using the put command the syntax must be in double qoutes singles wont work
        Bad Paths: nationObj.put('some namme', new Integer(10));
        Also two variables only nationObj.put("some namme", new Integer(10)), "word";
        From all this testing I realized that this is a hashmap!
        Another Bad Path that got me:
        nationObJ.put("Capitalist Nation?",new Boolean(true)); captial J in Obj
        
        */
        JSONArray listOfStates = new JSONArray();
        listOfStates.add("Colorado");
        listOfStates.add("Alabama");
        listOfStates.add("Delaware");
 
        nationObj.put("States", listOfStates);
 
        try {
            
            // Writing to a file
            File file=new File("C:NationJSONFile.json");
            file.createNewFile();
            FileWriter fileWriter = new FileWriter(file);
            System.out.println("Writing JSON object to file");
            System.out.println("-----------------------");
            System.out.print(nationObj);
 
            fileWriter.write(nationObj.toJSONString());
            fileWriter.flush();
            fileWriter.close();
 
        } catch (IOException e) {
            e.printStackTrace();
        }
 
    }
}