import java.util.*;

public class practice {
    public static void main(String[] args) {
        System.out.println("Talkin' 'bout practice");

        // Random object
        Random r = new Random();

        float[] f = new float[10];

        for(int i = 0; i < 10; i++)
            f[i] = r.nextFloat();

        // 'foreach' syntax (anything that returns an array)
        for(float x : f)
            System.out.print(x);
        System.out.println();

        String sentence = "I am the walrus";

        for(char c : sentence.toCharArray())
            System.out.print(c + " ,");
        System.out.println();

        // break ends a loop
        // continue advances to the next iteration
    }
}
