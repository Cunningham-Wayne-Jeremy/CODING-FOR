package testing;

import static org.junit.Assert.*;

import org.junit.Ignore;
import org.junit.Test;

public class JUnitTestCase{

		@Test
		public void testSubtraction() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			int result = test.IntSubtraction(10, 20);
			assertEquals(-10, result);
		}

		
		@Test
		public void testSqaurert() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			int result = test.square(10);
			assertEquals(100, result);
		}

		//This test will use assertArrayEquals to verify arrays of expected and results.
		@Test
		public void testArray(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			int[] value = {100,36,25,16};
			int[] expected = {10,6,5,4};
			int[] result = new int[4];
			for(int i = 0; i<value.length;i++){
				result[i] = test.square(value[i]);
			}
			assertArrayEquals(expected,result);
		}
		

		//This test will use assertTrue to test the result of square()
		@Test
		public void testTrue(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			double result = test.square(10);
			assertTrue(100 == result);
		}
		
		//This test will use assertFalse to test the result of square()
		@Test
		public void testFalse(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			double result = test.square(10);
			assertFalse(100 != result);
		}
		
		//This test will use assertNull to test if the result is null
		@Test
		public void testNull(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			String result = test.nullForJeremy("Jeremy");
			assertNull(result);
		}
		
		//This test will use assertNotNull to test if the result is not null
		@Test
		public void testNotNull(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			String result = test.nullForJeremy("Tom");
			assertNotNull(result);
		}
		
		//This test uses assertSame to test if two objects are actually the same one
		@Test
		public void testSameObject(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			Object testObj = new JUnitMyFunctions();
			Object result = test.returnSameObject(testObj);
			assertSame(testObj, result);
		}
		
		//This test uses assertNotSame to test if two objects are not the same one
		@Test
		public void testNotSameObject(){
			JUnitMyFunctions test = new JUnitMyFunctions();
			Object testObj = new JUnitMyFunctions();
			Object result = test.returnSameObject(new JUnitMyFunctions());
			assertNotSame(testObj, result);
		}
		
		//fail() will just fail the test with a message.
		@Test
		public void failTest(){
			fail("This test failed.");
		}
		
		// This test will not run because of the @Ignore
	
		@Ignore
		@Test
		public void testSqaurert2() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			int result = test.square(10);
			assertEquals(100, result);
		}

		// This test will fail because the test run more than 0.02 second
		@Test(timeout = 20)
		public void testPrintMessage() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			test.PrintJTest(10000);
		}

		// Similar to the last test, but this one run less than 0.02 second
		// so it passed
		@Test(timeout = 20)
		public void testPrintMessage2() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			test.PrintJTest(100);
		}

		/*
		 * This test expects an IndexOutOfBoundsException
		 * It will fail if any other exception thrown or no exception
		 */
		@Test(expected = IndexOutOfBoundsException.class)
		public void testException() {
			JUnitMyFunctions test = new JUnitMyFunctions();
			test.arrayIndexOutofBounds();
		}

	
}

