import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rd


N = int(input('바늘의 개수:'))    #바늘의 총 개수
n = 0                           #세로선에 닿은 바늘의 수

x = rd.uniform(1, 7, N)  
y = rd.uniform(1, 5, N)
t = rd.uniform(0, 2*np.pi, N)    # 각각 바늘의 x값,  y값, 바늘의 회전 각도에 대한 난수를 생성합니다. 


def needle(i):                                              #바늘을 생성하는 함수 입니다.
    return plt.plot([x[i], x[i] + np.cos(t[i])],
                    [y[i], y[i] + np.sin(t[i])])


def line(x):                                                #평면에 세로선을 그어주는 함수 입니다.
    return plt.plot([x, x], [0, 6], 'k')


lines = line(np.arange(9))
needles = needle(np.arange(N))

for needle in needles:
    '''
    바늘이 세로선에 닿은 여부를 판별해 주는 부분입니다. 중간값 정리에서 힌트를 얻었습니다.
    바늘의 양 끝의 x값 사이에 정수(세로선이 있는부분)가 있으면 바늘이 세로선을 지나간 것이며, 그렇게 되면 두 x값의 
    정수부분이 다르다는 점을 이용했습니다. 바늘이 세로선과 겹치는 경우는 거의 없어서 고려하지 않았습니다.
    '''
    check = [int(i) for i in needle.get_xdata()]

    if check[0] != check[1]:
        n += 1      

Pi = 2*N/n

plt.title('$\pi\\approx$' + str(Pi))
plt.margins(False)

plt.show()
