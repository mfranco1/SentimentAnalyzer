import codecs
import nltk
import pickle

word_features = ""

def split_training_data(content):
    data = []
    for line in content:
        try:
            sentiment, text = line.split('|')
            words = [w.lower() for w in text.split() if len(w) > 2]
            data.append((words, sentiment))
        except ValueError:
            pass
    return data

def get_words(training_data):
    all_words = []
    for (words, sentiment) in training_data:
        all_words.extend(words)
    return all_words

def get_word_features(all_words):
    all_words2 = nltk.FreqDist(all_words)
    word_features2 = all_words2.keys()
    return word_features2

def extract_features(words):
    unique_words = set(words)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in unique_words)
    return features

def save_classifier(classifier):
    f = open('db/naive_bayes_classifier2.pickle', 'wb')
    pickle.dump(classifier, f)
    f.close()
    return "Successfully saved classifier!"

def main():
    with codecs.open('res/training_data2.txt', 'r', encoding='utf8', errors='replace') as f:
        raw_content = [x.strip('\n') for x in f.readlines()]

    training_data = split_training_data(raw_content)
    global word_features
    word_features = get_word_features(get_words(training_data))
    training_set = nltk.classify.apply_features(extract_features, training_data)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print(classifier.show_most_informative_features(30))
    print(save_classifier(classifier))


if __name__ == "__main__":
    main()
