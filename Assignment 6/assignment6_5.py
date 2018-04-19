#http://www.gregreda.com/2013/10/26/using-pandas-on-the-movielens-dataset/

import pandas as pd
import numpy as np

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('data/u.user', sep='|', names=u_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('data/u.data', sep='\t', names=r_cols, encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('data/u.item', sep='|', names=m_cols, usecols=range(5), encoding='latin-1')

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)

movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()

# sort by rating average
print(movie_stats.sort_values([('rating', 'mean')], ascending=False).head())
print(movie_stats.sort_values([('rating', 'mean')], ascending=True).head())
