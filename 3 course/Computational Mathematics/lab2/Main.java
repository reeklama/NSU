package dmitry;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        printInfoBar();
        int n = 3;
        int[][] matrix = new int[n][n];
        for(int i = 0; i < n; i++){
            System.out.print("Строка№");
            System.out.println(i+1);
            for(int j = 0; j < n; j++){
                matrix[i][j] = in.nextInt();
            }
        }

        int[] vector = new int[n];
        System.out.print("Вектор");
        for(int i = 0; i < n; i++){
            vector[i] = in.nextInt();
        }

        printMatrix(matrix, n);
        printVector(vector, n);

        //findX(matrix, vector);
        /*
        colomnVector = initColomnVector()
        print("f:", colomnVector, "\n")

        algSystem = SystemEquations(matrix, colomnVector)
        x = algSystem.findRootsByTridiagAlg()
        print("Found roots:")
        for i in range(len(x)):
        print("x{} = {}".format(i, x[i]))

        */
    }

    static void findX(int[][] M, int[] v){

    }

    static void printMatrix(int[][] m, int n){
        System.out.println("A:");
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                System.out.print(m[i][j]);
                System.out.print("     ");
            }
            System.out.println();
        }
    }

    static void printVector(int[] v, int n){
        System.out.println("f:");
        for(int i = 0; i < n; i++){
            System.out.println(v[i]);
        }
    }

    static void printInfoBar(){
        System.out.println("This program calculates roots by tridiagonal matrix algorithm.");
        System.out.println("The algebraic system has the form: Ax = f");
        System.out.println("A - coefficient matrix.");
        System.out.println("f - column of the right side of the equation.");
        System.out.println("x - column of roots.");
    }
}
