//this is the beginning of the file
public class HelloWorld {
    public static void printMessage(String msg) {
        System.out.println(msg);
    }
    public static void main(String[] args) {
        printMessage("Hello, world!");
        printMessage("This program prints a few lines.");
        for (int i = 1; i <= 10; i++) {
            printMessage("Counting: " + i);
        }
        printMessage("Loop finished.");
        printMessage("Now printing letters:");
        for (char c = 'A'; c <= 'E'; c++) {
            printMessage("Letter: " + c);
        }
        printMessage("Program ended.");
    //this is the end of the file
    } 
}