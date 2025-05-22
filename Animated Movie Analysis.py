# -*- coding: utf-8 -*-
"""
Created on Wed May 21 20:12:12 2025

@author: Josh Garzaniti
"""
import pandas as pd
import numpy as np

movies = pd.read_csv("G:\My Drive\Personal Projects\movies.csv")

movies.head(5)

reviews = pd.read_csv("G:\My Drive\Personal Projects\critic_reviews.csv")

reviews.head(5)

movies_with_reviews = pd.merge(movies, reviews, on = "movieId", how = "outer")

movies_with_reviews.head(5)

movies_with_reviews.columns

movies_with_reviews = movies_with_reviews.drop(columns=["movieId", 
                                                        "movieURL",
                                                        "reviewId",
                                                        "criticPageUrl",
                                                        "isRtUrl",
                                                        "publicationUrl",
                                                        "reviewUrl"])

movies_with_reviews.head(5)