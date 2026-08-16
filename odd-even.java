public class EvenOdd {

    public static void main(String[] argd) {

        int n = 6;
        int rem = n % 2; 

        if (rem == 0) {
            System.out.println(n + " is even");
        } else {
            System.out.println(n + " is odd");
        }

    }
}