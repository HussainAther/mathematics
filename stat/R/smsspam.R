"Filtering mobile phone spam with naive Bayes algorithm."
sms_raw <- read.csv("spam.csv", stringsAsFactors = FALSE)
sms_raw$type <- factor(sms_raw$type) # Convert to factor
sms_corpus <- Corpus(VectorSource(sms_raw$text)) 
corpus_clean <- tm_map(sms_corpus, tolower) # Convert to lowercase
corpus_clean <- tm_map(corpus_clean, removeNumbers) # Remove numbers

