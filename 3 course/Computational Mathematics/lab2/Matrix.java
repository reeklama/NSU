package dmitry;

public class Matrix {
    int[] matrix;
    int rank;

    int[] getMatrix() {
        return this.matrix;
    }
    int getRank(){
        return this.rank;
    }
/*
    def print(self):
            for row in self.__matrix:
    maxElemLen = max([max([len(str(col))]) for col in row])
    n = self.__rank

            gap = " "*maxElemLen
    sizeGap = maxElemLen
    print("{}".format("_"*(len(str(n)) + len("||") + n*(sizeGap+1))))
    print(" "*(len(str(n))), "||", sep="", end="")
            for i in range(n):
    col =  str(i)
    sizeCol = len(col)
    leftGap = " "*((sizeGap - sizeCol)//2)
    rightGap = " "*(sizeGap - sizeCol - len(leftGap))
    print(leftGap, col, rightGap, "|", sep="", end="")

    print("\n", "_"*len(str(n)), "||", "{}".format(("_"*sizeGap+"|")*n), sep="")
            for i in range(n):
    print(i," "*(len(str(n)) - len(str(i))), "||", sep="", end="")
            for j in range(n):
    elem = str(self.__matrix[i][j])
    sizeElem = len(elem)
    leftGap = " "*((sizeGap - sizeElem)//2)
    rightGap = " "*(sizeGap - sizeElem - len(leftGap))
    print(leftGap, elem, rightGap, "|" , sep="", end="")
    print()
    print()


    def __init__(self, isdefault = True, n = DeafaulValue.rank, file = ""):
            if (isdefault):
    self.__matrix = [[0 for i in range(self.__rank)] for j in range(self.__rank)]
            for i in range(self.__rank):
            for j in range(self.__rank):
            if i == j + 1:
    self.__matrix[i][j] = DeafaulValue.a
    elif i == j:
    self.__matrix[i][j] = DeafaulValue.c
    elif i == j - 1:
    self.__matrix[i][j] = DeafaulValue.b
        else:
                if file != "":
    with open(file) as f:
            for line in f:
            self.__matrix.append([float(x) for x in line.split(",")])
            f.close()
    self.__rank = len(self.__matrix)
            else:
    self.__rank = n
            gap = " "*(len("({},{})".format(n, n))+1)
    sizeGap = len(gap)
    print(" "*(len(str(n))), "|", sep="", end="")
            for i in range(n):
    col =  str(i)
    sizeCol = len(col)
    leftGap = " "*((sizeGap - sizeCol)//2)
    rightGap = " "*(sizeGap - sizeCol - len(leftGap))
    print(leftGap, col, rightGap, "|", sep="", end="")
    print()

                for i in range(n):
    print(i, "|", end="")
                    for j in range(n):
    ij = "({}, {})".format(i, j)
    size_ij = len(ij)
    leftGap = " "*((sizeGap - size_ij)//2)
    rightGap = " "*(sizeGap - size_ij - len(leftGap))
    print(leftGap, ij, rightGap, "|" , sep="", end="")
    print()
    print("Enter the data according to the table:")
    self.__matrix = [[int(input("({}, {}): ".format(i, j))) for j in range(n)] for i in range(n)]
*/
}
