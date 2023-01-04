import random    
son = random.randint(1, 10)
print("1dan 10gacha son oyladm topishga harakat qiling")
c = 1
while True:
    f_son = int(input("son kiriting -> "))
    if f_son == son:
        print(f"Tabriklayman men oylagan sonni {c} urinishda topdingiz")
        break
    elif f_son < son:
        print("siz kiritgan son men oylagan sondan kichik")
        c += 1
    else:
        print("siz kiritgan son men oylagan sondan katta")
        c += 1
print("\nbiron son oylang men uni topishga harakat qilaman")
t = input()
a = 1
b = 10
k = 1
while True:    
    h = random.randint(a, b)
    print("siz oylagan son ", h)
    savol = "agar men topgan son szniki bn teng bolsa (T), kichik bolsa (-) va katta bolsa (+) -> "
    t = input(savol)
    if t.upper() == 'T':
        print(f"siz o'ylagan sonni men {k} urinishda topdm")
        break
    elif t == '+':
        k += 1
        b -= 1
    elif t == '-':
        k += 1
        a += 1 
if c==k:
    print(f"durrang siz ham men ham {c} urinishda topdik")
elif c > k:
    print(f"men yutdm, chunki siz {c} urinishda men esa {k} urinishda topdm")
else:
    print(f"siz yutdingiz chunki men {k} urinishda siz esa {c} urinishda topdingiz")
    