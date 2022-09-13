def suma(l, m, primo): return [(l[i] + m[i]) % primo for i in range (0,len(l))]
def resta(l, m, primo):return [(l[i] - m[i]) % primo for i in range (0,len(l))]
def reducir(pol,t,p):
    signo = -1
    sol=[0]*t
    for i in range(0, len(pol)):
        signo = -signo if i%t == 0 else signo
        sol[i % t] = (sol[i % t] + signo * pol[i]) %p
    return sol[:t]
def fft(pol, pot_xi,p):# pol es un polinomio que tiene como coeficientes polinomios en R[u]/<u^2n1+1> y es de grado < n2 , xi = u ^pot_xi
    n2 = len(pol)
    _2n1 = len(pol[0])
    if n2 == 1:
        return pol
    p_even = [[0]*_2n1] * (n2//2)
    p_odd  = [[0]*_2n1] * (n2//2)
    for i in range(n2//2):
        p_even[i] = pol[2*i]
        p_odd[i] = pol[2*i+1]
    a_even = fft(p_even, pot_xi*2, p)
    a_odd  = fft(p_odd, pot_xi*2, p)
    a = [[0]*_2n1] * n2
    for i in range(n2//2):
        a[i] = suma(a_even[i], reducir([0]*(pot_xi*i) + a_odd[i], _2n1, p), p)
        a[i+n2//2] = resta( a_even[i], reducir([0]*pot_xi*i + a_odd[i], _2n1, p), p)
    return a
def ifft(a, menos_pot, primo, k):
    inverso = 2**((primo-k-1)) % primo
    # inverso = pow(len(a), -1, p)
    sol = fft(a, menos_pot, primo)
    return [ [(y * inverso) % primo for y in x] for x in sol]
def mult_ss_mod(f,g,k,p):
	k1 = k//2
	k2 = k-k1
	n1,n2,n = pow(2,k1),pow(2,k2),pow(2,k)
	if k == 0:
		return [f[0] * g[0] % p]
	elif k == 1:
		return [(f[0] * g[0] - f[1] * g[1]) % p, (f[0] * g[1] + f[1] * g[0]) % p]
	elif k == 2: 
		return [(f[0] * g[0] - f[1] * g[3] - f[2] * g[2] - f[3] * g[1]) % p,
			(f[0] * g[1] + f[1] * g[0] - f[2] * g[3] - f[3] * g[2]) % p,
			(f[0] * g[2] + f[1] * g[1] + f[2] * g[0] - f[3] * g[3]) % p,
			(f[0] * g[3] + f[1] * g[2] + f[2] * g[1] + f[3] * g[0]) % p]
	exp_xi = (2*n1)//n2 
	a_fTilda = [ reducir(([0] * exp_xi * i) + f[n1*i : n1*i+n1 ] + ([0]*n1), 2*n1, p) for i in range (n2)]
	a_gTilda = [ reducir(([0] * exp_xi * i) + g[n1*i : n1*i+n1 ] + ([0]*n1), 2*n1, p) for i in range (n2)]
	fft1 = fft(a_fTilda, 2*exp_xi, p)
	fft2 = fft(a_gTilda, 2*exp_xi, p)
	f_g = [mult_ss_mod(fft1[i], fft2[i], k1+1, p) for i in range (n2)] 
	fft_inv = ifft(f_g, 4*n1 - 2*exp_xi ,p, k2) 
	h_tilda =  [ reducir(([0] * 4*n1 - (exp_xi*i)) + fft_inv[i], 2*n1, p) for i in range (n2)]
	h = [0]*n
	for i in range(n2):
		for j in range(2*n1):
			h[(n1*i+j) % n] = (h[(n1*i+j) % n] + h_tilda[i][j])%p if ((n1*i+j) // n)%2 == 0 else  (h[(n1*i+j) % n] - h_tilda[i][j])%p
	return h
def mult_pol_mod(f,g,p):
	grado = len(f)-1 + len(g)-1
	n = 1 
	k = 0
	while grado >= n:
		n *= 2
		k += 1
	f = f + [0] * (n-len(f))
	g = g + [0] * (n-len(g))
	return quitar_ceros(mult_ss_mod(f, g, k, p))
def quitar_ceros(lista):
    while lista and lista[-1] == 0:
        lista.pop()
    return lista

#p=5
#k=9
#d=2**k
#ini=time.time()
#print(mult_ss_mod ([1] * d,[p-1,0,1] + [0] * (d-3),k,p),time.time()-ini)