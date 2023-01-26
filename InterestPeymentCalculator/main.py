def each_year(P, r, n, t):

    for period in range(t):
        amount = P*(pow((1+r/n), n*(period+1)))
        print('Period:', period+1, amount)

    return amount

P = 5000 # Boshlang'ich summa
r = .06  # Yillik foiz stavkasi
n = 1  # Yillik birikma davrlari soni
t = 10  # Necha yil
print(each_year(P, r, n, t))

# https://www.statology.org/compound-interest-in-python/