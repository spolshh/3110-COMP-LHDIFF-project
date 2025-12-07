public class Student {
    private String name;
    private int id;
    private double grade;
    public Student(String name, int id, double grade) {
        this.name = name;
        this.id = id;
        this.grade = grade;
    }
    public void display() {
        System.out.println("Student Information:");
        System.out.println("Name : " + name);
        System.out.println("ID   : " + id);
        System.out.println("Grade: " + grade);
    }
    public boolean isPassing() {
        return grade >= 50;
    }
    public static void main(String[] args) {
        Student s = new Student("Alex", 12345, 78.5);
        s.display();
        System.out.println("Passing: " + s.isPassing());
    }
}