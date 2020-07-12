{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "column_names = ['user_id', 'item_id', 'rating', 'timestamp']\n",
    "df = pd.read_csv('u.data', sep = '\\t', names = column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>172</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>133</td>\n",
       "      <td>1</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>196</td>\n",
       "      <td>242</td>\n",
       "      <td>3</td>\n",
       "      <td>881250949</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>186</td>\n",
       "      <td>302</td>\n",
       "      <td>3</td>\n",
       "      <td>891717742</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp\n",
       "0        0       50       5  881250949\n",
       "1        0      172       5  881250949\n",
       "2        0      133       1  881250949\n",
       "3      196      242       3  881250949\n",
       "4      186      302       3  891717742"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>item_id</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>GoldenEye (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Four Rooms (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Get Shorty (1995)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Copycat (1995)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   item_id              title\n",
       "0        1   Toy Story (1995)\n",
       "1        2   GoldenEye (1995)\n",
       "2        3  Four Rooms (1995)\n",
       "3        4  Get Shorty (1995)\n",
       "4        5     Copycat (1995)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "movie_titles = pd.read_csv(\"Movie_Id_Titles\") # getting the movie titles\n",
    "movie_titles.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>user_id</th>\n",
       "      <th>item_id</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "      <th>title</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>881250949</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>290</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>880473582</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>79</td>\n",
       "      <td>50</td>\n",
       "      <td>4</td>\n",
       "      <td>891271545</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>888552084</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>50</td>\n",
       "      <td>5</td>\n",
       "      <td>879362124</td>\n",
       "      <td>Star Wars (1977)</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   user_id  item_id  rating  timestamp             title\n",
       "0        0       50       5  881250949  Star Wars (1977)\n",
       "1      290       50       5  880473582  Star Wars (1977)\n",
       "2       79       50       4  891271545  Star Wars (1977)\n",
       "3        2       50       5  888552084  Star Wars (1977)\n",
       "4        8       50       5  879362124  Star Wars (1977)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.merge(df, movie_titles, on = 'item_id')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Exploring the data and get a look at some of the best rated movies."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "sns.set_style('white')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Creating a ratings dataframe with average rating and number of ratings."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Marlene Dietrich: Shadow and Light (1996)     5.0\n",
       "Prefontaine (1997)                            5.0\n",
       "Santa with Muscles (1996)                     5.0\n",
       "Star Kid (1997)                               5.0\n",
       "Someone Else's America (1995)                 5.0\n",
       "Name: rating, dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].mean().sort_values(ascending = False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "title\n",
       "Star Wars (1977)             584\n",
       "Contact (1997)               509\n",
       "Fargo (1996)                 508\n",
       "Return of the Jedi (1983)    507\n",
       "Liar Liar (1997)             485\n",
       "Name: rating, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('title')['rating'].count().sort_values(ascending = False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating\n",
       "title                              \n",
       "'Til There Was You (1997)  2.333333\n",
       "1-900 (1994)               2.600000\n",
       "101 Dalmatians (1996)      2.908257\n",
       "12 Angry Men (1957)        4.344000\n",
       "187 (1997)                 3.024390"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings = pd.DataFrame(df.groupby('title')['rating'].mean())\n",
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Setting the no of ratings column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating  no_of_ratings\n",
       "title                                             \n",
       "'Til There Was You (1997)  2.333333              9\n",
       "1-900 (1994)               2.600000              5\n",
       "101 Dalmatians (1996)      2.908257            109\n",
       "12 Angry Men (1957)        4.344000            125\n",
       "187 (1997)                 3.024390             41"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings['no_of_ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())\n",
    "ratings.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2216e2d9c88>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10, 4))\n",
    "ratings['no_of_ratings'].hist(bins = 70)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2216e401ec8>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize = (10, 4))\n",
    "ratings['rating'].hist(bins = 70)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "from the ratings histogram we can say that most of the peoples have given ratings between 3-5 and we can see some outliers also."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.JointGrid at 0x2216e9c6a08>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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vtby/ddffz0/+MEP5nWMZk+nB+9a+BtYM1rdZJeC0+m8QHxuWtHqYWApOJ3OC8yvhnKhee1dDzUErPrMwUJwIvfClzNLHqx83+eOO+5g7969CCH49Kc/zebNm1u+/0z7A8XExMQ040y7Fy55GlBVVf7+7/9+qYcRExMTE3Mas+TS9ZiYmJiYmNmIg1VMTExMzGlPHKxiYmJiYk574mAVExMTE3PaEwermJiYmJjTnjhYxcTExMSc9sTBKiYmJibmtCcOVjExMTExpz1xsIqJiYmJOe1ZcgeL+dLf38/111+/1MOIiYmJOeV0dnby9a9/fc7vPZNYcm/AmJiYmJiY2YjTgDExMTExpz1xsIqJiYmJOe2Jg1VMTExMzGlPHKxiYmJiYk574mAVExMTE3PaEwermJiYmJjTnmUbrJ599lluuummadt/8YtfcMMNN3DjjTdy//33L+lYvvnNb/LGN76Rm266iZtuuon9+/cv6Dgcx+FjH/sY7373u3nb297Gww8/3PD6Yp6b2caymOfG8zxuu+023vnOd/Ke97yHw4cPN7y+2NfMbONZ7OsGYHR0lKuuuop9+/Y1bF+K71OrsSzFeXnrW98aHe+2225reO3+++/n+uuv5x3veAePPPLIgo9l2SOWIV/5ylfEddddJ97+9rc3bLdtW1x99dViYmJCWJYlrr/+ejE0NLQkYxFCiI985CNi586dC3r8er7//e+Lf/iHfxBCCDE2Niauuuqq6LXFPjczjUWIxT03P//5z8Wtt94qhBDit7/9rbj55puj15bimplpPEIs/nVj27b4wAc+IN7whjeIl156qWH7Yp+bVmMRYvHPS61WE295y1uavjY0NCSuu+46YVmWKBQK0b9jTpxlObNav349d99997Tt+/btY/369bS3t2OaJq985St56qmnlmQsALt27eIrX/kK73rXu/iXf/mXBR0HwLXXXstf//VfRz9rmhb9e7HPzUxjgcU9N1dffTV33nknAMeOHaOnpyd6bSmumZnGA4t/3Xz2s5/lne98JytWrGjYvhTnptVYYPHPy549e6hWq7zvfe/jve99L9u3b49e27FjB5dccgmmaZLL5Vi/fj179uxZ8DEtZ5ZlsLrmmmvQ9elOUqVSiVwuF/2cyWQolUpLMhaAN77xjdxxxx3827/9G08//fSCpwoymQzZbJZSqcRf/dVf8aEPfSh6bbHPzUxjgcU/N7qu84lPfII777yTa665Jtq+FNfMTOOBxT03P/jBD+jq6uK1r33ttNcW+9zMNBZY/GsmmUzy/ve/n69//ev83d/9HR/96EdxXRdYuutmObMsg1Urstks5XI5+rlcLjdcUIuJEII/+ZM/oaurC9M0ueqqq3j++ecX/LjHjx/nve99L295y1t405veFG1finPTaixLdW4++9nP8rOf/Yzbb7+dSqUCLO0102w8i31uHnjgAf7zP/+Tm266id27d/OJT3yC4eFhYPHPzUxjWYprZuPGjbz5zW9GURQ2btxIR0fHkp2bM4EzKlht3ryZQ4cOMTExgW3bPPXUU1xyySVLMpZSqcR1111HuVxGCMHjjz/OBRdcsKDHHBkZ4X3vex8f+9jHeNvb3tbw2mKfm5nGstjn5oc//GGUNkqlUiiKEqUll+KamWk8i31u7rvvPr71rW9x7733ct555/HZz36W3t5eYPHPzUxjWYrv0/e//33uuusuAAYHBymVStF4tm3bxtNPP41lWRSLRfbt28fWrVsXdDzLnZed6/qJ8OMf/5hKpcKNN97Irbfeyvvf/36EENxwww309fUt2VhuueUW3vve92KaJq961au46qqrFvTY99xzD4VCgS9/+ct8+ctfBuDtb3871Wp10c/NbGNZzHPzhje8gdtuu433vOc9uK7LJz/5SR588MElu2ZmG89iXzdTib9Pkre97W3cdtttvOtd70JRFD796U9z7733sn79ev7wD/+Qm266iXe/+90IIbjllltIJBILOp7lTuy6HhMTExNz2nNGpQFjYmJiYl6exMEqJiYmJua0Jw5WMTExMTGnPXGwiomJiYk57YmDVUxMTEzMaU8crGJi6rAsi+9973uAdEyYarAbExOzNMTS9ZiYOo4ePcqHP/zhRXMQj4mJmRtnRFFwTEzID37wAx544AF83+faa6/l4YcfxnVdcrkcd999N/fccw8vvfQSX/rSlxBC0NPTw6ZNm/jqV7+KYRgcPXqUP/7jP+Yv/uIvOHToELfeeiu6rrNmzRr6+/u59957l/ojxsQsS+I0YMwZR1tbG/fddx/FYpF//dd/5dvf/jau67Jz505uvvlmzj77bP7yL/+y4XeOHTvG3XffzXe/+12+9rWvAfC5z32Om2++mXvvvZdLL710KT5KTMwZQzyzijnj2LhxI6qqYhgGH/7wh0mn0wwMDESO2c3YunUruq6j6zrJZBKQLTJCL7xXvvKV/PjHP16U8cfEnInEM6uYMw5VVdmzZw8PPfQQX/ziF7n99tvxfR8hBKqq4vv+tN9RFGXatq1bt/K73/0OkN2gY2JiFo54ZhVzRrJhwwZSqRTXX389pmnS29vL0NAQl1xyCY7j8I//+I/RDKoVH/3oR/nkJz/JN77xDXK5XMu+ZTExMSdPrAaMiTlBfvSjH3HRRRexYcMGvve97/HMM8/wmc98ZqmHFROzLIkfBWNiTpBVq1Zxyy23kEqlUFWVT3/600s9pJiYZUs8s4qJiYmJOe2JBRYxMTExMac9cbCKiYmJiTntiYNVTExMTMxpTxysYmJiYmJOe+JgFRMTExNz2vP/A3nbySnWDMy1AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x432 with 3 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.jointplot(x = 'rating', y = 'no_of_ratings', data = ratings, alpha = 0.6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Recommending Similar Movies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>title</th>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <th>187 (1997)</th>\n",
       "      <th>2 Days in the Valley (1996)</th>\n",
       "      <th>20,000 Leagues Under the Sea (1954)</th>\n",
       "      <th>2001: A Space Odyssey (1968)</th>\n",
       "      <th>3 Ninjas: High Noon At Mega Mountain (1998)</th>\n",
       "      <th>39 Steps, The (1935)</th>\n",
       "      <th>...</th>\n",
       "      <th>Yankee Zulu (1994)</th>\n",
       "      <th>Year of the Horse (1997)</th>\n",
       "      <th>You So Crazy (1994)</th>\n",
       "      <th>Young Frankenstein (1974)</th>\n",
       "      <th>Young Guns (1988)</th>\n",
       "      <th>Young Guns II (1990)</th>\n",
       "      <th>Young Poisoner's Handbook, The (1995)</th>\n",
       "      <th>Zeus and Roxanne (1997)</th>\n",
       "      <th>unknown</th>\n",
       "      <th>Á köldum klaka (Cold Fever) (1994)</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>user_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 1664 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "title    'Til There Was You (1997)  1-900 (1994)  101 Dalmatians (1996)  \\\n",
       "user_id                                                                   \n",
       "0                              NaN           NaN                    NaN   \n",
       "1                              NaN           NaN                    2.0   \n",
       "2                              NaN           NaN                    NaN   \n",
       "3                              NaN           NaN                    NaN   \n",
       "4                              NaN           NaN                    NaN   \n",
       "\n",
       "title    12 Angry Men (1957)  187 (1997)  2 Days in the Valley (1996)  \\\n",
       "user_id                                                                 \n",
       "0                        NaN         NaN                          NaN   \n",
       "1                        5.0         NaN                          NaN   \n",
       "2                        NaN         NaN                          NaN   \n",
       "3                        NaN         2.0                          NaN   \n",
       "4                        NaN         NaN                          NaN   \n",
       "\n",
       "title    20,000 Leagues Under the Sea (1954)  2001: A Space Odyssey (1968)  \\\n",
       "user_id                                                                      \n",
       "0                                        NaN                           NaN   \n",
       "1                                        3.0                           4.0   \n",
       "2                                        NaN                           NaN   \n",
       "3                                        NaN                           NaN   \n",
       "4                                        NaN                           NaN   \n",
       "\n",
       "title    3 Ninjas: High Noon At Mega Mountain (1998)  39 Steps, The (1935)  \\\n",
       "user_id                                                                      \n",
       "0                                                NaN                   NaN   \n",
       "1                                                NaN                   NaN   \n",
       "2                                                1.0                   NaN   \n",
       "3                                                NaN                   NaN   \n",
       "4                                                NaN                   NaN   \n",
       "\n",
       "title    ...  Yankee Zulu (1994)  Year of the Horse (1997)  \\\n",
       "user_id  ...                                                 \n",
       "0        ...                 NaN                       NaN   \n",
       "1        ...                 NaN                       NaN   \n",
       "2        ...                 NaN                       NaN   \n",
       "3        ...                 NaN                       NaN   \n",
       "4        ...                 NaN                       NaN   \n",
       "\n",
       "title    You So Crazy (1994)  Young Frankenstein (1974)  Young Guns (1988)  \\\n",
       "user_id                                                                      \n",
       "0                        NaN                        NaN                NaN   \n",
       "1                        NaN                        5.0                3.0   \n",
       "2                        NaN                        NaN                NaN   \n",
       "3                        NaN                        NaN                NaN   \n",
       "4                        NaN                        NaN                NaN   \n",
       "\n",
       "title    Young Guns II (1990)  Young Poisoner's Handbook, The (1995)  \\\n",
       "user_id                                                                \n",
       "0                         NaN                                    NaN   \n",
       "1                         NaN                                    NaN   \n",
       "2                         NaN                                    NaN   \n",
       "3                         NaN                                    NaN   \n",
       "4                         NaN                                    NaN   \n",
       "\n",
       "title    Zeus and Roxanne (1997)  unknown  Á köldum klaka (Cold Fever) (1994)  \n",
       "user_id                                                                        \n",
       "0                            NaN      NaN                                 NaN  \n",
       "1                            NaN      4.0                                 NaN  \n",
       "2                            NaN      NaN                                 NaN  \n",
       "3                            NaN      NaN                                 NaN  \n",
       "4                            NaN      NaN                                 NaN  \n",
       "\n",
       "[5 rows x 1664 columns]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moviemat = df.pivot_table(index = 'user_id', columns = 'title', values = 'rating')\n",
    "moviemat.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>4.359589</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Contact (1997)</th>\n",
       "      <td>3.803536</td>\n",
       "      <td>509</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fargo (1996)</th>\n",
       "      <td>4.155512</td>\n",
       "      <td>508</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>4.007890</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>3.156701</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>English Patient, The (1996)</th>\n",
       "      <td>3.656965</td>\n",
       "      <td>481</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Scream (1996)</th>\n",
       "      <td>3.441423</td>\n",
       "      <td>478</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Toy Story (1995)</th>\n",
       "      <td>3.878319</td>\n",
       "      <td>452</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Air Force One (1997)</th>\n",
       "      <td>3.631090</td>\n",
       "      <td>431</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Independence Day (ID4) (1996)</th>\n",
       "      <td>3.438228</td>\n",
       "      <td>429</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                 rating  no_of_ratings\n",
       "title                                                 \n",
       "Star Wars (1977)               4.359589            584\n",
       "Contact (1997)                 3.803536            509\n",
       "Fargo (1996)                   4.155512            508\n",
       "Return of the Jedi (1983)      4.007890            507\n",
       "Liar Liar (1997)               3.156701            485\n",
       "English Patient, The (1996)    3.656965            481\n",
       "Scream (1996)                  3.441423            478\n",
       "Toy Story (1995)               3.878319            452\n",
       "Air Force One (1997)           3.631090            431\n",
       "Independence Day (ID4) (1996)  3.438228            429"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.sort_values('no_of_ratings', ascending = False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's choose two movies Star Wars, a sci-fi movie and Liar Liar, a comedy movie."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>rating</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>2.333333</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>2.600000</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>2.908257</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>4.344000</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>3.024390</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                             rating  no_of_ratings\n",
       "title                                             \n",
       "'Til There Was You (1997)  2.333333              9\n",
       "1-900 (1994)               2.600000              5\n",
       "101 Dalmatians (1996)      2.908257            109\n",
       "12 Angry Men (1957)        4.344000            125\n",
       "187 (1997)                 3.024390             41"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now taking the movie ratings of these two movies:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "user_id\n",
       "0    5.0\n",
       "1    5.0\n",
       "2    5.0\n",
       "3    NaN\n",
       "4    5.0\n",
       "Name: Star Wars (1977), dtype: float64"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "starwars_user_ratings = moviemat['Star Wars (1977)']\n",
    "liarliar_user_ratings = moviemat['Liar Liar (1997)']\n",
    "starwars_user_ratings.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use corrwith() method to get correlations between two pandas series:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\nites\\anaconda3\\lib\\site-packages\\numpy\\lib\\function_base.py:2526: RuntimeWarning: Degrees of freedom <= 0 for slice\n",
      "  c = cov(x, y, rowvar)\n",
      "C:\\Users\\nites\\anaconda3\\lib\\site-packages\\numpy\\lib\\function_base.py:2455: RuntimeWarning: divide by zero encountered in true_divide\n",
      "  c *= np.true_divide(1, fact)\n"
     ]
    }
   ],
   "source": [
    "similar_to_starwars = moviemat.corrwith(starwars_user_ratings)\n",
    "similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lets clean this by removing  NaN values and using a dataFrame instead of a series:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation\n",
       "title                                 \n",
       "'Til There Was You (1997)     0.872872\n",
       "1-900 (1994)                 -0.645497\n",
       "101 Dalmatians (1996)         0.211132\n",
       "12 Angry Men (1957)           0.184289\n",
       "187 (1997)                    0.027398"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars = pd.DataFrame(similar_to_starwars, columns = ['Correlation'])\n",
    "corr_starwars.dropna(inplace = True)\n",
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now if we sort the dataframe by correlation, we should get the most similar movies, however we will some results that don't really make sense. This is because there are a lot of movies only watched once by users who also watched stars was "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Commandments (1997)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Cosi (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>No Escape (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Stripes (1981)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Man of the Year (1995)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hollow Reed (1996)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Beans of Egypt, Maine, The (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Good Man in Africa, A (1994)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Old Lady Who Walked in the Sea, The (Vieille qui marchait dans la mer, La) (1991)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Outlaw, The (1943)</th>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation\n",
       "title                                                          \n",
       "Commandments (1997)                                         1.0\n",
       "Cosi (1996)                                                 1.0\n",
       "No Escape (1994)                                            1.0\n",
       "Stripes (1981)                                              1.0\n",
       "Man of the Year (1995)                                      1.0\n",
       "Hollow Reed (1996)                                          1.0\n",
       "Beans of Egypt, Maine, The (1994)                           1.0\n",
       "Good Man in Africa, A (1994)                                1.0\n",
       "Old Lady Who Walked in the Sea, The (Vieille qu...          1.0\n",
       "Outlaw, The (1943)                                          1.0"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars.sort_values('Correlation', ascending = False).head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now lets fix this by filtering out movies that have less than 100 reviews (this value is chosen based off the histogram from earlier)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>'Til There Was You (1997)</th>\n",
       "      <td>0.872872</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1-900 (1994)</th>\n",
       "      <td>-0.645497</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>101 Dalmatians (1996)</th>\n",
       "      <td>0.211132</td>\n",
       "      <td>109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12 Angry Men (1957)</th>\n",
       "      <td>0.184289</td>\n",
       "      <td>125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>187 (1997)</th>\n",
       "      <td>0.027398</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           Correlation  no_of_ratings\n",
       "title                                                \n",
       "'Til There Was You (1997)     0.872872              9\n",
       "1-900 (1994)                 -0.645497              5\n",
       "101 Dalmatians (1996)         0.211132            109\n",
       "12 Angry Men (1957)           0.184289            125\n",
       "187 (1997)                    0.027398             41"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars = corr_starwars.join(ratings['no_of_ratings'])\n",
    "corr_starwars.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Star Wars (1977)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>584</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Empire Strikes Back, The (1980)</th>\n",
       "      <td>0.748353</td>\n",
       "      <td>368</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Return of the Jedi (1983)</th>\n",
       "      <td>0.672556</td>\n",
       "      <td>507</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Raiders of the Lost Ark (1981)</th>\n",
       "      <td>0.536117</td>\n",
       "      <td>420</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Austin Powers: International Man of Mystery (1997)</th>\n",
       "      <td>0.377433</td>\n",
       "      <td>130</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                    Correlation  no_of_ratings\n",
       "title                                                                         \n",
       "Star Wars (1977)                                       1.000000            584\n",
       "Empire Strikes Back, The (1980)                        0.748353            368\n",
       "Return of the Jedi (1983)                              0.672556            507\n",
       "Raiders of the Lost Ark (1981)                         0.536117            420\n",
       "Austin Powers: International Man of Mystery (1997)     0.377433            130"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_starwars[corr_starwars['no_of_ratings'] > 100].sort_values('Correlation', ascending = False).head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now the same for comedy Liar Liar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Correlation</th>\n",
       "      <th>no_of_ratings</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>title</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Liar Liar (1997)</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>485</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Batman Forever (1995)</th>\n",
       "      <td>0.516968</td>\n",
       "      <td>114</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mask, The (1994)</th>\n",
       "      <td>0.484650</td>\n",
       "      <td>129</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Down Periscope (1996)</th>\n",
       "      <td>0.472681</td>\n",
       "      <td>101</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Con Air (1997)</th>\n",
       "      <td>0.469828</td>\n",
       "      <td>137</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Correlation  no_of_ratings\n",
       "title                                            \n",
       "Liar Liar (1997)          1.000000            485\n",
       "Batman Forever (1995)     0.516968            114\n",
       "Mask, The (1994)          0.484650            129\n",
       "Down Periscope (1996)     0.472681            101\n",
       "Con Air (1997)            0.469828            137"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "corr_liarliar = pd.DataFrame(similar_to_liarliar, columns = ['Correlation'])\n",
    "corr_liarliar.dropna(inplace = True)\n",
    "corr_liarliar = corr_liarliar.join(ratings['no_of_ratings'])\n",
    "corr_liarliar[corr_liarliar['no_of_ratings'] > 100].sort_values('Correlation', ascending = False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
