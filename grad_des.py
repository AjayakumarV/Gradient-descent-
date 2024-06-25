import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


p= pd.read_csv('c:\\Users\\ajayakumar.vijayakum\\Desktop\\aj practise\\insurance.csv')
x=np.array(p['age'])
y=np.array(p['charges'])

m_curr=b_curr=0
iterations=10000
n= len(x)
learning_rate = 0.0001
    
for i in range(iterations):
    y_predicted=m_curr * x + b_curr
    cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
    md = -(2/n) * sum(x*(y-y_predicted))
    bd = -(2/n) * sum(y-y_predicted)
    m_curr = m_curr - learning_rate * md   
    b_curr = b_curr - learning_rate * bd
        
    print(f"m {m_curr}, b {b_curr}, cost {cost}, iteration {i}")

plt.scatter(x,y)
plt.xlabel('age')
plt.ylabel('charges')
plt.title(f'm {m_curr}, b {b_curr}, cost {cost}, iteration {i}')
plt.show()





