import time


def naive(pattern, text):
    pattern = pattern.replace('\n', '')
    text = text.replace('\n', '')
    m = len(pattern)
    n = len(text)

    for s in range(n - m + 1):
        if pattern == text[s: s + m]:
            print(f'pattern found at index {s}')


def rabin_karp(pattern, text, d=128, q=27077):
    pattern = pattern.replace('\n', '')
    text = text.replace('\n', '')
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    # Wyliczy h = (d to potęgi m - 1) modulo q
    for i in range(m - 1):
        h = (h * d) % q

    # Wyliczone: wartość p kodująca wzorzec
    # oraz       wartość t kodująca tekst
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if pattern == text[s:s + m]:
                print(f'pattern found at index {s}')
        if s < n - m:
            # Wylicza t kodujące o 1 znak dalej
            t1 = (ord(text[s]) * h) % q
            if t < t1:
                t += q
            t = (d * (t - t1) + ord(text[s + m])) % q


def prefix_function(pattern, m):
    pi = [0] * m
    k = 0

    for q in range(1, m - 1):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k

    return pi


def knuth_morris_pratt(pattern, text):
    pattern = pattern.replace('\n', '')
    text = text.replace('\n', '')
    m = len(pattern)
    n = len(text)
    pi = prefix_function(pattern, m)
    q = 0

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            print(f'pattern found at index {i - m + 1}')
            q = pi[q - 1]


f = open("text1.txt", "r")
text1 = f.read()
f.close()

f = open("text2.txt", "r")
text2 = f.read()
f.close()

f = open("pattern1.txt", "r")
pattern1 = f.read()
f.close()

f = open("pattern2.txt", "r")
pattern2 = f.read()
f.close()

f = open('times.txt', 'a')
start = time.time()
naive(pattern1, text1)
end = time.time()
f.write(str(end - start) + '\n')

start = time.time()
rabin_karp(pattern1, text1)
end = time.time()
f.write(str(end - start) + '\n')

start = time.time()
knuth_morris_pratt(pattern1, text1)
end = time.time()
f.write(str(end - start) + '\n')

start = time.time()
naive(pattern2, text2)
end = time.time()
f.write(str(end - start) + '\n')

start = time.time()
rabin_karp(pattern2, text2)
end = time.time()
f.write(str(end - start) + '\n')

start = time.time()
knuth_morris_pratt(pattern2, text2)
end = time.time()
f.write(str(end - start) + '\n\n')

f.close()
