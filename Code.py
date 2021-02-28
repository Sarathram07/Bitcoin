from prettytable import PrettyTable

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

from scipy import stats

from sklearn.linear_model import LinearRegression

x = PrettyTable()

import csv

with open('bitcoindataset1.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

month=[]
yr=[]
price=[]

n=len(data)
#print("Length of the given data:",n)

for i in range(1,n):
    month.append(float(data[i][0]))
    yr.append(float(data[i][1]))
    price.append(float(data[i][3]))
    
class Node:

    def __init__(self,yr,avg):

        self.left = None
        self.right = None
        self.yr = yr
        self.avg = avg
 
    def insert(self,yr,avg):
        if self.yr:
            if yr < self.yr:
                if self.left is None:
                    self.left = Node(yr,avg)
                else:
                    self.left.insert(yr,avg)
            elif yr > self.yr:
                if self.right is None:
                    self.right = Node(yr,avg)
                else:
                    self.right.insert(yr,avg)
        else:
            self.yr = yr

    def search(self,key):
        x = PrettyTable()
        x.field_names = [data[0][1],data[0][3]]
        if key < self.yr:
            return self.left.search(key)
        elif key > self.yr:
            return self.right.search(key)
        else:
            x.add_row([ self.yr,self.avg])
        return x
        del(x)

root=Node(month[1],price[1])
for i in range(0,n-1):
    root.insert(yr[i],price[i])

   
def menu():
    print("*****************   MAIN MENU   ********************")
    print()
    
    choice = int(input("""     Select a number from the given menu
                      1: Show data
                      2: Central tendency values of price
                      3: Correlation and Regression
                      4: Prediction and Hypothesis Testing
                      5: Search
                      6: Graph
                      7: Quit
                      

                      Please enter your choice: """))
    
    while(1):
        if choice == 1:
            print(" ")
            showdata()
            menu()
            
        elif choice ==2:
            print(" ")
            centraltendency()
            menu()
            
        elif choice ==3:
            print(" ")
            correg()
            menu()
            
        elif choice==4:
            print(" ")
            prediction()
            menu()
            
        elif choice==6:
            print(" ")
            main()
            
        elif choice==7:
            print(" ")
            print(" *****************  THANK YOU   *********************")
            exit(1)
            
        elif choice==5:
            print(" ")
            search()
            menu()
            
        else:
            print(" You are only allowed to select the given options ")
            print(" Please don't exceed limit ")
            print(" ")
            menu()
                                          
def showdata():
    x.field_names = (data[0][1], data[0][2], data[0][3])
    for i in range (1,n):
        x.add_row([data[i][1], data[i][2], data[i][3]])
    print(x)
    print("-------------------------------------------------------------------------------")

def search():
    a=data[1][1]
    b=data[n-1][1]
    find_yr=float(input("Enter a year between {}-{}:".format(a,b)))
    print(root.search(find_yr))
    print("-------------------------------------------------------------------------------")
    
def centraltendency():
    mean=np.mean(price)
    median=np.median(price)
    print("Mean:",mean)
    print("Median:",median)
    print("-------------------------------------------------------------------------------")

def estimate_coef(x, y): 
    n = np.size(x) 
    m_x, m_y = np.mean(x), np.mean(y) 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x  
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1)
    print("-------------------------------------------------------------------------------")

def correg():
    cov=0.0
    mx=0.0
    my=0.0
    mx2=0.0
    b=0.0
    a=0.0
    mx=np.mean(month)
    my=np.mean(price)
    for i in range(len(price)):
         cov=cov+((month[i]-mx)*(price[i]-my))
         mx2=mx2+((month[i]-mx)**2)
    b=cov/mx2
    a=my-b*mx
    print("y = {} + {}x".format(a,b))
    print("-------------------------------------------------------------------------------")

def prediction():
    cov=0.0
    mx=0.0
    my=0.0
    mx2=0.0
    b=0.0
    a=0.0
    y=0.0
    mx=np.mean(month)
    my=np.mean(price)
    for i in range(len(price)):
         cov=cov+((month[i]-mx)*(price[i]-my))
         mx2=mx2+((month[i]-mx)**2)
    b=cov/mx2
    a=my-b*mx
    yy=int(input("Enter the year : "))
    mm=int(input("Enter the month: "))    
    ye=((yy-2010)*12)+mm
    y=a+b*ye

    #print(y,a,b)
    print("The predicted price of the year {} is: {}".format(yy,y))
    print("-------------------------------------------------------------------------------")
    print(" ")
    
    print(" ------------------------ HYPOTHESIS TESTING ------------------------ ")
    sd=np.std(price)
    obs=(n-1)
    n2=obs**0.5
    z=abs(y-my)/(sd/n2)
    #print(z)
    print("we have taken the 5% level of significance")
    print(" ")
    print("z-table=1.645")
    print(" ")
    print("The Hypothesis value is: %f"%(z))
    print(" ")
    val=1.645
    if val>z:
     print("We ACCEPT the Null Hypothesis")
     print("Result: The predicted value is Wrong")
    else:
     print("We REJECT the Null Hypothesis")
     print("Result: The predicted value is Correct")
     print("-------------------------------------------------------------------------------")
    

def main(): 
    data=pd.read_csv('bitcoindataset1.csv')
    #print("\n",data)
    x = data.Slno.values
    y = data.Average.values
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {}  \  \nb_1 = {}".format(b[0], b[1])) 
    plot_regression_line(x, y, b) 
    print("-------------------------------------------------------------------------------")

def plot_regression_line(x, y, b): 
    plt.scatter(x, y, color = "m", 
               marker = "o", s = 30)
    y_pred = b[0] + b[1]*x 
    plt.plot(x, y_pred, color = "g") 
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.show()
    print("-------------------------------------------------------------------------------")
    menu()
    
        
menu()
