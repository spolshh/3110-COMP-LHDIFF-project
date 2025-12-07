public class Counter {
    private int value;
    private int step;
    public Counter(int step) {
        this.value = 0;
        this.step = step;
    }
    public void increment() {
        value += step;
    }
    public void show() {
        System.out.println("Counter value: " + value);
    }
    public static void main(String[] args) {
        Counter c = new Counter(2);
        for (int i = 0; i < 10; i++) {
            c.increment();
            c.show();
        }
    }
}