import java.util.*;

public class Main {
    public static void main(String[] args) {
        new Main().solution();
    }

    public void solution() {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int answer = recurse(a, b);

        System.out.println(answer);
    }

    public int recurse(int a, int b) {
        if (a == b) return 1;
        if (a > b) return -1;

        int retVal;

        if (b % 2 == 0) {
            retVal = recurse(a, b/2);
        } else if (b % 10 == 1) {
            retVal = recurse(a, b/10);
        } else {
            retVal = -1;
        }

        if (retVal == -1) return -1;
        else return retVal + 1;
    }
}
