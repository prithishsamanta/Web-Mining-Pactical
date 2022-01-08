import numpy as np
 
dimension = input('Enter no of terms: ')
q = []
for i in range(int(dimension)):
    q.append(input('Enter q ' + str(i + 1) + ': '))
drNo = input('Enter no of relevent docs: ')
dr = []
for i in range(int(drNo)):
    for j in range(int(dimension)):
        dr.append(input('Enter dr ' + str(i + 1) + ' ' + str(j + 1) + ': '))
dnNo = input('Enter no of non relevent docs: ')
dn = []
for i in range(int(dnNo)):
    for j in range(int(dimension)):
        dn.append(input('Enter dn ' + str(i + 1) + ' ' + str(j + 1) + ': '))
alpha = input('Enter alpha: ')
beta = input('Enter beta: ')
gamma = input('Enter gamma: ')
alphaQ = []
for i in q:
    alphaQ.append(float(i)*float(alpha))
betaQ = []
# betaQ = np.sum(dr, axis=0)
# for i in betaQ:
#     i = float(i)*float(beta)
for i in range(int(dimension)):
    sum = 0
    for j in range(int(drNo)):
        sum += int(dr[i][j])
    sum /= float(drNo)
    betaQ.append(sum * float(beta))
gammaQ = []
# gammaQ = np.sum(dn, axis=0)
# for i in gammaQ:
#     i = float(i)*float(gamma)
for i in range(int(dimension)):
    sum = 0
    for j in range(int(dnNo)):
        sum += int(dn[i][j])
    sum /= float(dnNo)
    gammaQ.append(sum * float(gamma))
qNew = []
print(alphaQ)
print(betaQ)
print(gammaQ)
 
for i in range(int(dimension)):
    qNew.append(alphaQ[i] + betaQ[i] - gammaQ[i])
print("qNew = ", qNew)
