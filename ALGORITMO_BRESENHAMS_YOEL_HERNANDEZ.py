from GRAFICA_BRESENHAMS  import Bresenhams
def main():
    x = int(input('INGRESA VALOR PARA X: \n'))
    y = int(input('INGRESA VALOR PARA Y: \n'))
    x1 = int(input('INGRESA VALOR PARA X1: \n'))
    y1 = int(input('INGRESA VALOR PARA Y1: \n'))
    Bresenhams(x,y,x1,y1)

if __name__=='__main__':
   main()