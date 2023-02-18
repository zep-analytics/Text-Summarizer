# Text-Summarizer

Summarization can be defined as a task of producing a concise and fluent summary while preserving key information and overall meaning.

Summarization systems often have additional evidence they can utilize in order to specify the most important topics of document(s). For example, when summarizing blogs, there are discussions or comments coming after the blog post that are good sources of information to determine which parts of the blog are critical and interesting.


#### Text Summarizer app will summarize the input text and play the summarized text as audio.

This Text Summarizer app is the type of Extractive Summarization. This approach weights the important part of sentences and uses the same to form the summary. 

Different algorithm and techniques are used to define weights for the sentences and further rank them based on importance and similarity among each other.

Input document → sentences similarity → weight sentences → select sentences with higher rank.

Text Summarizer app used an unsupervised learning approach to find the sentences similarity and rank them. One benefit of this will be, you don’t need to train and build a model prior start using it for your project.

Text Summarizer app used cosine similarity to find similarity between sentences.

### Code flow to generate summarize text:-
Input article → split into sentences → remove stop words → build a similarity matrix → generate rank based on matrix → pick top N sentences for summary.

#### Input Screen
![image](https://github.com/zep-analytics/Text-Summarizer/blob/main/Input%20Screen.png)

#### Output Screen
![image](https://github.com/zep-analytics/Text-Summarizer/blob/main/Output%20Screen.png)

