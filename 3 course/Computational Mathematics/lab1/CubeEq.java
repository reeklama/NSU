package dmitry;

import static java.lang.Math.abs;
import static java.lang.Math.sqrt;

public class CubeEq {
    public static float a;
    public static float b;
    public static float c;
    public void cubeEq(float e, float d) {
        float disc = (2*a) * (2*a) - 4*3*b;
        if(disc <= 0){
            if(c > e){
                System.out.println("Корень на (-∞;0]");
                System.out.println("x: ");
                System.out.println(toLeft(e, d,0));
            } else if(c < (-e)){
                System.out.println("Корень на [0;+∞)");
                System.out.println("x: ");
                System.out.println(toRight(e, d,0));
            }else {
                System.out.println("Корень f(0)=c");
                System.out.println("x: ");
                System.out.println(c);
            }
        } else{
            float x1 = (float) ((-(2*a) - sqrt(disc))/6),
                    x2 = (float) ((-(2*a) + sqrt(disc))/6);
            float alpha = f(x1),
                    beta = f(x2);
            System.out.println(alpha);
            System.out.println(beta);
            if(alpha > e){
                if (beta > e){
                    System.out.println("Корень на (-∞;alpha]");
                    System.out.println("x: ");
                    System.out.println(toLeft(e, d, x1));
                } else if (beta < -e){
                    System.out.println("Корни на (-∞,alpha][alpha,beta][beta,+∞)");
                    System.out.println("x1: ");
                    System.out.println(toLeft(e, d, x1));
                    System.out.println("x2: ");
                    System.out.println(find_in_range(x1, x2, e));
                    System.out.println("x3: ");
                    System.out.println(toRight(e, d, x2));
                } else {
                    System.out.println("Корни на (-∞,alpha],beta)");
                    System.out.println("x1: ");
                    System.out.println(toLeft(e, d, x1));
                    System.out.println("x2: ");
                    System.out.println(x2);
                }
            } else if(alpha < -e){
                    System.out.println("Корень на [beta,+∞)");
                    System.out.println("x: ");
                    System.out.println(toRight(e, d, x2));
            } else {
                if (beta < -e){
                    System.out.println("Корни на alpha,[beta,+∞)");
                    System.out.println("x1: ");
                    System.out.println(x1);
                    System.out.println("x2: ");
                    System.out.println(toRight(e, d, x2));
                } else {
                    System.out.println("Корень");
                    System.out.println("x: ");
                    System.out.println((x1+x2)/2);
                }
            }
        }
    }

    private float f(float x){
        return x*x*x + a*x*x + b*x +c;
    }

    private float toLeft(float e, float d, float right){
        float left = right - d;
        while (f(left) > 0){
            left -= d;
        }
        return find_in_range(left, right, e);
    }

    private float toRight(float e, float d, float left){
        float right = left + d;
        while (f(right) < 0){
            right += d;
        }
        return find_in_range(left, right, e);
    }

    private float find_in_range(float left,float right,float e) {
        boolean sign = f(left) < f(right);
        float answer = (left + right) / 2;
        while (abs(f(answer)) > e) {
            if (f(answer) > e) {
                if (sign){
                    right = answer;
                }
                else{
                    left = answer;
                }
            } else {
                if (sign){
                    left = answer;
                }
                else{
                    right = answer;
                }
            }
            answer = (left + right) / 2;
        }
        return answer;
    }
}
