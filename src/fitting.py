import numpy as np

def polyfitT(x, y, degree):
    coeffs = np.polyfit(x, y, degree)
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    results = ssreg / sstot
    return results

def IVfittting(x, q, w, alp, xi = [], yi = []):
    polyfiti = np.polyfit(xi, yi, 12)
    fiti = np.poly1d(polyfiti)
    return abs(q * (np.exp(x / w) - 1)) + alp * fiti(x)