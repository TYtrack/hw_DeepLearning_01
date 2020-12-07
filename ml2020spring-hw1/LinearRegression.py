import numpy as np


class LinearRegression():

    def __init__(self):

        self.coef=0.0
        self.intercept=0.0
        self.theta=None

    def __hypotheis(self,x):
        res=np.dot(self.theta,x)+self.intercept
        return res

    def __decal_error(self,x,y):

        return self.__hypotheis(x)-y

    def fit(self,x,y):
        self.m=x.shape[0]
        self.x=x
        self.y=y
        self.theta=np.zeros(x[0].size)
        self.__gradient_descent()
        self.coef=self.coef

    def predict(self,x):
        y=[]
        cost=0
        for i in x:
            y.append(self.__hypotheis(i))

        return y


    def __gradient_descent(self):
        cost=10000000.0
        threshold=0.001
        learing_rate=0.5
        count=0
        while cost>threshold:
            self.theta=self.theta-learing_rate*self.__partialderiv_theta()
            self.intercept=self.intercept-learing_rate*self.__partialderiv_intercept()
            cost=self.__Jfunction()

            if count%10==0:
                print("Loss count:   ",cost)
            count+=1



    def __Jfunction(self):
        sum=0.0
        for i in range(self.m):
            temp=self.__decal_error(self.x[i],self.y[i])
            sum+=np.dot(temp,temp)
        return sum/(2*self.m)

    def __partialderiv_theta(self):

        sum=0
        for i in range(self.m):
            temp=self.__decal_error(self.x[i],self.y[i])
            sum+=np.dot(temp,self.x[i])
        return sum/self.m

    def __partialderiv_intercept(self):

        sum=0
        for i in range(self.m):
            temp=self.__decal_error(self.x[i],self.y[i])
            sum+=temp
        return sum/self.m










