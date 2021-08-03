def printMat(Matriz):
       for i in range(len(Matriz)):
      for j in range(len(Matriz[0])):
         print("%2s"%Matriz[i][j], " ", end="")
      print()


a = int(input("1 coluna/ 1 linha: "))
b = int(input("2 coluna/ 1 linha: "))
c = int(input("1 coluna/ 2 linha: "))
d = int(input("2 coluna/ 2 linha: "))

Matriz = [[a,b],[c,d]]

printMat(Matriz)

def printMat(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
        print("%2s"%Matriz[i][j], " ", end="")
      print()