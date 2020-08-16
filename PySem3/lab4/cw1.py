import numpy  as np

t = np.arange(1., 11, 1)
# t=t*0

# print np.random.random_integers(-1,1,2)

n = (3. / 2)
dim = 2


def silnia(n):
    sil = 1.
    if (n % 1) == 0:
        while n > 1:
            sil = sil * n
            n = n - 1.
    else:
        while n > 1.:
            sil = sil * n
            n = n - 1.

        sil = sil * (np.sqrt(np.pi) / 2)
    return sil


##########################################################
def strzal(dim):
    No = 0.
    Nk = 0.
    So = (np.pi ** (dim / 2)) / (silnia(dim / 2))
    Sk = 2 ** dim


# for i in range(10):


##########################################################
print silnia(1. / 2)
# strzal(2)
