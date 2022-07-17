y=np.array(tseries[1,:], dtype='complex')
t=np.array(tseries[0,:], dtype='complex')

def FourierRiemann(y,t):
    T=np.max(t)

    omega=np.array(2*np.pi/T*np.arange(t.shape[0]),dtype='complex')
    a=np.zeros_like(omega)
    for na in range(omega.shape[0]):
        w=omega[na]
        a[na] = np.sum(np.exp(-1j*w*t)*y)/np.sqrt(y.shape[0])
    return a

a=FourierRiemann(y,t)

def IFourierRiemann(a,t):
    T=np.max(t)
    omega=np.array(2*np.pi/T*np.arange(a.shape[0]),dtype='complex')
    
    yre=np.zeros_like(t)    
    na=0
    for lt in t:
        yre[na]=np.sum(np.exp(1j*omega*lt)*a)/np.sqrt(a.shape[0])
        na +=1
    
    return yre

yre=IFourierRiemann(a,t)
