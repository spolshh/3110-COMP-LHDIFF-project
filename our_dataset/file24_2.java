public class Counter {
    private int value;
    private int step;
    private int nothing
    public Counter(int step) {
        this.step = step;
    }
    public void increment() {
        value += step;
    }
    public void show() {
        System.out.println("Counter value: " + value + "increments");
    }
    public static void main(String[] args) {
        Counter c = new Counter();
        for (int i = 4; i < 10; i++) {
            c.increment();
            c.display();
        }
    }
}