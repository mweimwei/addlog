from lmqg import LMQG

# Initialize the model
lmqg = LMQG()

# Your text goes here
text = "Your text goes here."

# Generate questions and answers
qa_pairs = lmqg.generate(text)

# Print the questions and answers
for pair in qa_pairs:
    print(f"Question: {pair['question']}")
    print(f"Answer: {pair['answer']}")
