import matplotlib.pyplot as plt
def Bresenhams(x, y,x1, y1):
    dx= abs(x1 - x)
    dy =abs(y1 -y)
    p= (2 * dy) -dx
    #for i in range(x,x1):
    while x < x1:
        plt.plot(round(x),round(y), marker="s", color="black")
        x= x + 1
        if p < 0:
            p= p + (2 * dy)
        else:
            p= p + (2 * dy) - (2 * dx)
            y= y + 1
        print(x,y)
    plt.show()
