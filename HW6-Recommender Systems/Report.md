# Homework 6 - Recommendation Systems 
 
## Assignment 

The goal of this assignment is to use the basic recommendation principles we have learned to recommend movies for yourself.

### Dataset
The MovieLens datasets were collected by the [GroupLens Research Project](https://grouplens.org/) at the University of Minnesota during the seven-month period from September 19, 1997 through April 22, 1998.  We are using the "100k dataset", available from [https://grouplens.org/datasets/movielens/100k/](https://grouplens.org/datasets/movielens/100k/)

## Questions

The questions below were answered using a [jupyter notebook](https://github.com/jgbotello/Web-Science/blob/main/HW6-Recommender%20Systems/Code/code.ipynb) that includes parts of the provided [example](https://github.com/odu-cs432-websci/public/blob/main/432_PCI_Ch02.ipynb) and some functions created from scratch.

### Q1: Find 3 users who are closest to you in terms of age, gender, and occupation. For each of those 3 users:

**Q: What are their top 3 (favorite) films?**
**Q: What are their bottom 3 (least favorite) films?**

| **User ID** | **Age** | **Gender** | **Occupation** | **Top 3 Movies**                                                                 | **Bottom 3 Movies**                                                                 |
|-------------|---------|------------|----------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **153**     | 25      | M          | Student        | 1. *The Shawshank Redemption* (1994) - 5 <br> 2. *Pulp Fiction* (1994) - 5 <br> 3. *Contact* (1997) - 5 | 1. *Raiders of the Lost Ark* (1981) - 1 <br> 2. *Star Wars* (1977) - 1 <br> 3. *Return of the Jedi* (1983) - 1 |
| **154**     | 25      | M          | Student        | 1. *Brazil* (1985) - 5 <br> 2. *GoodFellas* (1990) - 5 <br> 3. *Star Wars* (1977) - 5     | 1. *Evita* (1996) - 2 <br> 2. *Lost Highway* (1997) - 2 <br> 3. *Star Trek: First Contact* (1996) - 2 |
| **248**     | 25      | M          | Student        | 1. *The Rock* (1996) - 5 <br> 2. *Trainspotting* (1996) - 5 <br> 3. *The Godfather* (1972) - 5 | 1. *Forrest Gump* (1994) - 1 <br> 2. *Emma* (1996) - 1 <br> 3. *Dante's Peak* (1997) - 1 |




Based on the movie values in those 6 tables (3 users X (favorite + least favorite)), choose a user that you feel is most like you.  Feel free to note any outliers (e.g., "I mostly identify with user 123, except I did not like "Ghost" at all").  You can investigate more than just the top 3 and bottom 3 movies to find your best match.

This user is the *substitute you*.  

### Q2

Based on the ratings that users have given to the movies, answer the following questions:

* *Q: Which 5 users are most correlated to the* substitute you *(i.e., which 5 users rate movies most similarly to the* substitute you?)
* *Q: Which 5 users are least correlated (i.e., negative correlation)?*
* *Q: Explain the general operation of any functions you use from recommendations.py.*

### Q3
Compute ratings for all the films that the *substitute you* has not seen and answer the following questions:

* *Q: What are the top 5 recommendations for films that the *substitute you* should see.?*
* *Q: What are the bottom 5 recommendations (i.e., films the *substitute you* is almost certain to hate)?*
* *Q: Explain the general operation of any functions you use from recommendations.py.*

### Q4
Choose your (the real you, not the *substitute you*) favorite and least favorite film from the data. 

* *Q: What are the top 5 most correlated films to your favorite film?  Bottom 5 least correlated?*
* *Q: What are the top 5 most correlated films to your least favorite film?  Bottom 5 least correlated?*
* *Q: Based on your knowledge of the resulting films, do you agree with the results?*  In other words, do you personally like/dislike the resulting films? 
* *Q: Explain the general operation of any functions you use from recommendations.py.*

If you have not heard of the recommended movies, search for the movie's trailer on YouTube and watch it before you answer.  If you do this, include the link to the trailer in your report.  For example, the [trailer for "Top Gun (1986)"](https://www.youtube.com/watch?v=xa_z57UatDY) was found by searching for "top gun 1986 trailer" on Google.   

## Extra Credit

### Q5 *(2 points)*

Filter the MovieLens dataset so that it only contains movies with at least 10 ratings.  

*Q: How many movies are in the filtered dataset?*

Re-do Q3 and Q4 using this dataset.  

*Q: Do you think the recommendations have improved?*

### Q6 *(2 points)*  

Rank all 1682 movies in the 1997/1998 MovieLens dataset.  (*Rank*, not rate. These should be 1-1682.) Break any ties based on number of raters (for example, a movie with an average rating of 4 with 100 raters should be ranked higher than a movie with an average rating of 4 with only 50 raters).

Put a file with the full list in your repo.  List the top 10 and bottom 10 movies in your report.

### Q7 *(3 points)*  

Rank the 1682 movies in the 1997/1998 MovieLens dataset according to [today's IMDB data](https://www.imdb.com/interfaces/).  Note that the IMDB data includes TV shows and other items that aren't movies. Break any ties based on number of raters (for example, a movie with an average rating of 7.2 with 10,000 raters should be ranked higher than a movie with a rating of 7.2 with only 9,000 raters).

Put a file with the full list in your repo.  List the top 10 and bottom 10 movies in your report.

### Q8 *(1 point)*

*You must have done both Q6 and Q7 to complete this question.*

Draw a scatterplot where each dot is a film (i.e., 1682 dots).  The x-axis is the MovieLens ranking (Q6) and the y-axis is today's IMDB ranking (Q7).  Note that the MovieLens ratings are 1-5 and the IMDB ratings are 1-10, so you may want to normalize the data before plotting.  *The scatterplot must be created in R or Python, no Excel.*

*Q: Describe any interesting outliers.*
