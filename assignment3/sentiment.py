import sys
import os
import string

# NOTE: Python 2 :)

def getVocab(data):
	result = set()
	for line in data:
		temp = line.split()
		for word in temp:
			result.add(word)

	return sorted(result)

def getData(fileName):
	data = []
	dataTruth = []
	deleteChars = string.punctuation + "1234567890"
	with open(fileName) as f:
		training = f.readlines()

	for line in training:
		temp = line.split('\t')

		data.append(temp[0].translate(None, deleteChars).lower())
		dataTruth.append(temp[1].strip())

	dataTruth = list(map(int, dataTruth))
	return data, dataTruth

def buildFeatureVector(vocab, sentences, truth):
	result = []

	truthIndex = 0

	for s in sentences:
		sentence = s.split()
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
		for i in feature:
			trainFile.write(str(i) + ",")
		trainFile.write("\n")

	for feature in test:
		for i in feature:
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

if __name__ == "__main__":
	main(sys.argv)
