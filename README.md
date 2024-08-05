# Birth Control Drug Reviews Analysis

Birth control drugs are among the most reviewed on drugs.com, partly due to the likelihood of uncomfortable side effects associated with them. This project analyzes reviews for the top five most reviewed birth control drugs on drugs.com to provide insights into user experiences with these options. The data contains user ratings ranging from 1 to 10 and was collected between 2008 and 2017.

## Project Overview

The goal of this project was to explore the sentiments and topics discussed in birth control drug reviews. Initially, the plan was to scrape data directly from drugs.com. However, a pre-scraped dataset from UCI ML ([Drug Review Dataset](https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com)) was found, which was sufficient for exploratory analysis and proof of concept. The project methodology includes:

1. **Data Acquisition**: Utilizing the existing dataset.
2. **Sentiment Analysis**: Analyzing the sentiment of reviews using a fine-tuned DistilBERT model.
3. **Topic Modeling**: Identifying prevalent topics in the reviews using LDA.
4. **Visualization**: Creating an interactive dashboard in Tableau to present insights from the analysis.

## Insights from the Dashboard

The dashboard offers detailed insights through two pages:

- **Overview Dashboard**: Summarizes key metrics and provides a broad view of the overall review data and discerned themes and sentiments2.
### ![Overview Dashboard](/Users/Abdul/Desktop/Drug-Sentiment-Analysis/Images/db1.png)
- **Detailed Topic Analysis**: Presents an in-depth examination of the identified topics in the reviews.
### ![Detailed Topic Analysis](/Users/Abdul/Desktop/Drug-Sentiment-Analysis/Images/db2.png)

## Sentiment Analysis

For sentiment analysis, the [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) pipeline was used, which has achieved state-of-the-art accuracy of 91.3% on the SST-2 dataset. This model was employed to predict the sentiment of each review, and confidence scores were obtained to validate the predictions.



## LDA Topic Modeling

For topic modeling, Latent Dirichlet Allocation (LDA) was used due to its simplicity and effectiveness. The process involved:

1. **Text Preprocessing**:
   - Converted text to lowercase.
   - Removed multiple white spaces and line breaks.
   - Tokenized the text into individual words using NLTK’s `word_tokenize`.
   - Removed non-alphabetic tokens.
   - Used NLTK's stopword list and added custom stopwords.
   - Removed stopwords from the tokenized text.
   - Created bigrams and trigrams using Gensim's `Phrases` and `Phraser`.
   - Lemmatized the text using SpaCy, retaining only nouns, adjectives, verbs, and adverbs.
   - Applied the preprocessing pipeline to the DataFrame's `review` column.
   - Created a dictionary (`id2word`) and filtered extremes to remove words appearing in fewer than 50 documents or more than 50% of the documents.
   - Created a corpus representing each document as a list of tuples with word IDs and their frequencies.

2. **Topic Selection**:
   - Selected the number of topics based on coherence and perplexity scores.
   - Chose three topics due to their high coherence score of 0.46, despite high perplexity, based on manual review of representative documents.

### ![Coherence Score Plot](/Users/Abdul/Desktop/Drug-Sentiment-Analysis/Images/Cs.png)

## Insights

- **Topic 1: "Weight Gain and Side Effects"** - Reviews often mentioned words like weight and gain, focusing on the impact of the drug on weight and other side effects.
- **Topic 2: "Bleeding and Cycle Issues"** - Reviews discussed terms such as bleeding and cramps, relating to the impact of the drug on bleeding and menstrual cycle issues.
- **Topic 3: "Pain and Insertion Issues"** - Reviews highlighted pain and discomfort, particularly related to drug ingestion or the insertion of devices.

### [Placeholder for Insights Description]
