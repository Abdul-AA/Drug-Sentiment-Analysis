# Birth Control Drug Reviews Analysis

Birth control drugs are among the most reviewed on Drugs.com, likely due to the high likelihood of uncomfortable side effects associated with them. My motivation for this project is to analyze reviews for popular birth control drugs on Drugs.com to provide insights into user experiences with these options.

## Project Overview

The goal is to explore the sentiments and topics discussed in birth control drug reviews. Initially, the plan was to scrape data directly from Drugs.com. However, a pre-scraped dataset from UCI ML ([Drug Review Dataset](https://archive.ics.uci.edu/dataset/462/drug+review+dataset+drugs+com)) spanning 2008-2017 was found, which was sufficient for exploratory analysis and proof of concept. The dataset also contains user ratings ranging from 1 to 10 and was collected between 2008 and 2017.

To achieve the overarching goal, several techniques were employed:

1. **Sentiment Analysis**: Analyzing the sentiment of reviews using a fine-tuned DistilBERT model. Reviews were grouped into positive and negative categories.
2. **Topic Modeling**: Identifying prevalent topics or themes in the reviews using Latent Dirichlet Allocations (LDA) topic modeling. This helps in understanding what users are actually discussing about the medication.
3. **Visualization**: Creating an interactive dashboard in Tableau to present insights from the analysis in a clear and accessible manner.

## The Resulting Dashboard

The dashboard consists of two main pages: an overview page and a detailed topic analysis page.

- **Overview Dashboard**: Summarizes key metrics and provides a broad view of the overall review data and discerned sentiments. It shows metrics such as the number of reviews, average ratings, number of drugs, and the distribution of positive and negative reviews. It also compares these metrics across different drugs and time periods, allowing for detailed comparisons. See the overview page below:

  ![Overview Dashboard](Images/db1.png)

- **Detailed Topic Analysis**: Offers an in-depth examination of the identified topics in the reviews. It features metrics such as the number of topics and the distribution of sentiments within each topic. This helps to determine whether users are discussing ongoing issues (negative sentiment) or resolved issues (positive sentiment). For instance, a review mentioning that bleeding and side effects have stopped after using the drug reflects a positive sentiment, even though the topic may appear problematic. The page also includes average ratings across topics and temporal analysis to show how sentiment distribution has evolved over time. See the topic analysis page below:

  ![Detailed Topic Analysis](Images/db2.png)

## Sentiment Analysis Technique

For sentiment analysis, the fine-tuned [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) model on Hugging Face was used, achieving state-of-the-art accuracy of 91.3% on the SST-2 dataset. This model was employed to predict the sentiment of each review, with confidence scores obtained to validate the predictions. The preprocessing steps were managed through the pipeline library available in the Transformers library, which handles essential preprocessing tasks. HTML tags were found and removed from the texts, but stop words were not removed as the transformer-based model handles them and requires them for contextual understanding.

## LDA Topic Modeling

Latent Dirichlet Allocation (LDA) was used for topic modeling due to its simplicity and effectiveness. The process involved robust preprocessing to achieve good coherence in the resulting topics. The following steps were taken:

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

  ![Coherence Score Plot](Images/Cs.png)

## Topics Inferred from the Reviews

- **Topic 1: "Weight Gain and Side Effects"** - Reviews often mentioned terms like weight and gain, focusing on the impact of the drug on weight and other side effects.
- **Topic 2: "Bleeding and Cycle Issues"** - Reviews discussed terms such as bleeding and cramps, relating to the drug's effect on bleeding and menstrual cycle issues.
- **Topic 3: "Pain and Insertion Issues"** - Reviews highlighted pain and discomfort, particularly related to drug ingestion or the insertion of devices.

## Threats to Validity and Next Steps

Currently, the insights might be biased as they are obtained from a single source. Acquiring data from multiple sources would provide a more representative sample and, in turn, more robust insights.

## Access the Dashboard
You can interact with the dashboard using the following link: [Which Issues and Sentiments Dominate Birth Control Drug Discussions](https://public.tableau.com/views/WhichIssuesandSentimentsDominateBirthControlDrugDiscussions/Overview?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link).

