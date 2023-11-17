print((lambda n: [0, 1] + [((lambda f: f(f, i))(lambda f, x: 1 if x <= 2 else f(f, x - 1) + f(f, x - 2))) for i in range(2, n)])(10))
