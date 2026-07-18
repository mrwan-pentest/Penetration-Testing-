# What is Artificial Intelligence (AI)?

The simplest definition is:

> Artificial Intelligence (AI) refers to computer systems capable of performing tasks that normally require human intelligence.

Examples include:

- Understanding language
- Making decisions
- Recognizing images
- Solving problems

---

# A More Accurate Definition

AI does **not** think like humans.

Instead, it learns **statistical patterns** from massive amounts of data and uses those patterns to predict the most likely answer.

For example, if you ask:

```
What is the capital of France?
```

AI does not search through a book.

Instead, during training it has seen millions of examples like:

```
France → Paris
```

Therefore, it predicts that the correct answer is:

```
Paris
```

---

# Traditional Programming vs Artificial Intelligence

## Traditional Programming

Traditional programs follow fixed rules written by the programmer.

Example:

```python
if age >= 18:
    print("Adult")
else:
    print("Child")
```

The logic is straightforward:

```
If X happens → Perform Y
```

The result is deterministic.

---

## Artificial Intelligence

AI does not rely on fixed rules.

Instead, it makes predictions based on probabilities.

For example, when AI analyzes an image, it does not say:

```
This is definitely a cat.
```

Instead, it may produce:

```
Cat = 95%
Dog = 3%
Rabbit = 2%
```

Then it chooses the class with the highest probability.

---

# Learning from Data

This is one of the most important concepts in AI.

In traditional programming:

The programmer writes all the rules.

In AI:

The system learns the rules automatically from large datasets.

For example, we provide:

- One million images of cats.
- One million images of dogs.

Instead of explicitly telling the computer:

```
Cats have these features.
```

The AI discovers the patterns by itself.

---

# Pattern Recognition

Pattern recognition is the ability to identify recurring structures within data.

This is one of AI's greatest strengths.

For example:

When humans see:

```
🙂
```

They immediately recognize it as a smiling face.

AI performs a similar process.

It learns that certain visual patterns correspond to:

- Face
- Eyes
- Smile

---

# Why Is AI Good at Language?

Suppose you read the sentence:

```
I am hungry and I want...
```

The most likely next words are:

- Food
- Something to eat
- A meal

AI has learned these language patterns from billions of sentences during training.

Rather than understanding language exactly like humans, it predicts the most probable continuation.

---

# AI vs Machine Learning vs Deep Learning

These three terms are often confused.

---

## Artificial Intelligence (AI)

AI is the broad field.

It includes every technique designed to make machines perform intelligent tasks.

---

## Machine Learning (ML)

Machine Learning is a subset of AI.

Its main idea is:

> Enable computers to learn from data instead of relying only on manually written rules.

Common applications include:

- Spam Detection
- Fraud Detection
- Recommendation Systems

---

## Deep Learning (DL)

Deep Learning is a subset of Machine Learning.

It relies on:

```
Neural Networks
```

Deep Learning is widely used for:

- Computer Vision
- Speech Recognition
- Natural Language Processing (NLP)

Examples include:

- ChatGPT
- Claude
- Gemini

---

# Relationship Between AI, ML, and DL

They can be visualized as:

```text
Artificial Intelligence
│
├── Machine Learning
│       │
│       └── Deep Learning
```

Or more simply:

```
AI = The entire field

ML = A method that enables computers to learn from data

DL = An advanced type of Machine Learning based on neural networks
```