import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1541 {
    public static void main(String[] agrs) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String expression = br.readLine();

        String[] group = expression.split("-");

        int result = 0;
        for (int i = 0; i < group.length; i++) {
            int step = sum(group[i]);
            if (i == 0) {
                result += step;
            } else {
                result -= step;
            }
        }

        System.out.println(result);
        return;
    }

    private static int sum(String expression) {
        int result = 0;
        String[] split = expression.split("\\+");
        for (String s : split) {
            int num = Integer.parseInt(s);
            result += num;
        }
        return result;
    }
}

/*
 * 숫자는 0 으로 시작할 수 있다
 * 숫자는 최대 5자리까지 연속될 수 있다
 * 총 문자열은 50 이하이다.
 * 가장 처음과 마지막은 숫자이다.
 * 연산자는 +와 -뿐이다.
 * 연속해서 2개의 연산자는 나타나지 않는다.
 * 
 * 괄호를 쳐서 값을 최소로 만들어야 한다.
 * 
 * 시간 제한이 2초, N 은 50
 * 
 * 최소로 만들려면? - 인걸 크게 () 쳐야할 거 같은데
 * - 하면 다음 - 가 나올 때 까지 + 를 다 합치면 된다.
 * + 는 그냥 냅둬도 된다.
 */
