# Movie-Recommendation-System

A simple movie recommendation engine which uses the concept of Content based filtering and cosine similarity to find the similarity between movies

Two options are provided for this recommendation engine...
First is searching for the list of movies of a director and each movie's details viz. director, top 3 cast and genres. 
Second is searching for a list of recommended movies for a given movie. In this option, we can also get the details of each movie viz. director, top 3 cast and genres



**URL of data sets:**

Movies -> [Movies](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

Credits (cast and crew) -> [Credits](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_credits.csv)


**Screenshots:**

**1) Welcome Page**

![image](https://user-images.githubusercontent.com/105063050/170866401-e17f3ea4-e365-4424-8451-4bd9d0666264.png)



**2) Different Options**

![image](https://user-images.githubusercontent.com/105063050/170869564-cd5dcc0c-bcde-42eb-be42-148f33de974f.png)
 
 
 **3) Searching the movies of a Director**
 
 **i)**
 ![image](https://user-images.githubusercontent.com/105063050/170869721-faedc284-aa79-4a2e-830f-d6d9f97983a0.png)
 
 
 **ii)**
 ![image](https://user-images.githubusercontent.com/105063050/170869994-edd85743-7f4e-4d86-a659-bba1eb7df05b.png)
 
 
 **4) Recommended movies of a selected movie**
 
 **i)**
 ![image](https://user-images.githubusercontent.com/105063050/170870208-ca5b06dc-d8bd-432c-be11-1a95d6f2d0a1.png)




**ii) We can also compare the details of each movie by clicking on the exapander**  ***"See Details"*** 
![image](https://user-images.githubusercontent.com/105063050/170870738-7f37234f-41ad-4c73-88c5-6e79f584fb0c.png)


**For calculating the similarity between movies, I have considered the cosine similarity instead of Eucledian distance 
because the latter gives the in-accurate results for larger data sets**


**Also, the similarity is not solely based (only on genre or cast or overview) on a single detail. I have combined 
all the details viz. overview, keywords, genres, cast, crew and calculated the similarity values**
