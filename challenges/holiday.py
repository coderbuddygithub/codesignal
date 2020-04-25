import calendar as c
def holiday(x, w, m, y):
    f, l = c.monthrange(y, [*c.month_name].index(m))
    r = ([*c.day_name].index(w) - f) % 7 + x * 7 - 6
    return r + ~r * (r > l)