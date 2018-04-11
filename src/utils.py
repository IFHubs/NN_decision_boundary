#!/usr/bin/env python
from sklearn.datasets import make_classification
import sklearn
import numpy 
import pylab
import random
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import LinearSVC, SVC
from sklearn.model_selection import cross_val_score

# This binary classification should be linear separable
def play_iris():
	data = load_iris()
	feature = data.data
	label = data.target
	label[label==2]=1
	# clf = LinearSVC(random_state=0)
	clf = SVC(kernel='linear')
	clf.fit(feature, label)
	scores = cross_val_score(clf, feature, label, cv=5)


def generate_lin_spe():
	separable = False
	while not separable:
	    samples = make_classification(n_samples=100, n_features=2, 
	    	n_redundant=0, n_informative=1, n_clusters_per_class=1, flip_y=-1)
	    red = samples[0][samples[1] == 0]
	    blue = samples[0][samples[1] == 1]
	    separable = any([red[:, k].max() < blue[:, k].min() or 
	    	red[:, k].min() > blue[:, k].max() for k in range(2)])
	plt.plot(red[:, 0], red[:, 1], 'r.')
	plt.plot(blue[:, 0], blue[:, 1], 'b.')
	plt.show()

def lin_sep_with_ground_truth():
	x = np.random.rand(100)
	y = np.random.rand(100)
	z = x+y
	ind_1 = np.where(z>1.2)[0]
	ind_2 = np.where(z<0.8)[0]

	pylab.scatter(list(x[ind_1])+[0.4,0.8, 0.75],
		list(y[ind_1])+[0.8, 0.4, 0.45])
	pylab.scatter(list(x[ind_2])+[0.4, 0.3, 0.2],
		list(y[ind_2])+[0.4, 0.5, 0.6])
	pylab.plot([0, 1.2], [1.2, 0])
	pylab.plot([0, 0.8], [0.8, 0])
	pylab.xlim(0,1)
	pylab.ylim(0,1)
	pylab.savefig('svm_original.png',dpi=300, bbox_inches='tight')
	pylab.show()