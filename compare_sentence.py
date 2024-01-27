from sentence_transformers import SentenceTransformer, util
import torch
import csv

csvfile = "C:\\Ming\\GPT\\myNote\\mynote1.csv"

questions = []
answers = []


with open(csvfile) as f:
    for row in csv.reader(f):
        questions.append(row[0])
        answers.append(row[1])

print(f"The size of questions is {len(questions)}")

# https://huggingface.co/sentence-transformers/distilbert-base-nli-stsb-mean-tokens
# This model is deprecated
# model = SentenceTransformer('distilbert-base-nli-mean-tokens')
model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
# sentence_embeddings = model.encode(questions)

questions = [s for s in questions if s.strip() != ""]
length1 = len(questions)
print(f"The length of the Q&A is {length1}.")
sentence_embeddings = model.encode(questions, convert_to_tensor=True)

length = len([s for s in questions if s.strip() != ""])

print(f"The length of the Q&A is {length}.")

# list top
top_k = min(3, length)
 
# For small corpora (up to about 1 million entries) we can compute the cosine-similarity between the query and all entries in the corpus. 
# https://www.sbert.net/examples/applications/semantic-search/README.html
def getSimilarity(sentence):
    query_embedding = model.encode(sentence, convert_to_tensor=True)
    
    cos_scores = util.cos_sim(query_embedding, sentence_embeddings)
    # cos_scores = result[0]
    best_score_index = cos_scores.argmax()
    
    # leave the best score for later
    best_score = cos_scores[0][best_score_index]
    print(f"The best_score is {best_score:.2f}")
    if(best_score<0.8):
        best_score_index = -1
    return best_score_index    

def getAnswer(indx):
    if( indx >0 and indx <length):
        return answers[indx]
    else:
        return 'I do not know'

def add_Entry(question, answer):
    result = 'Success'
    indx = getSimilarity(question)
    if( indx >0 and indx <length):
        result = 'Question exists already: ' + str(indx)
    else:
        # Open the CSV file in append mode
        with open(csvfile, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the new question-answer pair to the CSV file
            writer.writerow([question, answer])
        
        questions = []
        answers = []    
        with open(csvfile) as f:
            for row in csv.reader(f):
                questions.append(row[0])
                answers.append(row[1])
        questions = [s for s in questions if s.strip() != ""]
        sentence_embeddings = model.encode(questions, convert_to_tensor=True)    
        result = 'new entry has beeen added'  
    return  result

if __name__ == "__main__":
    add_Entry('You are not allowed to push code to this project.', 'this is a permission issue, talk with source branch owner')
    
    ret = add_Entry("中文问题", "答案")

    sentence = input("Enter a sentence: ").lower()
    query_embedding = model.encode(sentence)
    
    indx = getSimilarity(sentence)
    if( indx >0 and indx <length):
        ans = getAnswer(indx)
    else:
        ans = 'I do not know'
    # Print the result
    print("The answer is {ans}")