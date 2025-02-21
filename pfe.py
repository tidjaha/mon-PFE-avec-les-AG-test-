import numpy as np
import random


mat=np.array(([398.83,702.56,1.00,568.83],[423.97,717.72,1.00,594.70],[447.31,730.12,1.00,617.70]), float)
m=3 #taille des données
#print(mat)
#co3=[[0.679043245,0.625996619,-142.8883032],[0.598162889,0.800450995,-233.5524498],[0.76264064,0.218254937,124.8496426],[0.022871665,3.563532402,-2058.456036],[-4.510869565,34.49516908,-23832.79541]]
co3=np.array(([0.6,0.6,-142],[0.5,0.8,-233],[0.02,3.5,-2058],[-4.5,34.49,-23832]),float)
l=len(co3) #taille des coef
limit=np.array(range(3*2), float)
limit=limit.reshape(3,2)
#print(limit)
co0=np.array(range(l), float)
co1=np.array(range(l), float)
co2=np.array(range(l), float)

#print(limit)
pop=0
maxfit=np.array(range(l), float)
for i in range(l):
    maxfit[i]=random.random()*10
#print(maxfit)
fit=np.array(range(l*m),float)
fit=fit.reshape(l,m)
#print(fit)
#print(max)
for i in range(l):
    for j in range(m):
        fit[i][j] = ((co3[i][0]*mat[j][0]+co3[i][1]*mat[j][1]+co3[i][2])-mat[j][3])**2
r=0
    #print(fit)
fit=np.absolute(fit)
for i in range(l):
        maxfit[i]=np.max(fit[i])
index=np.where(maxfit==min(maxfit))
best=int(index[0])
limit[0][0]=co3[best][0]*10
limit[0][1]=co3[best][0]/10
limit[1][0]=co3[best][1]*10
limit[1][1]=co3[best][1]/10
limit[2][0]=co3[best][2]*10
limit[2][1]=co3[best][2]/10
if l<200:
  l=l+1
  for i in range(l,2001):
    co3=np.vstack((co3,co3[best]))
while min(maxfit)>0.1:
#for i in range(50):
        #clacul du fitmax
    l=len(co3) #taille des coef
    r=0
#print(fit)>
    maxfit=np.array(range(l), float)
    for i in range(l):
        maxfit[i]=random.random()*10
#print(maxfit)
    fit=np.array(range(l*m),float)
    fit=fit.reshape(l,m)
    n=0
        #print(fit)
    for i in range(l):
        for j in range(m):
            fit[i][j] = ((co3[i][0]*mat[j][0]+co3[i][1]*mat[j][1]+co3[i][2])-mat[j][3])**2
        r=0
    #print(fit)
    fit=np.absolute(fit)
    for i in range(l):
        maxfit[i]=np.max(fit[i])
    #print(maxfit)
    #print(co3)
        # selection
    ps=np.array(range(l), float)
    qs=np.array(range(l), float)
    smax=np.sum(maxfit)
    for i in range(l):
        ps[i]=maxfit[i]/smax
            #print(ps)
    qs[0]=ps[0]
    for j in range(l-1):
        qs[j+1]=qs[j]+ps[j+1]
            #print(qs)
            #print(ps)
    rs=np.array(range(l), float)
    for i in range(l):
        rs[i]=random.random()
            #print(r
    #print(maxfit)
    #print(rs)
    #print(qs)
    minimum=min(maxfit)
    #print("minimum=",minimum)
    for i in range(l):
        for j in range(l):
            if rs[i]<qs[j]:
                    if maxfit[j]>maxfit[i]:
                         co3[j]=co3[i]
                                                 #print(co3)
    #print(co3)  #print(maxfit)
    l=len(co3)
    #print("lavaleur de l = ",l)
                    #croisement
    rc=np.array(range(l), float)
    rcs=np.array(range(3), float)
    for i in range(l):
        rc[i]=random.random()
    for i in range(3):
        rcs[i]=random.random()
            #print(rc)
            #print(rcs)
    indexrc=np.where(rc>0.75) #àvoir si il ne faut pas l'augmenter ou la reduire conseiller 0.75
    indexrcs=np.where(rcs>0.75)
    longrc=(len(indexrc[0]))//2
    #rcc=random.random()
    #print(longrc)
    longrcs=len(indexrcs[0])
    #print(longrcs)
    h=0
    #print(indexrc)
    #print(indexrcs)
    inrc=indexrc[0]
    inrcs=indexrcs[0]
    testco3=np.copy(co3)
    #print(inrc)
    #print(inrcs)
    #print(rcc)
    for i in range(longrc):
        for j in range(longrcs):
            inter=co3[inrc[h]][inrcs[j]]
            co3[inrc[h]][inrcs[j]]=co3[inrc[h+1]][inrcs[j]]
            co3[inrc[h+1]][inrcs[j]]=inter
        h=h+2
    #print(co3)
    #recalcul du fitmax
            #mutation
    rm=np.array(range(l*m), float)
    for i in range(l*m):
        rm[i]=random.random()
    rm=rm.reshape(l,m)
    #print(rm)
    #print(" valeurs de rm",rm)
    #maxrm=np.max(rm)
    #testco=np.copy(co3)
    #testfit=np.copy(fit)
    #testmaxfit=np.copy(maxfit)
    for i in range(l):
        for j in range(3):
            if rm[i][j]<0.75:
                co3[i][j]=random.uniform(limit[j][1],limit[j][0])
                #print("valeur random =",co3[i][j])
                #recacalcul du maxfit
    maxfit=np.array(range(l), float)
    for i in range(l):
        maxfit[i]=random.random()*10
#print(maxfit)
    fit=np.array(range(l*m),float)
    fit=fit.reshape(l,m)
    r=0
    #print(fit)
    n=0
        #print(fit)
    for i in range(l):
        for j in range(m):
            fit[i][j] = ((co3[i][0]*mat[j][0]+co3[i][1]*mat[j][1]+co3[i][2])-mat[j][3])**2
            n=n+1
        r=0
    fit=np.absolute(fit)
    for i in range(l):
        maxfit[i]=np.max(fit[i])
    max=min(maxfit)
    print("minfit=", max)
    #print("co=", co3)
    pop=pop+1
    print("pop = ",pop)
    be=np.min(maxfit)
    #for i in range(100000000):
       # r=r+1
be=np.min(maxfit)
best=np.where(maxfit==be)
print(best)
print(co3[best[0][0]])



        #my_wb.save("sample_data3.xlsx")
        #print(co)
