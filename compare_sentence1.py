from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from scipy.spatial.distance import cosine

import csv

questions = []
answers = []

with open("D:\\ming\\projects\\mynote1.csv") as f:
    for row in csv.reader(f):
        questions.append(row[0])
        answers.append(row[1])

print(f"The size of questions is {len(questions)}")

    
stopwords = stopwords.words('english')

def compare2(sentence1, sentence2):
    # Tokenize and remove stopwords
    tokens1 = [w for w in word_tokenize(sentence1) if w not in stopwords]
    tokens2 = [w for w in word_tokenize(sentence2) if w not in stopwords]

    # Create a set of unique words from both sentences
    words = set(tokens1 + tokens2)

    # Create vectors of word counts for each sentence
    vector1 = [tokens1.count(w) for w in words]
    vector2 = [tokens2.count(w) for w in words]

    # Calculate the cosine similarity
    similarity = 1 - cosine(vector1, vector2)

    return similarity

def getSimilarity(sentence):
    distance2 = 0.0
    index1 = len(questions)
    
    for i, element in enumerate(questions):
        curdistance = compare2(sentence,element)
        if(distance2 < curdistance):
            distance2 = curdistance
            index1 = i
        print(f"Element {i}: {element} with distance {curdistance}\n")
    return index1    

def getAnswer(index1):
    return answers[index1]

if __name__ == "__main__":
    sentence = input("Enter a sentence: ").lower()
    indx = getSimilarity(sentence)
    ans = getAnswer(indx)
    # Print the result
    print("The answer is {ans}}")