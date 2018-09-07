import codecs
import nltk
import pickle
import trainer

word_features = ""

def parse_raw_content(content):
    texts, dates, locations, urls = ([], [], [], [])
    for line in content:
        try:
            text, date, loc, url = line.split('|')
            texts.append(text)
            dates.append(date)
            locations.append(loc)
            urls.append(url)
        except ValueError:
            pass
    return texts, dates, locations, urls

def load_classifier():
    f = open('db/naive_bayes_classifier.pickle', 'rb')
    classifier = pickle.load(f)
    f.close()
    return classifier

def classify_texts(texts, classifier, dates):
    data = []
    for text, date in zip(texts, dates):
        sentiment = classifier.classify(trainer.extract_features(text.split()))
        data.append((text, sentiment, date))
    return data

def store_classified_text(texts):
    f = codecs.open('db/classified_texts.txt', 'a', encoding='utf8')
    for text, sentiment, date in texts:
        f.write("|".join([text, sentiment, date]) + "\n")
    f.close()

def main():
    with codecs.open('res/raw_twitter_data.txt', 'r', encoding='utf8', errors='replace') as f:
        raw_content = [x.strip('\n') for x in f.readlines()]
    
    with codecs.open('res/training_data.txt', 'r', encoding='utf8', errors='replace') as f2:
        raw_content2 = [x.strip('\n') for x in f2.readlines()]

    texts, dates, locations, urls = parse_raw_content(raw_content)
    classifier = load_classifier()

    training_data = train.split_training_data(raw_content2)
    global word_features
    word_features = trainer.get_word_features(trainer.get_words(training_data))
    classified_texts = classify_texts(texts, classifier, dates)
    store_classified_text(classified_texts)


if __name__ == "__main__":
    main()
