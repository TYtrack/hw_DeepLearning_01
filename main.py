import LinearRegression as us

plt.title("Toy Dataset")
X1, Y1 = make_regression(n_samples=100000, n_features=100, n_informative=80, n_targets=1,noise=0.5)

X1_train = X1[:-10000]
Y1_train = Y1[:-10000]


X1_test = X1[-10000:]
Y1_test = Y1[-10000:]
our_rg = us.LinearRegression()
our_rg.fit(X1_train, Y1_train)
our_Y1_pred = our_rg.predict(X1_test)
our_Y1_fit = our_rg.predict(X1_train)

def count_predict_Loss(y,target):
    sum=0
    for i in range(len(y)):
        sum+=(y[i]-target[i])**2
    return sum/len(y)

train_loss=count_predict_Loss(our_Y1_fit,Y1_train)
test_loss=count_predict_Loss(our_Y1_pred,Y1_test)

print("train_loss:   ",train_loss)
print("test_loss:   ",test_loss)


print(our_rg.theta)

