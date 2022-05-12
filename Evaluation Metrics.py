
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print("acc: ", acc)


from sklearn.metrics import precision_score
pr = precision_score(pred, labels_test)
print("precision_score ", pr)


from sklearn.metrics import  recall_score
rec = recall_score(pred, labels_test)
print("recall_score", rec)

