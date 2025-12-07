public class Animal {
    private String type;
    private int age;
    public Animal(String type, int age) {
        this.type = type;
        this.age = age;
    }
    public void describe() {
        System.out.println("Animal Type: " + type);
        System.out.println("Age        : " + age + " years");
    }
    public void sound() {
        System.out.println("The " + type + " makes a sound.");
    }
    public static void main(String[] args) {
        Animal a = new Animal("Dog", 5);
        a.describe();
        a.sound();
    }
}