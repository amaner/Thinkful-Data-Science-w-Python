# knn.py

import csv
import random
import math
import operator

# load the iris data set into a training and a test set
# do this randomly, using a provided split ratio
def load_iris(filename, split_ratio, train=[], test=[]):
	with open(filename, 'rb') as input_file:
		lines = csv.reader(input_file)
		# convert csv.reader object to a list
		data = list(lines)
		# loop through each row in the list
		for i in range(len(data)-1):
			# convert first 4 columns to float
			for j in range(4):
				data[i][j] = float(data[i][j])
			# randomly split according to split_ratio
			if random.random() < split_ratio:
				train.append(data[i])
			else:
				test.append(data[i])

# calculate the euclidean distance between two points in d-space
def euclidean_distance(a, b, d):
	# init distance to 0
	dist = 0
	# sum up the squared coordinate diffs
	for i in range(d):
		dist += pow((a[i]-b[i]),2)
	# take the square root
	return math.sqrt(dist)

# get the k nearest neighbors
def get_knn(train, tval, k):
	dists = []
	# first 4 entries are numeric, last is str - the flower type
	length = len(tval)-1
	# loop through all points in the training set
	for i in range(len(train)):
		dist = euclidean_distance(tval, train[i], length)
		dists.append((train[i], dist))
	# sort by distance
	dists.sort(key=operator.itemgetter(1))
	# empty list for the k neareast neighbors
	neighbors = []
	# tack on the k nearest neighbors
	for i in range(k):
		neighbors.append(dists[i][0])
	return neighbors

# get the majority class for the set of k nearest neighbors
def get_majority_class(neighbors):
	# empty dictionary for the class votes
	class_votes = {}
	# loop through each row in the k nearest neighbors
	# and find which class it is
	for i in range(len(neighbors)):
		# vote is the last entry in the row
		vote = neighbors[i][-1]
		# tabulate the votes
		# first, if we've already gotten a vote for the given class
		# then just increment its number of votes by 1
		if vote in class_votes:
			class_votes[vote] += 1
		# but if this is the first vote, we set the key,value pair to be vote,1
		else:
			class_votes[vote] = 1
		# now sort the votes in descending order (so the majority class is first)
	sorted_votes = sorted(class_votes.iteritems(), key=operator.itemgetter(1), reverse=True)
	# return the first entry - the majority class
	return sorted_votes[0][0]

# loop through the test set and predict flower types
def predict_classes(test, train, k):
	preds = []
	for i in range(len(test)):
		neighbors = get_knn(train,test[i],k)
		result = get_majority_class(neighbors)
		preds.append(result)
		# print "predicted= " + repr(result) + ", actual= " + repr(test[i][-1])
	return preds

# calc_acc calculates the accuracy of our predictions
# test is the test set, predictions is a set of predictions made
# by our knn algorithm
def calc_acc(test, preds):
	# initialize the count of correct predictions to 0
	correct = 0
	# loop through each element in the test set
	for i in range(len(test)):
		# if the last entry - the flower type - is the same as
		# our prediction, then increment correct by 1
		if test[i][-1] == preds[i]:
			correct += 1
	# return the percentage of correct predictions
	return (correct/float(len(test))) * 100.0

def main():
	train = []
	test = []
	split_ratio = 0.67
	load_iris('iris.txt',split_ratio,train,test)
	print "Train set length: " + repr(len(train))
	print "Test set length: " + repr(len(test))
	k = int(input("Enter a value for k: "))
	preds = predict_classes(test, train, k)
	accuracy = calc_acc(test, preds)
	print "Accuracy of predictions: " + repr(accuracy) + "%"

main()
