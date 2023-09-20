import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

class ModelHelper():
    def __init__(self):
        # select features for the model
        self.features = ['minplayers', 'maxplayers', 'maxplaytime',
        'age', 'total_weights',
       'mechanic_count', 'category_count', 'designer_count', 
       'category_clean_Adventure', 'category_clean_Educational',
       'category_clean_Era', 'category_clean_Expansion for Base-game',
       'category_clean_Other', 'category_clean_Strategy',
       'category_clean_Wargame', 'mechanic_clean_Co-op',
       'mechanic_clean_Dice_Rolling', 'mechanic_clean_Movement',
       'mechanic_clean_Other', 'mechanic_clean_PVP',
       'mechanic_clean_Role_Playing']


    def makePredictions(self, boardgame_name, min_rating, max_owners):
        df = pd.read_csv('./project_04_capstone/boardgames.csv')
        df_model = df.copy()
        # create a dataframe with only the relevant features
        # scale the features to a range between 0 and 1
        scaler = MinMaxScaler()
        df_model[self.features] = scaler.fit_transform(df[self.features])

        # create a dataframe with only the relevant features
        df_model = df_model.loc[:, ['id', 'name_clean','category_clean', 'mechanic_clean', 'average_rating', 'total_owners'] + self.features]

        # define the number of nearest neighbors to consider
        k = 25

        # initialize the model with the number of neighbors
        model = NearestNeighbors(n_neighbors=k)

        # fit the model to the data
        model.fit(df_model[self.features])

        # get the boardgame_id of the given boardgame name
        boardgame_id = df_model[df_model['name_clean'] == boardgame_name]['id'].iloc[0]
        
        # get the index of the boardgame in the model dataframe
        idx = df_model[df_model['id'] == boardgame_id].index[0]
        
        # get the features of the boardgame
        boardgame_features = df_model.loc[idx, self.features].values.reshape(1, -1)
        
        # find the k nearest neighbors
        distances, indices = model.kneighbors(boardgame_features)
        
        # get the boardgame names of the nearest neighbors
        boardgames = df.iloc[indices[0]]
        boardgames["distance"] = distances[0]

        # apply filters
        boardgames = boardgames.loc[boardgames.total_owners <= max_owners]   
        boardgames = boardgames.loc[boardgames.average_rating >= min_rating]   

        cols = ['id', 'name_clean','category_clean', 'mechanic_clean', 'average_rating', 'total_owners', 'minplayers', 'maxplayers', 'maxplaytime', 
                'age', 'total_weights', 'mechanic_count', 'category_count', 'designer_count', "distance"]

        boardgames = boardgames.loc[:, cols]
        boardgames = boardgames.sort_values(by = "distance")
        boardgames = boardgames.head(11).iloc[1:]


        return json.loads(boardgames.to_json(orient='records'))

