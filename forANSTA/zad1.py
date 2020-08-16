def make_postcode_list(arg):   # arg jest listą dwuelementową (2 kody pocztowe)
    # dzieliny kody na częś 1 i 2
    n1 = [int(arg[0][:2]),int(arg[0][3:])]
    n2 = [int(arg[1][:2]),int(arg[1][3:])]

    # upewniamy się, że n1 ma mniejszą liczbę w części 1
    if n1[0] > n2[0]:
        buf = n1
        n2 = n1
        n1 = buf

    # lista liczb cz. 1
    firtPat = range(n1[0],n2[0]+1)
    lista_kodow = []

    # tworzymy listę kodów pocztowych
    if  n1[0] == n2[0]:
        secPart = list(range(n1[1]+1,n2[1]))
        [lista_kodow.append(str("%02d" %n1[0]) + '-' + str("%03d" %a)) for a in secPart ]
    else:
        [lista_kodow.append(str("%02d" %n1[0]) + '-' + str("%03d" %i)) for i in range(n1[1]+1,1000) ]
        for fP in range(n1[0]+1,n2[0]):
            [lista_kodow.append(str("%02d" %fP) + '-' + str("%03d" %a)) for a in range(1000) ]
        [lista_kodow.append(str("%02d" %n2[0]) + '-' +  str("%03d" %i)) for i in  range(n2[1]) ]
    return lista_kodow
