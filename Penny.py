n1=205.15; n2=211.67; penny=0
list31=[1, 3, 5, 7, 8, 10, 12]
def mounth31(mn,chisl):
    if list31.count(mn):
        chisl+=1
    elif mn==2:
        chisl=chisl+vis-2
    return chisl
def rur(huh):
    zuz=0
    return 30+mounth31(huh,zuz)
def kf (huh):
    if huh>6:
        return n2
    else:
        return n1
def pen(koef,huh):
    return rur(huh)*vden*koef
print('Введите потребление ГВС в многоквартирном доме по ОДПУ в куб.м')
k=float(input())
print('Введите суммарное потребление ГВС жилыми и нежилыми помещениями в многоквартирном доме в куб.м')
t=float(input())
print('Введите площадь всех жилых и нежилых помещений в многоквартирном доме в кв.м')
r=float(input())
print('Введите площадь квартиры собственника в кв.м')
s=float(input())
print('Високосный ли год? 1-да, 0-нет')
vis=int(input())
vden=(k-t)*s/r
print('У собственника были долги? 1-да, 0-нет')
if 1==int(input()):
    print('Введите число, сколько промежутков долгов было у собственника')
    prom=int(input())
    for i in range (0,prom):
        print('Введите номер месяца, начиная с которого собственник не платил за услуги')
        mounthn=int(input())
        print('Введите через пробел день и номер месяца, когда собственник заплатил за услуги')
        day,mounthk=input().split()
        day=int(day)-1
        mounthk=int(mounthk)
        mounth=mounthk-mounthn
        a2=0
        for j in range (mounthn+1, mounthk):
            a2=mounth31(j,a2)
        if (mounth-1)*30+a2+day>30:
            ret=pen(kf(mounthn),mounthn)
            j=mounth+1
            tut=0
            while (tut<=30) and (j!=mounthk):
                tut+=rur(j)
                if tut>30:
                    penny+=ret*(tut-30)/300
                ret+=pen(kf(j),j)
                j+=1
            while (tut<=90) and (j!=mounthk):
                tut+=rur(j)
                if tut>90:
                    penny+=ret*(tut-90)/130+ret*(rur(j)+90-tut)/300
                else:
                    penny+=ret*rur(j)/300
                ret+=pen(kf(j),j)
                j+=1
            while j!=mounthk:
                penny+=ret*rur(j)/130
                ret+=pen(kf(j),j)
                j+=1
            if tut<30:
                penny+=ret*(tut+day-30)/300
            elif tut<90:
                if tut+day>=90:
                    penny+=ret*(tut+day-90)/130+ret*(90-tut)/300
                else:
                    penny+=ret*day/130
            else:
                penny+=ret*day/130
plat=vden*(n1*(181+vis)+n2*184)+penny
g=round(plat,3)-plat//1
p=0
if g*1000%10>0:
    p=1
print('Размер годовой платы на ГВС:')
print(int(plat//1),'руб.', int(g*100//1+p), 'коп.')
