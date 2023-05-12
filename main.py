def trans(array):
    new = [[0 for i in range(len(array))] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            new[j][i] = array[i][j]
    return new

def sum(array):
    s=0
    for i in range(len(array)):
        s+=array[i]
    return s

def sumar(value, vartist):
    sumar=0
    for i in range(len(value)):
        for j in range(len(value[i])):
            if value[i][j]>0:
                sumar+=value[i][j]*vartist[i][j]
    return sumar

def sumarray(value):
    sumarray = 0
    for i in range(len(value)):
        for j in range(len(value[i])):
            sumarray += value[i][j]
    return sumarray


def is_open(potreby, zapas):
    num=0
    if sum(potreby)!=sum(zapas):
        num = sum(potreby)-sum(zapas)
    return num

def open_zapas(num, vartist, zapas):
    for i in range(len(vartist)):
        vartist[i].append(0)
    zapas.append(num)
    return (vartist, zapas)

def open_potreby(num, vartist, potreby):
    num=abs(num)
    new = [0] * len(zapas)
    vartist.append(new)
    potreby.append(num)
    return (vartist, potreby)



def min_index(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]!=0:
                min=array[i][j]
                k=i
                n=j
                break
    for i in range(len(array)):
        for j in range(len(array[i])):
            a=array[i][j]
            if (array[i][j]<min) & (array[i][j]!=0):
                min=array[i][j]
                k=i
                n=j
    return (k, n)

def min_vartist(vartist, potreby, zapas):
    potreby_change = list(map(lambda x: x, potreby))
    zapas_change = list(map(lambda x: x, zapas))
    vartist_change = []
    for i in range(len(vartist)):
        n = []
        for j in range(len(vartist[i])):
            n.append(vartist[i][j])
        vartist_change.append(n)
    value = [[0 for _ in range(len(vartist_change[0]))] for _ in range(len(vartist_change))]
    while (sum(potreby_change)-potreby_change[-1] != 0) & (sum(zapas_change)-zapas_change[-1] != 0):
        i, j = min_index(vartist_change)
        if potreby_change[i] > zapas_change[j]:
            value[i][j] = zapas_change[j]
            potreby_change[i] -= zapas_change[j]
            zapas_change[j] = 0
            vartist_change[i][j] = 0
        elif potreby_change[i] < zapas_change[j]:
            value[i][j] = potreby_change[i]
            zapas_change[j] -= potreby_change[i]
            potreby_change[i] = 0
            vartist_change[i][j] = 0
        else:
            value[i][j] = potreby_change[i]
            zapas_change[j] = 0
            potreby_change[i] = 0
            vartist_change[i][j] = 0
    if (sum(potreby_change)-potreby_change[-1]==0) & (sum(zapas_change)!=0):
        for i in range(len(vartist_change[-1])):
            if potreby_change[-1] > zapas_change[i]:
                value[-1][i] = zapas_change[i]
                potreby_change[-1] -= zapas_change[i]
                zapas_change[i] = 0
                vartist_change[-1][i] = 0
            elif potreby_change[-1] < zapas_change[i]:
                value[-1][i] = potreby_change[-1]
                zapas_change[i] -= potreby_change[-1]
                potreby_change[-1] = 0
                vartist_change[-1][i] = 0
            else:
                value[-1][i] = potreby_change[-1]
                zapas_change[i] = 0
                potreby_change[-1] = 0
                vartist_change[-1][i] = 0
            if (sum(potreby_change)==0) & (sum(zapas_change)==0):
                break
    elif (sum(zapas_change)-zapas_change[-1]==0) & (sum(potreby_change)!=0):
        for i in range(len(vartist_change)):
            if potreby_change[i] > zapas_change[-1]:
                value[i][-1] = zapas_change[-1]
                potreby_change[i] -= zapas_change[-1]
                zapas_change[-1] = 0
                vartist_change[i][-1] = 0
            elif potreby_change[i] < zapas_change[-1]:
                value[i][-1] = potreby_change[i]
                zapas_change[-1] -= potreby_change[i]
                potreby_change[i] = 0
                vartist_change[i][-1] = 0
            else:
                value[i][-1] = potreby_change[i]
                zapas_change[-1] = 0
                potreby_change[i] = 0
                vartist_change[i][-1] = 0
            if (sum(potreby_change)==0) & (sum(zapas_change)==0):
                break
    return value


#Перевірка матриці значень перевезень на виродженість
def vyrodzhenist(value, potreby, zapas):
    n=0
    for i in range(len(value)):
        for j in range(len(value[i])):
            if value[i][j]!=0:
                n+=1
    if len(potreby)+len(zapas)-1==n:
        return True
    else:
        return False

#Якщо матриця вироджена, то додаємо 'зайняту' клітинку і позначеємо як -1
def vyrodarray(value, vartist):
    while not vyrodzhenist(value, potreby, zapas):
        min=vartist[0][0]
        k=0
        n=0
        for i in range(len(value)):
            for j in range(len(value[i])):
                if (value[i][j] == 0) & (vartist[i][j] < min) & (value[i][j] != -1) & (vartist[i][j] != 0):
                    min=vartist[i][j]
                    k=i
                    n=j
        value[k][n]=-1
    return value

#Вираховуэмо значення u, v для
def find_u_v(value, vartist, zapas, potreby):
    u = [0 for i in range(len(zapas))]
    v = [0 for i in range(len(potreby))]
    uperevirka = [0]
    vperevirka = []
    flag = len(potreby) + len(zapas) - 1
    vartist_t = trans(vartist)
    if not vyrodzhenist(value, potreby, zapas):
        value=vyrodarray(value, vartist)
    value_t = trans(value)
    for i in range(len(value_t[0])):
        if ((value_t[0][i] != 0) | (value_t[0][i] == -1))& (i not in vperevirka):
            v[i]=vartist_t[0][i]
            vperevirka.append(i)
            flag-=1
    i=1
    while flag!=0:
        for j in vperevirka:
            if ((value_t[i][j] != 0) | (value_t[i][j] == -1)) & (i not in uperevirka):
                u[i]= vartist_t[i][j] - v[j]
                flag-=1
                uperevirka.append(i)
        for j in range(len(value_t[i])):
            if ((value_t[i][j] != 0) | (value_t[i][j] == -1))  & (j not in vperevirka):
                v[j] = vartist_t[i][j] - u[i]
                vperevirka.append(j)
                flag -= 1
        i+=1
        if i>=len(zapas):
            i=0

    return (u, v)

#Перевіряємо оптимальність плану методом потенціалів, якщо план не оптимальний, переходимо до функції pattern
def potentials(value, vartist, u, v):
    value_t=trans(value)
    vartist_t=trans(vartist)
    potential=[[0 for i in range(len(vartist))] for i in range(len(vartist[0]))]
    flag=0
    for i in range(len(value_t)):
        for j in range(len(value_t[i])):
            if value_t[i][j]==0:
                potential[i][j]= (u[i] + v[j]) - vartist_t[i][j]
                if potential[i][j]>0:
                    flag=potential[i][j]
            elif value_t[i][j]==-1:
                value_t[i][j]=0
    return (trans(potential), flag)


def pererahunok(potential, value, flag):
    for i in range(len(value)):
        for j in range(len(value[i])):
            if potential[i][j]>0:
                col=i
                row=j
    rows=[]
    cols=[]
    for i in range(len(value[0])):
        a=value[col][i]
        if value[col][i]>0:
            rows.append(i)
    for i in range(len(value)):
        b=value[i][row]
        if value[i][row]>0:
            cols.append(i)
    c=-1
    for i in cols:
        for j in rows:
            l=value[i][j]
            if value[i][j]>0:
                c=i
                r=j
    if c==-1:
        array=[[0 for i in range(len(value[i]))] for i in range(len(value))]
        return array
    n=min(value[c][row], value[col][r])
    value[c][row]-=n
    value[col][r]-=n
    value[col][row]=n
    value[c][r]+=n
    return value


def final(vartist, potreby, zapas):
    n = len(potreby)
    k = len(zapas)
    num = is_open(potreby, zapas)
    if num > 0:
        vartist, zapas = open_zapas(num, vartist, zapas)
    elif num < 0:
        vartist, potreby = open_potreby(num, vartist, potreby)
    value = min_vartist(vartist, potreby, zapas)
    u, v = find_u_v(value, vartist, zapas, potreby)
    potential, flag = potentials(value, vartist, u, v)
    while flag != 0:
        value_new = pererahunok(potential, value, flag)
        if sumarray(value_new) == 0:
            break
        else:
            value = value_new
        u, v = find_u_v(value, vartist, zapas, potreby)
        potential, flag = potentials(value, vartist, u, v)
    for i in range(len(value)):
        for j in range(len(value[i])):
            if value[i][j] == -1:
                value[i][j] = 0
    value_t = trans(value)
    for i in range(k):
        for j in range(n):
            print(value_t[i][j], end="   ")
        print()
    print("Sum: ", sumar(value, vartist))

vartist=[[2, 3, 4], [5, 1, 2], [3, 2, 1], [1, 4, 5]]
potreby=[40, 50, 110, 40]
zapas=[90, 80, 70]
# vartist=[[1, 2, 3], [3, 1, 5], [2, 4, 6], [4, 3, 1]]
# potreby=[30, 10, 20, 40]
# zapas=[35, 50, 15]
# vartist=[[4, 5], [6, 5], [3, 2]]
# potreby=[1000, 1300, 1200]
# zapas=[2000, 2500]
# vartist=[[7, 4, 9], [8, 5, 2], [1, 9, 3], [2, 8, 6]]
# potreby=[120, 50, 190, 110]
# zapas=[160, 140, 170]
# vartist=[[6, 8, 5, 9], [4, 5, 6, 7 ], [7, 9, 8, 4]]
# potreby=[120, 100, 110]
# zapas=[105, 55, 90, 80]
final(vartist, potreby, zapas)
