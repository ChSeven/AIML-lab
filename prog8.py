from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
iris=datasets.load_iris()
print("iris data")
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.1)
print("training data and value",x_train.shape,y_train.shape)
print("test data and value",x_test.shape,y_test.shape)
classifier=KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print("result of the classification")
for r in range(0,len(x_test)):
    print("sample:",str(x_test[r]),"actual:",str(y_test[r]),"predicted:",str(y_pred[r]))
print("accuracy is",classifier.score(x_test,y_test));   
