# Homework 6 - Recommendation Systems 
 
## Assignment 

The goal of this assignment is to use the basic recommendation principles we have learned to recommend movies for yourself.

### Dataset
The MovieLens datasets were collected by the [GroupLens Research Project](https://grouplens.org/) at the University of Minnesota during the seven-month period from September 19, 1997 through April 22, 1998.  We are using the "100k dataset", available from [https://grouplens.org/datasets/movielens/100k/](https://grouplens.org/datasets/movielens/100k/)

## Questions

The questions below were answered using a [jupyter notebook](https://github.com/jgbotello/Web-Science/blob/main/HW6-Recommender%20Systems/Code/code.ipynb) that includes parts of the provided [example](https://github.com/odu-cs432-websci/public/blob/main/432_PCI_Ch02.ipynb) and some functions created from scratch.

### Q1: Find 3 users who are closest to you in terms of age, gender, and occupation.

**The 3 Users Closest to Me**

| **Index** | **user_id** | **age** | **gender** | **occupation** | **zip_code** |
|-----------|-------------|---------|------------|----------------|-------------|
| 152       | 153         | 25      | M          | student        | 60641       |
| 153       | 154         | 25      | M          | student        | 53703       |
| 247       | 248         | 25      | M          | student        | 37235       |


**For each of those 3 users:**

**Q: What are their top 3 (favorite) films?**

**User 153: Top and Bottom Movies**

*Top 3 Movies*

| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Shawshank Redemption, The (1994)         | 5          |
| 2        | Pulp Fiction (1994)                     | 5          |
| 3        | Contact (1997)                          | 5          |

*Bottom 3 Movies*
| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Raiders of the Lost Ark (1981)          | 1          |
| 2        | Star Wars (1977)                        | 1          |
| 3        | Return of the Jedi (1983)               | 1          |


**User 154: Top and Bottom Movies**

*Top 3 Movies*

| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Brazil (1985)                            | 5          |
| 2        | GoodFellas (1990)                        | 5          |
| 3        | Star Wars (1977)                         | 5          |

*Bottom 3 Movies*

| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Evita (1996)                             | 2          |
| 2        | Lost Highway (1997)                      | 2          |
| 3        | Star Trek: First Contact (1996)          | 2          |



**User 248: Top and Bottom Movies**

*Top 3 Movies*

| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Rock, The (1996)                         | 5          |
| 2        | Trainspotting (1996)                     | 5          |
| 3        | Godfather, The (1972)                    | 5          |

*Bottom 3 Movies*

| **Rank** | **Title**                                | **Rating** |
|----------|------------------------------------------|------------|
| 1        | Forrest Gump (1994)                      | 1          |
| 2        | Emma (1996)                              | 1          |
| 3        | Dante's Peak (1997)                      | 1          |



**Based on the movie values in those 6 tables (3 users X (favorite + least favorite)), choose a user that you feel is most like you.  Feel free to note any outliers (e.g., "I mostly identify with user 123, except I did not like "Ghost" at all").  You can investigate more than just the top 3 and bottom 3 movies to find your best match. This user is the *substitute you**.  

I will pick user 153 because the Shawshank Redemption movie is also my top favorite movie, and the genres of the other two movies are also of interest to me.

### Q2: Based on the ratings that users have given to the movies, answer the following questions:

**Q: Which 5 users are most correlated to the substitute you (i.e., which 5 users rate movies most similarly to the* substitute you?)**

*Top 5 Most Correlated Users*

| **User** | **Pearson Correlation** |
|----------|-------------------------|
| User 163 | 1.000                   |
| User 469 | 1.000                   |
| User 277 | 1.000                   |
| User 340 | 1.000                   |
| User 284 | 1.000                   |

**Q: Which 5 users are least correlated (i.e., negative correlation)?**

*Top 5 Least Correlated Users*

| **User** | **Pearson Correlation** |
|----------|-------------------------|
| User 939 | -1.000                  |
| User 257 | -1.000                  |
| User 258 | -1.000                  |
| User 32  | -1.000                  |
| User 231 | -1.000                  |


**Q: Explain the general operation of any functions you use from recommendations.py.**
To answer the question, I used the sim_pearson function from recommendations.py to calculate the Pearson correlation coefficient between two users. This function quantifies how similar two users are in terms of their movie ratings, specifically considering the movies they both rated. The function first identifies the list of movies that both users have rated. This is done by iterating through the movie ratings of two users and storing the overlapping item_id values in a dictionary.

Results regarding the top 5 Most Correlated Users indicate that these users share a perfect linear relationship with my "substitute jhon" in terms of ratings for the movies we both rated. In other words, our preferences are identical or proportional. It suggest similar tastes in movies. On the other hand, A correlation of -1.000 indicates a perfect negative linear relationship, meaning that the Top 5 least Correlated Users rated movies in an opposite manner to my "substitute jhon.

### Q3
Compute ratings for all the films that the *substitute you* has not seen and answer the following questions:

**Q: What are the top 5 recommendations for films that the *substitute you* should see.?**

| **Movie Title**                                           | **Predicted Rating** |
|-----------------------------------------------------------|----------------------|
| Little City (1998)                                       | 5.00                 |
| Entertaining Angels: The Dorothy Day Story (1996)        | 5.00                 |
| Aparajito (1956)                                         | 5.00                 |
| Aiqing wansui (1994)                                     | 5.00                 |
| World of Apu, The (Apur Sansar) (1959)                   | 5.00                 |

**Q: What are the bottom 5 recommendations (i.e., films the *substitute you* is almost certain to hate)?**

| **Movie Title**                                            | **Predicted Rating** |
|------------------------------------------------------------|----------------------|
| Amityville 3-D (1983)                                     | 1.00                 |
| Amityville 1992: It's About Time (1992)                   | 1.00                 |
| 3 Ninjas: High Noon At Mega Mountain (1998)               | 1.00                 |
| Turbo: A Power Rangers Movie (1997)                       | 1.00                 |
| Theodore Rex (1995)                                       | 1.00                 |

* *Q: Explain the general operation of any functions you use from recommendations.py.*
To answer this question, I used the getRecommendations function from recommendations.py. This function generates recommendations for a user based on collaborative filtering. It analyzes other users' preferences, using a similarity metric (I used pearson correlation) to identify relevant items that the target user hasn't rated yet. It receives three parameter as input: 1) a dictionary of preferences where the keys are user, and the values are dictionaries containing the movies ratings. 2) the target user for whom recommendations will be generated, and 3) the way similarity will be calculated (In this case pearson correlation).

### Q4: Choose your (the real you, not the *substitute you*) favorite and least favorite film from the data. 

I will pick Jurassic Park (1993) as my favorite movie because I used to watch it with my family when I was growing up. On the other hand, I will choose The Fugitive as my least favorite movie because I remember my grandpa saying that it was really bad when we watched it.

* *Q: What are the top 5 most correlated films to your favorite film?  Bottom 5 least correlated?*

*top 5 most correlated films*

| **Movie Title**            | **Similarity Score** |
|----------------------------|----------------------|
| Loch Ness (1995)           | 1.00                 |
| Nico Icon (1995)           | 1.00                 |
| Hurricane Streets (1998)   | 1.00                 |
| Love Serenade (1996)       | 1.00                 |
| Safe Passage (1994)        | 1.00                 |

*Bottom 5 least correlated?*

| **Movie Title**                         | **Similarity Score** |
|----------------------------------------|----------------------|
| Kaspar Hauser (1993)                   | -1.00               |
| Wonderland (1997)                      | -1.00               |
| The Innocent (1994)                    | -1.00               |
| Blood for Dracula (Andy Warhol's Dracula) (1974) | -1.00               |
| Perfect Candidate (1996)               | -1.00               |


* *Q: Based on your knowledge of the resulting films, do you agree with the results?*  In other words, do you personally like/dislike the resulting films? 
After watching the trailers of the recommended movies, I believe I would enjoy the top 3 most correlated films, but not the other two. On the other hand, for the bottom 5 least correlated films, I agree with the results—I don’t think I would like them.

I consider this is part of a recommendation system, which will not be 100% accurate as it depends on user preferences. Additionally, most of the movies are old and do not match exactly with my preferences.

* *Q: Explain the general operation of any functions you use from recommendations.py.*
To answer the above questions I used the topMatches and transformPrefs funtions from recomendations.py. The topMatches function works by iterating through all other users in the preferences dictionary, calculating the similarity score between the target user and each other one. The transformPrefs function restructures the input preferences dictionary into a reversed form. It transform the recommendations into a mapping where persons are described with interest scores for a given title e.g. {title: person} instead of {person: title}. Based on the above, when passing as input the id of my favorite movie, the system extract similar movies based on pearson correlation.

the [trailer for "Loch Ness (1995)"](https://www.youtube.com/watch?v=kMb5nrFsN2Q) was found by searching for "Loch Ness (1995)" on Google.

the [trailer for "Nico Icon (1995)"](https://mubi.com/en/films/nico-icon/trailer) was found by searching for "Nico Icon (1995)" on Google.

the [trailer for "Hurricane Streets (1998)"](https://www.youtube.com/watch?v=PZibLqWZ7cM) was found by searching for "Hurricane Streets (1998)" on Google.

the [trailer for "Love Serenade (1996)"](https://www.youtube.com/watch?v=Rk92ymOMlyc) was found by searching for "Love Serenade (1996) " on Google.

the [trailer for "Safe Passage (1994)"](https://www.youtube.com/watch?v=X2vyr662x4Q) was found by searching for "Safe Passage (1994)" on Google.

the [trailer for "Kaspar Hauser (1993)"](https://www.youtube.com/watch?v=6yuOZWBAhO8) was found by searching for "Kaspar Hauser (1993)" on Google.

the [trailer for "Wonderland (1997)"](https://www.youtube.com/watch?v=tIWMOSKKlgs) was found by searching for "Kaspar Hauser (1993)" on Google.

the [trailer for "The Innocent (1994)"](https://www.dailymotion.com/video/x8i23dv) was found by searching for "The Innocent (1994)" on Google.

the [trailer for "Blood for Dracula (Andy Warhol's Dracula)"](https://www.youtube.com/watch?v=-mxhJzSKV08) was found by searching for "Blood for Dracula (Andy Warhol's Dracula)" on Google.

the [trailer for "Perfect Candidate (1996)"](https://www.youtube.com/watch?v=-mxhJzSKV08) was found by searching for "Perfect Candidate (1996)" on Google.