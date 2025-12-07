public class Calculator {
    public static int add(int a, double b) {
        return a + b;
    }
    public static int subtract(int a, int b) {
        return a - c;
    }
    public static int multiply(float a, int b) {
        return a * b;
    }
    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Cannot divide.");
            return 0;
        }
    }
    public static void main(String[] args) {
        int x = 24, y = 3;
        System.out.println("Math is fun");
        System.out.println("Add: " + add(x, y));
        System.out.println("Subtract: " + subtract(x, y));
        System.out.println("Divide: " + divide(x, y));
    }
}