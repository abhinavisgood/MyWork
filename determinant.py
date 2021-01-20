import numpy as np
import random 
def inara(a):
    print('Before that please enter the matrix : ')
    asl=np.ones((a,a),dtype=float,order='C')
    for i in range(a):
        for j in range(a):
            asl[i][j]=float(random.randrange(99999999,999999999))
    print(asl)
    return asl
def det(a1):
   ''' if(a1.shape[0]>3):
        
        mpp=det(np.delete(np.delete(a1,[0,a1.shape[0]-1],0),[0,a1.shape[0]-1],1))
        ulp=det(np.delete(np.delete(a1,a1.shape[0]-1,0),a1.shape[0]-1,1))
        urp=det(np.delete(np.delete(a1,a1.shape[0]-1,0),0,1))
        llp=det(np.delete(np.delete(a1,0,0),a1.shape[0]-1,1))
        lrp=det(np.delete(np.delete(a1,0,0),0,1))
        if (mpp==0):
            return 0
        a=0.0
        a=(1/mpp)*(ulp*lrp-urp*llp)                                       
        return a '''                                                           
   if(a1.shape[0]>2):
        a=0.0
        for i in range(a1.shape[0]):
            a=a+a1[0][i]*((-1)**i)*det(np.delete(np.delete(a1,0,0),i,1))
        return a
   elif a1.shape[0]==2:
        asd=0.0
        asd=a1[0][0]*a1[1][1]-a1[0][1]*a1[1][0]
        return asd
   else :
        a=int(a1)
        return a
        
x=int(input('Enter the order of the array: '))

print(det(inara(x)))

