#Используется библиотека matplotlib
import matplotlib.pyplot as plt
from math import sin, cos, pi, atan2, sqrt
from itertools import product
from operator import itemgetter
from random import randint
def find_rhombus_vertices(A, C, side_length):
    x1, y1 = A
    x2, y2 = C
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    dx = x2 - x1
    dy = y2 - y1
    ac_length = sqrt(dx**2 + dy**2)
    if ac_length > 2 * side_length or ac_length == 0:
        return None
    other_diag_length = 2 * sqrt(side_length**2 - (ac_length/2)**2)
    if ac_length > 0:
        dx_norm = dx / ac_length
        dy_norm = dy / ac_length
    else:
        dx_norm, dy_norm = 1, 0
    perp_x = -dy_norm
    perp_y = dx_norm
    offset_x = perp_x * other_diag_length / 2
    offset_y = perp_y * other_diag_length / 2
    B = (mx + offset_x, my + offset_y)
    return B
def plot_figures(nfold, length, center_x = 0, center_y = 0):
    if nfold%2:
        print("Неверное количество сторон")
        return
    fig, ax = plt.subplots(figsize=(15, 9))
    pn=pi/nfold
    sins = tuple([center_x+sin(2*pn*i)*length for i in range(0, nfold)])
    coss = tuple([center_y+cos(2*pn*i)*length for i in range(0, nfold)])
    xs = list(coss)
    ys = list(sins)
    side_length = sqrt((xs[1]-xs[0])**2+(ys[1]-ys[0])**2)
    old_circles_x = xs[::2]
    old_circles_y = ys[::2]
    xs = xs[1::2]+old_circles_x
    ys = ys[1::2]+old_circles_y
    n =nfold//2
    for circle_id in range((nfold-2)//4):
        circles_x = []
        circles_y = []
        new_point = find_rhombus_vertices((old_circles_x[-1], old_circles_y[-1]), (old_circles_x[0], old_circles_y[0]), side_length)
        circles_x.append(new_point[0])
        circles_y.append(new_point[1])
        for i in range(0, len(old_circles_x)-1):
            new_point = find_rhombus_vertices((old_circles_x[i], old_circles_y[i]), (old_circles_x[i+1], old_circles_y[i+1]), side_length)
            circles_x.append(new_point[0])
            circles_y.append(new_point[1])
        xs.extend(circles_x)
        ys.extend(circles_y)
        old_circles_x = tuple(circles_x)
        old_circles_y = tuple(circles_y)
    for i in range(n, len(xs)-n):
        if (i+1)%n==0:
            ax.fill([xs[i], xs[i+1], xs[i+1-n], xs[i-n]], [ys[i], ys[i+1], ys[i+1-n], ys[i-n]], color = (randint(0,223)/255, randint(0, 191)/255, randint(0, 255)/255))
        else:
            ax.fill([xs[i], xs[i+n+1], xs[i+1], xs[i-n]], [ys[i], ys[i+n+1], ys[i+1], ys[i-n]], color = (randint(0,223)/255, randint(0, 191)/255, randint(0, 255)/255))
    minxs = min(xs)
    maxxs = max(xs)
    minys = min(ys)
    maxys = max(ys)
    print(f"Тут всего {len(xs)} точек")
    plt.xlim(minxs*(1+0.4*((minxs<0)-0.5)), maxxs*(1+0.4*((maxxs>0)-0.5)))
    plt.ylim(minys*(1+0.4*((minys<0)-0.5)), maxys*(1+0.4*((maxys>0)-0.5)))
    ax.set_aspect('equal')
    plt.title(f'Points of Penrose Tiling from a point {nfold}-fold')
    plt.show()
plot_figures(int(input())*4+2, 3, center_x = 0, center_y = 0)
