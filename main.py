#Метод для пошуку суми одномурного масиву
def sum(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum

#Метод для пошуку мінімального елементу в масиві
def min(array):
    min=array[0]
    for i in range(len(array)):
        if array[i]<min:
            min=array[i]
    return min

#Метод для пошуку індексу мінімального елементу масиву, який !=-1
def minindex(array):
    for i in range(len(array)):
        if array[i]!=-1:
            min=array[i]
            ind=i
            break
    for i in range(len(array)):
        n=array[i]
        if (n<min) & (n!=-1):
            min=n
            ind=i
    return ind

#Метод для підрахунку суми матриці(для визначення загальної вартості перевезень)
def sumarr(value, array2):
    sum=0
    for i in range(len(value)):
        for j in range(len(value[i])):
            if (array2[i][j]!=0)&(array2[i][j]!=-1):
                sum+= value[i][j] * array2[i][j]
    return sum

#Метод для визначення типу задачі(відкритий/закритий), якщо задача відкритого типу, то виклиаємо додатковий метод vidkryta
def perevirka(potreby, zapas):
    if sum(potreby)!=sum(zapas):
        vidkryta(sum(zapas)-sum(potreby), zapas)

#Метод для транспонування матриці
def trans(array):
    new = [[0 for i in range(len(array))] for i in range(len(array[0]))]
    for i in range(len(array)):
        for j in range(len(array[0])):
            new[j][i] = array[i][j]
    return new

#Якщо задача відкритого типу, то ми додаємо колонку в матрицю вартості та додаємо різницю потреб та запасів в потреби
def vidkryta(num, zapas):
    global value
    new=[0]*len(zapas)
    value.append(new)
    global potreby
    potreby.append(num)

#За допомогою методу мінімальної вартості розставляємо значення перевезень відповідно до матриці вартостей
def iteration(value, potreby, zapas):
    perevirka(potreby, zapas)
    value_copy=[]
    for i in range(len(value)):
        n=[]
        for j in range(len(value[i])):
            n.append(value[i][j])
        value_copy.append(n)
    vartist=[[0 for _ in range(len(value_copy[0]))] for _ in range(len(value_copy))]
    if sum(value_copy[-1]) == 0:
        while sum(potreby[:-2])!=0:
            for i in range(len(value_copy) - 1):
                if potreby[i]!=0:
                    ind=minindex(value_copy[i])
                    if potreby[i]<zapas[ind]:
                        zapas[ind]-=potreby[i]
                        vartist[i][ind]=potreby[i]
                        potreby[i]=0
                    else:
                        vartist[i][ind] =  zapas[ind]
                        potreby[i]-=zapas[ind]
                        zapas[ind]=0
                    value_copy[i][ind]=-1
        while sum(zapas)!=0:
            for i in range(len(zapas)):
                if zapas[i]!=0:
                    vartist[-1][i] = zapas[i]
                    potreby[-1] -= zapas[i]
                    zapas[i] = 0

    else:
        while sum(zapas) != 0:
            for i in range(len(value_copy)):
                if potreby[i]!=0:
                    ind=minindex(value_copy[i])
                    if potreby[i]<zapas[ind]:
                        zapas[ind]-=potreby[i]
                        vartist[i][ind]=potreby[i]
                        potreby[i]=0
                    else:
                        vartist[i][ind] =  zapas[ind]
                        potreby[i]-=zapas[ind]
                        zapas[ind]=0
                    value_copy[i][ind]=-1
    return vartist

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
    while not vyrodzhenist(vartist, potreby, zapas):
        min=value[0][0]
        k=0
        n=0
        for i in range(len(value)):
            for j in range(len(value[i])):
                if (vartist[i][j] == 0) & (value[i][j] < min) & (vartist[i][j] != -1) & (value[i][j] != 0):
                    min=vartist[i][j]
                    k=i
                    n=j
        vartist[k][n]=-1
    return vartist

#Вираховуэмо значення u, v для
def find_u_v(value, vartist, zapas, potreby):
    if vyrodzhenist(vartist, potreby, zapas):
        u=[0 for i in range(len(zapas))]
        v=[0 for i in range(len(potreby))]
        uperevirka=[0]
        vperevirka=[]
        flag=len(potreby)+len(zapas)-1
        value_t=trans(value)
        vartist_t=trans(vartist)
        for i in range(len(value_t[0])):
            if ((vartist_t[0][i] != 0) | (vartist_t[0][i] == -1))& (i not in vperevirka):
                v[i]=value_t[0][i]
                vperevirka.append(i)
                flag-=1
        i=1
        while flag!=0:
            for j in vperevirka:
                if ((vartist_t[i][j] != 0) | (vartist_t[i][j] == -1)) & (i not in uperevirka):
                    u[i]= value_t[i][j] - v[j]
                    flag-=1
                    uperevirka.append(i)
            for j in range(len(value_t[i])):
                if ((vartist_t[i][j] != 0) | (vartist_t[i][j] == -1))  & (j not in vperevirka):
                    v[j] = value_t[i][j] - u[i]
                    vperevirka.append(j)
                    flag -= 1
            i+=1
    else:
        vyrodarray(value, vartist)
        u = [0 for i in range(len(zapas))]
        v = [0 for i in range(len(potreby))]
        uperevirka = [0]
        vperevirka = []
        flag = len(potreby) + len(zapas) - 1
        value_t = trans(value)
        vartist_t = trans(vartist)
        for i in range(len(value_t[0])):
            if ((vartist_t[0][i] != 0) | (vartist_t[0][i] == -1)) & (i not in vperevirka):
                v[i] = value_t[0][i]
                vperevirka.append(i)
                flag -= 1
        i = 1
        while flag != 0:
            for j in vperevirka:
                if ((vartist_t[i][j] != 0) | (vartist_t[i][j] == -1)) & (i not in uperevirka):
                    u[i] = value_t[i][j] - v[j]
                    flag -= 1
                    uperevirka.append(i)
            for j in range(len(value_t[i])):
                if ((vartist_t[i][j] != 0) | (vartist_t[i][j] == -1)) & (j not in vperevirka):
                    v[j] = value_t[i][j] - u[i]
                    vperevirka.append(j)
                    flag -= 1
            i += 1
    return (u, v)

#Перевіряємо оптимальність плану методом потенціалів, якщо план не оптимальний, переходимо до функції pattern
def pererahunok(value, vartist, u, v):
    value_t=trans(value)
    vartist_t=trans(vartist)
    flag=0
    for i in range(len(value_t)):
        for j in range(len(value_t[i])):
            if vartist_t[i][j]==0:
                vartist_t[i][j]= (u[i] + v[j]) - value_t[i][j]
                if vartist_t[i][j]>0:
                    flag=vartist_t[i][j]
            elif vartist_t[i][j]==-1:
                vartist_t[i][j]=0
    return (trans(vartist_t), flag)


#За допомогою перетворень шукаємо оптимальний план(для кожного нового плану виконуємо методи find_u_v та potentsial)
def pattern(value, vartist, vartist_main, zapas, potreby, flag):
    array2t=trans(vartist)
    no=[]
    no_t=[]
    k=0
    n=0
    a1=0
    a2=0
    while flag!=0:
        for i in range(len(array2t)):
            for j in range(len(array2t[i])):
                if array2t[i][j]==flag:
                    k=i
                    n=j
        for i in range(len(vartist[n])):
            if (vartist[n][i] > 0) & (vartist[n][i] != flag) & (vartist[n][i] not in no):
                a1=i
                break
        for i in range(len(array2t[k])):
            if (array2t[k][i]>0) & (array2t[k][i]!=flag) & (array2t[k][i] not in no_t):
                a2=i
                break
        while vartist_main[a2][a1] <=0:
            no.append(vartist_main[n][a1])
            no_t.append(vartist_main[a2][k])
            for i in range(len(vartist_main[n])):
                if (vartist_main[n][i] > 0) & (vartist_main[n][i] not in no):
                    a1 = i
                    break
            if vartist_main[a1][a2] >0:
                break
            for i in range(len(vartist_main)):
                if (vartist_main[i][k] > 0)  & (vartist_main[i][k] not in no_t):
                    a2 = i
                    break

        num=min([vartist_main[a2][k], vartist_main[n][a1]])
        vartist_main[n][k]=num
        vartist_main[n][a1]-=num
        vartist_main[a2][k]-=num
        vartist_main[a2][a1]+=num
        u, v = find_u_v(value, vartist_main, zapas, potreby)
        vartist, flag = pererahunok(value, vartist, u, v)
    return vartist_main

#Метод для виводу фінальних значень
def show(array1, array2, n):
    print("Vartist` perevezen`: " + str(sumarr(array1, array2)))
    print()
    print("Perevezenya:")
    for i in range(len(array2[:n])):
        print(("B"+str(i+1)).rjust(6).ljust(4), end="")
    print()

    array2=trans(array2)
    for i in range(len(array2)):
        print(("A" + str(i + 1)), end="  ")
        for j in range(len(array2[i][:n])):
            if (array2[i][j] == 0) | (array2[i][j] == -1):
                print(str(0).rjust(1).ljust(5), end="")
            else:
                print(str(array2[i][j]).rjust(2).ljust(6), end="")
        print()


#Стручктуруючий метод
def final(value, potreby, zapas):
    n = len(potreby)
    vartist = iteration(value, potreby, zapas)
    u, v = find_u_v(value, vartist, zapas, potreby)
    vartist_main, flag = pererahunok(value, vartist, u, v)
    if flag == 0:
        show(value, vartist, n)
    else:
        vartist = pattern(value, vartist_main, vartist, zapas, potreby, flag)
        show(value, vartist, n)

# value=[[2, 3, 4], [5, 1, 2], [3, 2, 1], [1, 4, 5]]
# potreby=[40, 50, 110, 40]
# zapas=[90, 80, 70]
# value=[[4, 5], [6, 5], [3, 2]]
# potreby=[1000, 1300, 1200]
# zapas=[2000, 2500]

value=[[1, 2, 3], [3, 1, 5], [2, 4, 6], [4, 3, 1]]
potreby=[30, 10, 20, 40]
zapas=[35, 50, 15]

final(value, potreby, zapas)

