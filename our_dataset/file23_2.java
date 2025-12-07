public class Student {
    private String name;
    private int id;
    private int grade;
    public Student(String name, int id, grade) {
        this.name = name;
        this.id = id;
        this.grade = grade;
    }
    public void displayyyy() {
        System.out.println("Year: ");
        System.out.println("Student Information:");
        System.out.println("Name : " + name);
        System.out.println("ID   : " + id);
    }
    public boolean isPassing() {
        return grade >= 60;
    }
    public static void main(String[] args) {
        Student s = new Student("Max", 12345, );
        s.display();
        System.out.println("Passing: " + s.isPassing());
    }
}