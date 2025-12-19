#coding:utf8

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

# --------- Fonctions d'affichage ---------

def plot_discrete(x, pmf, title):
    plt.figure(figsize=(6,4))
    plt.stem(x, pmf)
    plt.title(title)
    plt.xlabel("k")
    plt.ylabel("P(X=k)")
    plt.grid(True)
    plt.savefig(f"{title}.png")
    plt.close()
 

# --------- 1. Lois discrètes ---------

# 1. Dirac en 3
x = np.arange(0, 10)
pmf = np.zeros_like(x, dtype=float)
pmf[x == 3] = 1
plot_discrete(x, pmf, "Loi de Dirac (point 3)")

# 2. Uniforme discrète sur {0,...,9}
x = np.arange(0, 10)
pmf = st.randint.pmf(x, 0, 10)
plot_discrete(x, pmf, "Loi uniforme discrète")

# 3. Loi binomiale
n, p = 20, 0.4
x = np.arange(0, n+1)
pmf = st.binom.pmf(x, n, p)
plot_discrete(x, pmf, "Loi binomiale (n=20, p=0.4)")

# 4. Loi de Poisson
mu = 5
x = np.arange(0, 20)
pmf = st.poisson.pmf(x, mu)
plot_discrete(x, pmf, "Loi de Poisson (mu=5)")

# 5. Loi de Zipf–Mandelbrot (zipfian)
a = 2
x = np.arange(1, 20)
pmf = st.zipf.pmf(x, a)
plot_discrete(x, pmf, "Loi de Zipf–Mandelbrot (zipfian)")


# Fonction pour tracer les lois continues
def plot_continuous(x, pdf, title):
    plt.figure(figsize=(6,4))
    plt.plot(x, pdf)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.savefig(f"{title}.png")
    plt.close()

# 1. Loi de Poisson 
mu = 5
x_poisson = np.arange(0, 20)
pmf_poisson = st.poisson.pmf(x_poisson, mu)

plt.figure(figsize=(6,4))
plt.stem(x_poisson, pmf_poisson)
plt.title("Loi de Poisson (discrète, mu=5)")
plt.xlabel("k")
plt.ylabel("P(X=k)")
plt.grid(True)
plt.savefig("Loi_de_Poisson_discrete.png")
plt.close()

# 2. Loi normale
mu, sigma = 0, 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
pdf = st.norm.pdf(x, mu, sigma)
plot_continuous(x, pdf, "Loi normale (mu=0, sigma=1)")

# 3. Loi log-normale
s = 0.954  # paramètre de forme (écart-type sur log)
x = np.linspace(0.01, 5, 200)  # commence à 0 car x>0 pour lognormale
pdf = st.lognorm.pdf(x, s)
plot_continuous(x, pdf, "Loi log-normale (s=0.954)")

# 4. Loi uniforme continue
a, b = 0, 10
x = np.linspace(a, b, 200)
pdf = st.uniform.pdf(x, a, b-a)
plot_continuous(x, pdf, "Loi uniforme continue [0,10]")

# 5. Loi du Chi-2 (chi-square)
df = 3  # degré de liberté
x = np.linspace(0, 15, 200)
pdf = st.chi2.pdf(x, df)
plot_continuous(x, pdf, "Loi du Chi-2 (df=3)")

# 6. Loi de Pareto
b = 2.62  # paramètre de forme
x = np.linspace(1, 5, 200)  # x >= 1 pour la loi de Pareto
pdf = st.pareto.pdf(x, b)
plot_continuous(x, pdf, "Loi de Pareto (b=2.62)")

# --- Définitions des fonctions pour moyenne et écart‑type ---

def uniforme_discrete_stats(a, b):
    n = b - a
    mean = (a + b - 1) / 2
    std = np.sqrt((n**2 - 1) / 12)
    return mean, std

def binomiale_stats(n, p):
    mean = n * p
    std = np.sqrt(n * p * (1 - p))
    return mean, std

def poisson_stats(mu):
    mean = mu
    std = np.sqrt(mu)
    return mean, std

def zipf_mandelbrot_stats(a, size=100000):
    r = st.zipf(a)
    data = r.rvs(size=size)
    return np.mean(data), np.std(data)

def normale_stats(mu, sigma):
    return mu, sigma

def lognormale_stats(s, scale=1):
    mean = np.exp(np.log(scale) + (s**2) / 2)
    variance = (np.exp(s**2) - 1) * np.exp(2*np.log(scale) + s**2)
    std = np.sqrt(variance)
    return mean, std

def uniforme_continue_stats(a, b):
    mean = (a + b) / 2
    std = (b - a) / np.sqrt(12)
    return mean, std

def chi2_stats(df):
    mean = df
    std = np.sqrt(2 * df)
    return mean, std

def pareto_stats(b, scale=1):
    mean = b * scale / (b - 1)
    variance = (b * scale**2) / ((b - 1)**2 * (b - 2))
    std = np.sqrt(variance)
    return mean, std


# --- Bloc principal pour afficher les résultats ---

if __name__ == "__main__":
    print("Dirac (point=3):", dirac_stats(3))
    print("Uniforme discrète [0..9]:", uniforme_discrete_stats(0, 10))
    print("Binomiale (n=20, p=0.4):", binomiale_stats(20, 0.4))
    print("Poisson (mu=5):", poisson_stats(5))
    print("Zipf–Mandelbrot (a=2):", zipf_mandelbrot_stats(2))
    print("Normale (mu=0, sigma=1):", normale_stats(0, 1))
    print("Log‑normale (s=0.954):", lognormale_stats(0.954))
    print("Uniforme continue [0,10]:", uniforme_continue_stats(0, 10))
    print("Chi‑2 (df=3):", chi2_stats(3))
    print("Pareto (b=2.62):", pareto_stats(2.62))
