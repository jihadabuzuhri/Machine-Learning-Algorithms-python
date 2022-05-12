from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training sets
model.fit(features,label)

#Predict Output

predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print(predicted)

from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(pred2, labels_test)

