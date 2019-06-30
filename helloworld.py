from sklearn import tree

features = [[150,0] , [170,0] , [140,1] , [130,1]]# 0 is bumpy and 1 is smooth
labels = [0,0,1,1]#0 is apple and 1 is orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features , labels)
print clf.predict([[150 , 0]])
