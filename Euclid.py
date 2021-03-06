print('ユークリッドの互除法\n\n')
while True:

    a: int = []
    b: int = []
    r: int = []
    q: int = []

    #input
    a.append(int(input('>[]x: ')))
    b.append(int(input('>[]y: ')))

    #preview
    print(f'\n{a[0]}x + {b[0]}y = 1')

    if 0 < a[0] or 0 < b[0]: #Check suitability
        i = 0
        print('\n--- ユークリッドの互除法 ---')

        #Euclid
        while True:
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])
            print('  ', a[i], '=', b[i], '×', q[i], '+', r[i])

            if r[i] == 0:
                break
            a.append(b[i])
            b.append(r[i])
            i += 1
        print(f'\n  最大公約数 = {b[i]}\n\n')

        #Hute-Ho-Te-Shiki
        print('--- 不定方程式 ---')
        P = [''] * (i+1)
        P[i] = 1
        while i != 0:
            P[i-1] =  -int(((P[i] * a[i-1])-1) / a[i])
            print(f'  1 = {P[i]} × {a[i-1]} + {P[i-1]} × {a[i]}')
            i -= 1

        #Output
        print('\n')
        print('--- 特殊解 ---')
        print(f'  x0 = {P[i+1]}\n  y0 = {P[i]}')
        print(f'  x = {P[i+1]} + {a[i+1]}t')
        print(f'  y = {P[i]} - {a[i]}t')

        if str(input('\n>exit?(y or n): ')) == 'y': #loop break
            break
    else:
        print('0むりです') #ERROR msg

