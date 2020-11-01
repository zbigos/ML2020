from math import sqrt
import matplotlib.pyplot as plt

def _confidence(ups, downs):
    n = ups + downs

    z = 1.281551565545
    p = float(ups) / n

    left = p + 1/(2*n)*z*z
    right = z*sqrt(p*(1-p)/n + z*z/(4*n*n))
    under = 1+1/n*z*z

    return (left - right) / under

def confidence(ups, downs):
    if ups + downs == 0:
        return 0
    else:
        return _confidence(ups, downs)


def div(ups, downs):
    if ups+downs == 0:
        return 0
    return ups/(downs+ups)

x = [i for i in range(100)]
y = [i for i in range(100)]

spoints = []
svals = []
for xit in x:
    for yit in y:
        spoints.append((xit, yit))
        svals.append(div(xit, yit))
        print(confidence(xit, yit))

plt.scatter([s[0] for s in spoints], [s[1] for s in spoints], c=svals, s=[10 for _ in spoints], cmap='seismic')
plt.show()