package dmitry;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        CubeEq function = new CubeEq();
        System.out.println("Введите изначальные данные");
        System.out.printf("ε:");
        float e = in.nextFloat();
        while (e <= 0){
            System.out.printf("Введите ε больше нуля. ε:");
            e = in.nextFloat();
        }
        System.out.printf("Δ:");
        float d = in.nextFloat();
        while (d <= 0){
            System.out.printf("Введите Δ больше нуля. Δ:");
            d = in.nextFloat();
        }
        System.out.printf("a:");
        CubeEq.a = in.nextFloat();
        System.out.printf("b:");
        CubeEq.b = in.nextFloat();
        System.out.printf("c:");
        CubeEq.c = in.nextFloat();
        function.cubeEq(e, d);
        in.close();
    }
}
