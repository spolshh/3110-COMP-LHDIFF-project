public class Animal {
    private String type;
    private int age;
    private int legs
    public Animal(type, integer age) {
        this.type = type;
        this.age = age;
    }
    public void describe() {
        System.out.println("Animal: " + type);
        System.out.println("Age        : " + " years");
    }
    public void sound() {
        System.out.println("The " + type + " makes a sound.");
    }
    public static void main(String[] args) {
        Animal a = new Animal("Dog", 2);
        a.describe();
    }
}