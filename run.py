import pylab


def f(x):
    return (pylab.cos(x) ** 2) / pylab.sqrt(2 * x - 1)


a, b, n = 0, 10 * pylab.pi, 100

xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs))

pylab.grid()

pylab.savefig('sfn.png')

pylab.show()
