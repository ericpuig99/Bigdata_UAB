import pandas as pd
import glob
import json
import numpy as np


#creem una variable dataset que englobi tots els arxius json que volem analitzar
#creem una llista amb els noms dels polítics que volem analitzar

datasets = glob.glob("api_responses/*json")
llista_politics = ['Basha Changue', 'Ernest Maragall', 'Ada Colau', 'Jaume Collboni', 'Xavier Trias', 'Anna Grau',
                   'Eva Parera', 'Daniel Sirera']

#creem una sèrie de llistes que representen les variables que volem analitzar

llista_mencions = []
llista_autors = []
llista_likes = []
llista_retweets = []
llista_quoted = []
llista_replies = []

#creem una llista on s'afegirà la informació source i target
llista_graf = []


for data in datasets: #for que itera sobre cada arxiu json

    with open(data, encoding="utf-8") as f:
        pre_df = json.loads(f.read())

    tweets = tweets + len(pre_df['data']) #comptador que emmagatzema la quantitat de tweets que es processaran
    for tweet in pre_df['data']:
        lower_tweet = "" #variable per emmagatzemar els tweets en minúscules
        for word in tweet['text']:
            lower_tweet = lower_tweet + word.lower() #transformem les lletres en minus i les afegim a la variable lower_tweet
            lower_tweet = lower_tweet.replace(" ", "") #eliminem els espais en blanc del tweet

        for politic in llista_politics: #iterem dins de la llista de politics
            if politic.replace(" ", "").lower() in lower_tweet: #mirem que el nom coincideixi en els tweets
                llista_mencions.append(politic) #afegim el nom del polític a la llista mencions
                llista_likes.append(tweet['public_metrics']['like_count']) #afegim la variable likes dins la llista likes
                llista_retweets.append(tweet['public_metrics']['retweet_count']) #afegim la variable retweets dins de la seva llista
                llista_quoted.append(tweet['public_metrics']['quote_count']) #afegim la variable quotes dins la seva llista
                llista_replies.append(tweet['public_metrics']['reply_count']) #afegim la variable reply dins la seva llista

                author_id = tweet['author_id'] #igualem el id de l'usuari amb la variable author_id
                for user in pre_df['includes']['users']: #iterem sobre el llistat d'usuaris
                    if user['id'] == author_id: #si la variable id coincideix amb la variable author_id
                        user_name = user['username'] #la variable user_name serà igual al nom d'usuari
                        break

                    else:
                        pass
                llista_autors.append(user_name) #afegim el llistat d'usuaris dins de la llista_autors

                df_graf = pd.DataFrame({"source": user_name, "target": politic}, index=[0]) #afegim a ls llista graph el seu target i source
                llista_graf.append(df_graf)

df = pd.DataFrame(
    np.column_stack([llista_mencions, llista_autors, llista_likes, llista_retweets, llista_quoted, llista_replies]),
    columns=['politics_name', 'author_name', 'likes', 'retweets', 'quoted', 'replies'])

df_graf_final = pd.concat(llista_graf)

df_graf_final.to_csv("graf.csv", index=False)
df.to_csv('Mencions.csv', index=False)
