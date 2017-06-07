from __future__ import division
import sys
import os
import string



# NOTE: Python 2 :)

def getVocab(data):
	result = set()
	for line in data:
		for word in line:
			result.add(word)

	return sorted(result)


def assign_vocab_probabilities(vocab, training, truth):

	true_records = 0
	false_records = 0

	for value in truth:
		if value == 1:
			true_records += 1
		else:
			false_records += 1

	result = {}

	for index, entry in enumerate(vocab):

		true_true_word_count = 0
		false_true_word_count = 0

		false_false_word_count = 0
		true_false_word_count = 0

		for sentence in training:

			if sentence[index] == 1:
				if sentence[-1] == 1:
					true_true_word_count += 1
				else:
					true_false_word_count += 1
			else:
				if sentence[-1] == 1:
					false_true_word_count += 1
				else:
					false_false_word_count += 1


		probabilities = (true_true_word_count/true_records, false_true_word_count/true_records, true_false_word_count/false_records, false_false_word_count/false_records)

		result[entry] = probabilities

	# print(result)
	return result, (true_records / len(truth), false_records / len(truth))

def testing_phase(sentences, trained_vocab, probabilities, vocab):
	result = []

	prob_class_true = probabilities[0]
	prob_class_false = probabilities[1]
	print(prob_class_true, prob_class_false)
	for sentence in sentences:
		prob_true = prob_class_true
		for index, word in enumerate(sentence):
			if vocab[index] in trained_vocab:
				# print("hello?")
				if word == 1:
					prob_true *= trained_vocab[vocab[index]][0]
				else:
					prob_true *= trained_vocab[vocab[index]][1]

		prob_false = prob_class_false
		for index, word in enumerate(sentence):
			if vocab[index] in trained_vocab:
				if word == 1:
					prob_false *= trained_vocab[vocab[index]][2]
				else:
					prob_false *= trained_vocab[vocab[index]][3]

		# print(prob_true, prob_false)
		if prob_true >= prob_false:
			result.append(1)
		else:
			result.append(0)

	return result

def check_accuracy(calculated_truth, real_truth):
	correct = 0

	for i in range(len(real_truth)):
		if calculated_truth[i] == real_truth[i]:
			correct += 1

	return correct / len(real_truth)

def getData(fileName):
	data = []
	dataTruth = []
	deleteChars = string.punctuation + "1234567890"
	with open(fileName) as f:
		training = f.readlines()

	for line in training:
		temp = line.split('\t')

		data.append(temp[0].translate(None, deleteChars).lower().split())
		dataTruth.append(temp[1].strip())

	dataTruth = list(map(int, dataTruth))
	return data, dataTruth

def buildFeatureVector(vocab, sentences, truth):
	result = []

	truthIndex = 0

	for sentence in sentences:
		# feature vector of size M+1, where M is the size of the vocab
		temp = [0 for _ in range(len(vocab))]
		for word in sentence:
			if word in vocab:
				try:
					index = vocab.index(word)
				except:
					continue

			temp[index] = 1

		temp[len(vocab) - 1] = truth[truthIndex]
		result.append(temp)
		truthIndex += 1

	return result

def outputPreprocess(vocab, train, test):
	os.system('rm preprocessed_train.txt')
	os.system('rm preprocessed_test.txt')

	trainFile = open("preprocessed_train.txt", 'w')
	testFile = open("preprocessed_test.txt", 'w')

	for word in vocab:
		trainFile.write(word + ",")
		testFile.write(word + ",")

	trainFile.write("classlabel\n")
	testFile.write("classlabel\n")

	for feature in train:
		for idx, i in enumerate(feature):
			if idx == len(feature) - 1:
				trainFile.write(str(i))
			else:
				trainFile.write(str(i) + ",")
		trainFile.write("\n")

	for feature in test:
		for idx, i in enumerate(feature):
			if idx == len(feature) - 1:
				testFile.write(str(i))
			else:
				testFile.write(str(i) + ",")
		testFile.write("\n")

def main(args):
	vocab = []
	trainingWords = []
	testingWords = []
	trainingTruth = []
	testingTruth = []
	training = []
	testing = []

	trainingSentences, trainingTruth = getData(args[1])

	testingSentences, testingTruth = getData(args[2])

	vocab = getVocab(trainingSentences)

	training = buildFeatureVector(vocab, trainingSentences, trainingTruth)

	testing = buildFeatureVector(vocab, testingSentences, testingTruth)

	outputPreprocess(vocab, training, testing)

	trained_vocab, (p_class_1, p_class_0) = assign_vocab_probabilities(vocab, training, trainingTruth)
	# print trained_vocab

	training_classification = testing_phase(training, trained_vocab, (p_class_1, p_class_0), vocab)
	print(training_classification)
	print(trainingTruth)
	testing_classification = testing_phase(testing, trained_vocab, (p_class_1, p_class_0), vocab)

	result1 = check_accuracy(training_classification, trainingTruth)
	result2 = check_accuracy(testing_classification, testingTruth)

	print(result1, result2)

if __name__ == "__main__":
	main(sys.argv)
