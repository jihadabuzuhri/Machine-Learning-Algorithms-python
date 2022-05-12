
from sklearn.naive_bayes import GaussianNB
### create classifier
clf = GaussianNB()
### fit the classifier on the training features and labels
clf.fit(features_train, labels_train)
### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)




def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    import numpy as np

    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)
    
    #print(features_train)
    #print(labels_train)
    #print(features_test)
    #print(labels_test)

    labels_test = np.array(labels_test)
    print(labels_test)
    
    print("################################################################")
    
    print(pred)

    
    c = float(0)

    for i in range(len(pred)):
        if pred[i] == labels_test[i]:
            c = c + 1
    
    
    print (labels_test.__len__())
    print (c)
    
    accuracy = c  / labels_test.__len__()
    
    
    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    from sklearn.metrics import accuracy_score
    #accuracy = accuracy_score(pred, labels_test)
    print("################################################################")
    return accuracy
