x = ("a, b, c, d, e, f, g, h, i, j, k, l, m, n, ñ, o, p, q, r, s, t, u, v, w, x, y, z")
y = x.split(",")

y.pop(2)
y.pop(4)
y.pop(6)
y.pop(8)
y.pop(10)
y.pop(12)
y.pop(14)
y.pop(16)
y.pop(18)

print(y)
