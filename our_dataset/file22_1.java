public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }
    public static int subtract(int a, int b) {
        return a - b;
    }
    public static int multiply(int a, int b) {
        return a * b;
    }
    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Cannot divide by zero.");
            return 0;
        }
    }
    public static void main(String[] args) {
        int x = 12, y = 3;
        System.out.println("Add: " + add(x, y));
        System.out.println("Subtract: " + subtract(x, y));
        System.out.println("Multiply: " + multiply(x, y));
        System.out.println("Divide: " + divide(x, y));
    }
}