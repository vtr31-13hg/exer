pr1=float(input('digite o preço de um produto'))
pr2=float(input('digite o preço do segundo produto'))
pr3=float(input('digite o preço de outro produto'))
if p1<p2 and p3:
    print('compre esse produto de {}'.format(pr1))
elif p2<p1 and p3:
    print('compre esse produto de {}'.format(pr2))
else:
    print('compre o produto que custa {}'.format(pr3))