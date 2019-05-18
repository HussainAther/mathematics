"Filtering mobile phone spam with naive Bayes algorithm."
install.packages("e1071") # Install naive Bayes implementation package
library(e1071)  # load package
sms_raw <- read.csv("spam.csv", stringsAsFactors = FALSE)
sms_raw$type <- factor(sms_raw$type) # Convert to factor
sms_corpus <- Corpus(VectorSource(sms_raw$text)) 
corpus_clean <- tm_map(sms_corpus, tolower) # Convert to lowercase
corpus_clean <- tm_map(corpus_clean, removeNumbers) # Remove numbers
corpus_clean <- tm_map(corpus_clean, removeWords, stopwords()) # Remove stop words
corpus_clean <- tm_map(corpus_clean, removePunctuation) # Remove punctuation
corpus_clean <- tm_map(corpus_clean, stripWhitespace) # Remove whitespace
sms_dtm <- DocumentTermMatrix(corpus_clean) # Create spares matrix
sms_raw_train <- sms_raw[1:4169, ] # Split to training and test
sms_raw_test  <- sms_raw[4170:5559, ] 
sms_dtm_train <- sms_dtm[1:4169, ] # Document term
sms_dtm_test  <- sms_dtm[4170:5559, ]
sms_corpus_train <- corpus_clean[1:4169] # Corpus
sms_corpus_test  <- corpus_clean[4170:5559]
wordcloud(sms_corpus_train, min.freq = 40, random.order = FALSE) # Word cloud
spam <- subset(sms_raw_train, type == "spam") # Subset of spam type
ham <- subset(sms_raw_train, type == "ham") # ham type
sindFreqTerms(sms_dtm_train, 5) # Create indicator features
sms_dict <- Dictionary(findFreqTerms(sms_dtm_train, 5)) # Save as dictionary 
sms_train <- DocumentTermMatrix(sms_corpus_train, list(dictionary = sms_dict))
sms_test  <- DocumentTermMatrix(sms_corpus_test, list(dictionary = sms_dict))
convert_counts <- function(x) { # function to convert counts to factors 
    x <- ifelse(x > 0, 1, 0)
    x <- factor(x, levels = c(0, 1), labels = c(""No"", ""Yes""))
    return(x)
 }
sms_train <- apply(sms_train, MARGIN = 2, convert_counts)
sms_test  <- apply(sms_test, MARGIN = 2, convert_counts)
sms_classifier <- naiveBayes(sms_train, sms_raw_train$type) # Model
sms_test_pred <- predict(sms_classifier, sms_test) # Evaluate
library(gmodels) # Compare predictions to actual values
CrossTable(sms_test_pred, sms_raw_test$type, prop.chisq = FALSE, prop.t = FALSE, dnn = c("predicted", "actual"))
