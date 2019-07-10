

public class AccessMultiDimentionalArray {
	public static void main(String[] args) {
		int[][][] StudentArray = { { {10, 20, 30}, {50, 60, 70}, {80, 90, 100}, {110, 120, 130} },
                                   { {15, 25, 35}, {22, 44, 66}, {33, 55, 77}, {78, 57, 76} }
                                  };
		System.out.println("Element at StudentArray[0][0][0] = " + StudentArray[0][0][0]);
		System.out.println("Element at StudentArray[0][0][1] = " + StudentArray[0][0][1]);
		System.out.println("Element at StudentArray[0][0][2] = " + StudentArray[0][0][2]);
		System.out.println("Element at StudentArray[0][1][0] = " + StudentArray[0][1][0]);
		System.out.println("Element at StudentArray[0][1][1] = " + StudentArray[0][1][1]);
		System.out.println("Element at StudentArray[0][1][2] = " + StudentArray[0][1][2]);
		System.out.println("Element at StudentArray[0][2][0] = " + StudentArray[0][2][0]);
		System.out.println("Element at StudentArray[0][2][1] = " + StudentArray[0][2][1]);
		System.out.println("Element at StudentArray[0][2][2] = " + StudentArray[0][2][2]);
		System.out.println("Element at StudentArray[0][3][0] = " + StudentArray[0][3][0]);
		System.out.println("Element at StudentArray[0][3][1] = " + StudentArray[0][3][1]);
		System.out.println("Element at StudentArray[0][3][2] = " + StudentArray[0][3][2]);
		
		//Accessing Second Table Rows & Columns
		System.out.println("=============");
		System.out.println("Element at StudentArray[1][0][0] = " + StudentArray[1][0][0]);
		System.out.println("Element at StudentArray[1][0][1] = " + StudentArray[1][0][1]);
		System.out.println("Element at StudentArray[1][0][2] = " + StudentArray[1][0][2]);
		System.out.println("Element at StudentArray[1][1][0] = " + StudentArray[1][1][0]);
		System.out.println("Element at StudentArray[1][1][1] = " + StudentArray[1][1][1]);
		System.out.println("Element at StudentArray[1][1][2] = " + StudentArray[1][1][2]);
		System.out.println("Element at StudentArray[1][2][0] = " + StudentArray[1][2][0]);
		System.out.println("Element at StudentArray[1][2][1] = " + StudentArray[1][2][1]);
		System.out.println("Element at StudentArray[1][2][2] = " + StudentArray[1][2][2]);
		System.out.println("Element at StudentArray[1][3][0] = " + StudentArray[1][3][0]);
		System.out.println("Element at StudentArray[1][3][1] = " + StudentArray[1][3][1]);
		System.out.println("Element at StudentArray[1][3][2] = " + StudentArray[1][3][2]);
	}
}