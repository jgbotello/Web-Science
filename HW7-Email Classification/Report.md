# Homework 7 - Email Classification

## Assignment

The goal of this assignment is to classify email into two groups based on topic -- either "on topic" or "not on topic".  You can choose the topic based on what types of emails you typically receive (or what you have access to).

**Tips for Completing this Assignment:**
* First, read the entire assignment before starting.
* Make sure you've watched the 	Document Filtering lecture videos.
* Watch the HW7 intro video.
* *Don't start with a Google search.*  Your first references should be
    * [Document Filtering lecture slides](https://docs.google.com/presentation/d/1OpfBDl2YEE7AONVeKUyHA-J7a1mRjncD7cen8F6BG1A/edit?usp=sharing) and videos
    * [class Colab notebook](https://github.com/odu-cs432-websci/public/blob/main/432_PCI_Ch06.ipynb)
    * [*Programming Collective Intelligence* book](https://go.oreilly.com/old-dominion-university/library/view/programming-collective-intelligence/9780596529321/) and [Chapter 6 code](https://github.com/arthur-e/Programming-Collective-Intelligence/tree/master/chapter6)  


***NOTES:***
* You don't have to use the SQL classifier.  You can replace `classifier` with `basic_classifer` in `naivebayes()` to use the simple text-based classifier.
* The naivebayes classifier handles calculating probabilities on individual words.  Once you've initialized that, you just need to train on one email at a time and then test the classifier.
* For training, you want to read in each email separately as a string and then pass that string to `train()`. For example, to train on 5 emails, you would need to call `train()` 5 times.
* Your emails should be formatted as one per file.  They should also be plain text only.  The easiest way to do this is open the email normally in your email reader, select and copy all of the text, and paste into a plain text document.  This copy/paste process shouldn't include any of the underlying HTML.
* You can set up whatever classification labels you want, you don't have to use 'bad' and 'good'.  Just make sure that you only use 2 different labels.
* To test (classify), you want to read in each email to test separately and pass that to `classify()`.  The return value from `classify()` is the result of the classification for that email.
* See the first cell under "Example 2 (pg. 127) - using thresholds" (in the Colab notebook) as an example of the process.  The `sampletrain()` function just calls `train()` multiple times on different documents.  In these examples, a single sentence is considered to be the entire document.


### Q1. Create two datasets, Testing and Training.
For this assignment, I have chosen to classify emails into two categories: Work-related and Non-work-related. The "Work-related" category includes emails from ODU and VMASC such as meeting invitations, project updates, task assignments, and collaboration with colleagues. The "Non-work-related" category include personal email, promotional content, newsletters, and other non-professional communications.

The training and testing dataset can be found in the Data folder.

The **Training** dataset consist of
* 20 text documents for email messages I considered on my chosen topic
* 20 text documents for email messages I considered *not* on my chosen topic

The **Testing** dataset consist of:
* 5 text documents for email messages I considered on my chosen topic
* 5 text documents for email messages I considered *not* on my chosen topic

### Q2. Naive Bayes classifier
I used the example code in the class Colab notebook to train and test the Naive Bayes classifier with my data. The table below shows the classification results for each email message 

| Actual   | Predicted  |
|----------|------------|
| work     | nonwork    |
| work     | nonwork    |
| work     | work       |
| work     | work       |
| work     | work       |
| nonwork  | nonwork    |
| nonwork  | nonwork    |
| nonwork  | nonwork    |
| nonwork  | nonwork    |
| nonwork  | nonwork    |

**Q: For those emails that the classifier got wrong, what factors might have caused the classifier to be incorrect?  You will need to look at the text of the email to determine this.**

The email body for the misclassified email included elements like Google Scholar and citation, among others. These words likely contributed to categorizing the email in the nonwork category during the training of the Naive Bayes classifier, which resulted in a misclassification during testing. We have to remember that Naive Bayes relies on the conditional independence assumption. The algorithm assumes that all words in a document are independent of one another, which is rarely true for natural language. In this case, specific combinations of words or phrases (e.g., "Google Scholar Alerts" combined with "citations") might provide a strong work-related signal. However, since the classifier evaluates each word in isolation, it can lead to misclassification. Additionally, some words may appear in both work and nonwork emails. This overlap can confuse the algorithm due to how probabilities are calculated, further contributing to the incorrect classification.



### Q3. Confusion Matrix

**Draw a confusion matrix for your classification results**

|                | Predicted: Work | Predicted: Nonwork |
|----------------|-----------------|--------------------|
| **Actual: Work** | 3               | 2                  |
| **Actual: Nonwork** | 0               | 5                  |


**Q: Based on the results in the confusion matrix, how well did the classifier perform?**  

I consider the classifier performed reasonably well, as it correctly classified 8 out of 10 emails, resulting in an accuracy of 80%. The classifier had 2 false negatives, meaning it incorrectly classified work emails as nonwork. There were no false positives, which means it did not misclassify any nonwork emails as work.

**Q: Would you prefer an email classifier to have more false positives or more false negatives?  Why?**

It depends on the purpose of the email classifier. However, in this specific cases, i would say it is preferable to have more false positives (classifying nonwork emails as work) rather than false negatives (classifying work emails as nonwork).It is because false negatives can cause work emails to be missed. It could lead to miss any deadline. False positives are less risky because a user can manually filter through a few incorrectly classified emails to find relevant ones.

## Extra Credit

### Q4 *(1 point)* 

Report the precision and accuracy scores of your classification results.

### **Q4: Precision and Accuracy Scores**

#### **Confusion Matrix Recap**
|                | Predicted: Work | Predicted: Nonwork |
|----------------|-----------------|--------------------|
| **Actual: Work** | 3               | 2                  |
| **Actual: Nonwork** | 0               | 5                  |

- **True Positives (TP):** 3 (work emails correctly classified as *work*)  
- **False Negatives (FN):** 2 (work emails incorrectly classified as *nonwork*)  
- **True Negatives (TN):** 5 (nonwork emails correctly classified as *nonwork*)  
- **False Positives (FP):** 0 (nonwork emails incorrectly classified as *work*)  

---

#### **Formulas**
- **Precision** (for *work* category):
Precision = TP / (TP + FP)

**Accuracy**:
Accuracy = (TP + TN) / (TP + TN + FP + FN)

---

The precision and accuracy scores for the classifier are:

- **Precision:** \( 1.0 \) (or 100%)  
- **Accuracy:** \( 0.8 \) (or 80%)  

The precision is **1.0** because there were no false positives, meaning the classifier never incorrectly classified a nonwork email as work. The accuracy is **80%**, as 8 out of 10 emails were correctly classified.


### Q5 *(2 points)* 

Tune your classifier by updating weights to obtain better classification results. You may want to change the default weights (`weight`, `ap`) given to `weightedprob()` or the threshold used for the Bayesian classifier or change how the words are extracted from the document (for this you will need to re-train the model).  Report the changes you made, re-run your Testing dataset, and show that the performance improved (either by using the confusion matrix or by computing precision and accuracy).

If your classifier got all of the items correct in Q2, change the weights to make the classifier perform worse and discuss the results.

### Q6 *(4 points)* 

Implement the classifier with the Multinomial model instead of the multiple Bernoulli model and re-run Q2 and Q3.  Did the classification improve?  *Make sure to remove the unique word filter from the extractor.*

*For credit on this part, you must describe what you have done and discuss the differences between the Multinomial model and the multiple Bernoulli model.*

