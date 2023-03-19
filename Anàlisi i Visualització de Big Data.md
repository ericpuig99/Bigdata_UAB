https://adriapadilla.github.io/bigdata-uab/ --> apunts
https://github.com/AdriaPadilla/bigdata-uab --> GitHub Adrià

14/03

**Dataset_twitch_gran**

```Python 
import pandas as pd
import pd

#columnes en el dataset
inici = time.time()
df = pd.read_csv("feb-full-2023.csv", sep="\t") #el dataset està separat per tabuladors
sampe = df.sample(frac=0.1) #agafem una mostra del 10% del dataset 
print (sample) #si utiltizem sample es carrega el dataset igualment i ens ralentitza molt l'ordinador.
final = time.time()



```


no volem carregar tot el dataset, per tant utilitzem nrows per carregar la fila que volem.

```Python 
import pandas as pd
import pd

#columnes en el dataset
inici = time.time()
df = pd.read_csv("feb-full-2023.csv", sep="\t", nrows=2)
print(df)
for col in df.columns:
	print(col)
	
final = time.time()
print(final-inici)



```

Definim els següents objectius:
- Stream més vist
- Total espectadors a la plataforma
- Streamer amb més followers
- Streamer amb més mitjana més alta
- Pic espectadors acumulats (suma tots espectadors)
- Joc més vist

```Python 

import pandas as pd
import pd

inici = time.time()
df = pd.read_csv("feb-full-2023.csv", 
				sep = "\t", #indiquem que el separador és un tabulador - \t
				nrows=2, #delimitem el nombre de files a llegir a 2.
				usecols=['captured_at"', "streamer_name", "viewer_count", "game_name", "stream_title"]) #indique, les columnes que volem

print(df)

posicio = df["viewer_count"].idmax()
print(df["streamer_name"].iloc[posicio], df["stream_title"].iloc[posicio], df["viewer_count"].iloc[posicio]) #amb això     imprimim la row amb les variables que volem, sobretot amb les dades d'espectadors.


				 
				
				
```


Nem a netejar el dataset centrant-nos només en el compte de la **Kings League**

```Python 
import pandas as pd
import pd

inici = time.time()
df = pd.read_csv("feb-full-2023.csv", 
				sep = "\t", #indiquem que el separador és un tabulador - \t
				nrows=10000, #delimitem el nombre de files a llegir a 100000
				usecols=["position","captured_at", "streamer_name", "viewer_count", "game_name", "stream_title"]) #indique, les columnes que volem
print(df)				
dades_kings_league = df[df["streamer_name"] == "kingsleague"]
print (dades_kings_league)
#falta info



```

Afegim el chunks, un bloc d'informació d'un tamany x
```Python 
import pandas as pd
import pd

inici = time.time()
df = pd.read_csv("feb-full-2023.csv", 
				sep = "\t", #indiquem que el separador és un tabulador - \t
				nrows=10000, #delimitem el nombre de files a llegir a 100000
				usecols=["position","captured_at", "streamer_name", "viewer_count", "game_name", "stream_title"]) #indique, les columnes que volem
				chunksize = 1000 #agafa el dataframe de n columnes i el carrega a blocs.
print(df)

llista_kings_league = [] #creem una llista on afegirem les dades dels blocs que ens interessa
for chunk in df: #itera per buscar les dades en blocs
	dades_kings_league = chunk[chunk["streamer_name"] == "kingsleague"]
	print (dades_kings_league) #de les primeres 1000 files, tindré les dades de la Kings League
	llista_kings_league.append(dades_kings_league)
final_frame = pd.concat(llista_kings_league) #pd.concat concatena tots els frames en una bbdd
final_frame.to.csv("kingsleague.csv")

```

*anar de 1000 a 1000 chunks és molt poc, sempre variarà en base a la quantitat de dades de la bbdd*





**Ejercicio 2**: Importación de Dataset y Trabajo con Datos
Planteamiento del problema
En este [archivo .csv](https://github.com/AdriaPadilla/bigdata-uab/blob/main/ejercicios/dataset_youtube.csv) tienes los datos extraídos de dos canales de YouTube. Se trata de los canales de las emisoras de rádio: "NPR" (National Public Rádio) y "KEXP" (Seattle International). Ambas emisoras tienen una larga tradición de conciertos en directo. El dataset contiene **todos los vídeos publicados por estas emisoras**. Queremos saber:

1.  Importa el dataset con Pandas
2.  ¿Cuantas filas y columnas tiene el dataset completo?
3.  ¿Qué columnas componen el dataset?
4.  Limpia los datos, si es necesario
5.  Elimina columnas, si es necesario
6.  Calcula cuantos vídeos ha publicado cada canal
7.  Calcula el promedio de espectadores/comentarios/likes que tiene cada uno de los canales
8.  Calcula la desviación de cada vídeo sobre el promedio de especatadores/comentarios/likes
9.  Localiza el vídeo más visto de cada canal
10.  Localiza el vídeo más comentado de cada canal
11.  Crea una nueva columna para cada uno de los valores calculador anteriormente, y crea un nuevo dataset final que incorpore toda la nueva información

```Python 
#1
import pandas as pd
df = pd.read_csv("dataset_youtube.csv") #importem el dataset
prindt(df)

#2
prindt(df.shape) #genera una tupla on el primer valor son les columnes i la segona són les files. (19128, 25)

#3
nombre_columnas = df.columns
for col in nombre_columnas:
	print (col)

#4 no cal
#5 Columnes que sobren: Position, PublisedAt, dislikecount, channelId, tags, category
df_net = df.drop ("position", "publishedAt", "dislikeCount", "channelId", axis=1, inplace=True)
	print(df_net, df.shape) #igualem el dataframe a un de nou a l'hora d'imprimir el df amb les columnes eliminades. Això és útil perquè si no ho respectem eliminem aquestes columnes indefinidament.

#6 Primer hem de saber quants canals hi ha
canals = df ["channelTtile"]
	print(canals) 
#volem saber les variables de la columna
canals_unics = df.channelTitle.unique()
print(canals_unics)

#hem de separar el df per filtrar-ho

df_1 = df.loc[df['channelTitle'] == "NPR Music"]]
df_2 = df.loc[df['channelTitle'] == "KEXP"]]
	print(df_1) #  NPR ens dona com a reusltat 2314 videos
	print (df_2) # KEXP ens dona com a resultat 16814 videos

#7 
print(df_1["viewCount"].mean()) 
print (df_2["viewCount"].mean())
#els resultats donan massa decimals
print(round(df_1["viewCount"].mean(),2)) 
print (round(df_2["viewCount"].mean(),2)) 
#arrodonim a 2 decimals

#volem un resultat maco i estructurat
print(f"El canal NPR té un total de {df_1.shape[0]} videos") #NPR
print(f"El canal KEXP té un total de {df_2.shape[0]} videos") #KEXP

print(f"El promig d'espectador de NPR és de : {round(df_1["viewCount"].mean(),2)}")

print(round(df_1["viewCount"].mean(),2)) 
print (round(df_2["viewCount"].mean(),2)) 


#9 Demana calcular la diferència absoluta entre videos. És a dir si destaca per pobre o per massa. Necessitem tenir el promig com a variable en el df.

prom_espectador_1 = round(df_1["viewCount"].meamn(),2)
prom_espectador_2 = round(df_2["viewCount"].meamn(),2)

#hem de iterar per cada una de les files. Agafar el valor de viewers i restar el valor promig.

list_desviacio = []
for index, row in df_1.iterrows():
	desviacio = prom_espectadors1 - row["viewcount"]
	list_desviacio.append(desviacio)
	

def_1["desviacio"]
=
```
Pandas és el centre de tot. Ens permet transformar les dades per poder analitzar.  És un estàndard en la indústria.



----------
07/03
qyzfms4ue7ahwvw71fu2bhb1ke3z5v
0c06xau3qas1ln1xr0t3d2c3xsdll3

```Python 
from twitchAPI.twitch import Twitch
importat json

twitch = Twitch 
```

```Python
stream= twitch.get_streams(first=20, language="es")
print (streams)```

Com a resultat dona una llista de valors en format taula

```python 
data = streams 
for d in data: 
print(d)```

El següent fragment de codi crea un arxiu OUPUT FILE.JSOn on hi posa el resultat a dins i el guarda:
```Python
 with open("output_file.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)```
*** hem d'afegir la llibreria JSON al header.
Aquest document s'utilitza per analitzar les dades que ens ofereix el codi. En aquest cas ens dona dades del directe.

Ara transformarem les dades en un CSV per interpretar-ho en tableau.
D'aquestes dades del directe agafarem les següents dades a analtizar:
- user_id
- game_name
- game_id
- game_name
- title
- viewer_count
- started_at --> és la data de l'inici del stream
*cal conèixer en el moment que s'han extret les dades, per això afegim*:
- captured_at

```python 
dades = stream["data"]
#data es la llibreria de dades del stream
for dada in dades:
	user_id = dada["user_id"]
	user_name = dada ["user_name"]
	game_id = dada["game_id"]
	game_name = dada["game_name"]
	title = dada["title"]
	viewers_count = dada["viewer_count"]
	started_at = dada['started_at']
	is_mature = dada["is_mature"]
	captured_at = now
	```
Per conèixer en el moment que hem tret les dades--> 
```Python
import datetime
now = datetime.datetime.now()
print(now)```

Anem a crear un data frame per passar les dades a CSV

```Python
import pandas as pd


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   print(df) #variable que conté el contingut que volem imprimir sobre la taula
				
				   ```

Hem de guardar fora del for una llista de dataframes buida per afegir les dades imprimides dins de la mateixa llista

```Python
data_frame = [] #això va fora del for

llista_dataframes.append(df)
print(llista_dataframes)```

Ara cal concatenar les dades en una mateixa taula pel CSV
```python
final_dataframe = pd.concat(llista_dataframes)
print(final_dataframe)```

Ara exportem les dades a CSV
```python
final_dataframe.to_csv("export.csv", index=False)```


La API no et permetrà analitzar una serie ilimitada de streams. El màxim nª d'Items és de 100.

L'arxiu JSON, al final, hi ha la "pagination" y "cursor", això ens permet posicionar els streams per després jugar amb el "after", "before", "first".

```Python 
stream= twitch.get_streams(first=20, language="es", after = "cursor") #el cursor fa referencia a un codi identificatiu.
```

**Funcions**

Com definir una funció a Python
```python
def loquesea():
	print("hola")
loquesea() #imprimeix hola

variable = "hola"
def loquesea(variable):
	print(variable)
loquesea(variable) #imprimeix hola

variable = "hola"
variable_2 = "adeu"

def loquesea(pip, cac):
	print(pip, cac)

loquesea(variable, variable_2) #imprimeix "hola" i "adeu"
```
Podem enviar funcions dins d'una variable???? Ho mirem més tard

Ara volem reutilitzar el següent codi per saber les dades de més de 100 streams

```Python 
stream= twitch.get_streams(first=20, language="es")
```

Creem el següent

```python
data_frame = [] #el treiem fora per no maxacar la llista
def crida():
stream= twitch.get_streams(first=100, language="es")
dades = stream["data"]


for dada in dades:
	user_id = dada["user_id"]
	user_name = dada ["user_name"]
	game_id = dada["game_id"]
	game_name = dada["game_name"]
	title = dada["title"]
	viewers_count = dada["viewer_count"]
	started_at = dada['started_at']
	is_mature = dada["is_mature"]
	captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)
			
crida()

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)
```


Necessitem la segona volta de recolecció de dataframes (següent tanda de streams)

```Python
data_frame = [] #el treiem fora per no maxacar la llista
def crida():
stream= twitch.get_streams(first=100, language="es")
dades = stream["data"]


for dada in dades:
	user_id = dada["user_id"]
	user_name = dada ["user_name"]
	game_id = dada["game_id"]
	game_name = dada["game_name"]
	title = dada["title"]
	viewers_count = dada["viewer_count"]
	started_at = dada['started_at']
	is_mature = dada["is_mature"]
	captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)
				   cursos = streams["pagination"]["cursor"]
				   print["cursor"] #imprimeix el cursor de cada stream
	
crida()

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)
```


Seguim

```Python
data_frame = [] #el treiem fora per no maxacar la llista
def crida():
stream= twitch.get_streams(first=100, language="es", after=cursor)
dades = stream["data"]


for dada in dades:
	user_id = dada["user_id"]
	user_name = dada ["user_name"]
	game_id = dada["game_id"]
	game_name = dada["game_name"]
	title = dada["title"]
	viewers_count = dada["viewer_count"]
	started_at = dada['started_at']
	is_mature = dada["is_mature"]
	captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)
				   cursos = streams["pagination"]["cursor"]
				   crida(cursor) #aquí falta un valor a cursor
	
crida()

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)
```

A la crida anterior no tenim valor al cursor:
Variables dummy

```Python
data_frame = [] #el treiem fora per no maxacar la llista
cursor_dummy = None
def crida():
stream= twitch.get_streams(first=100, language="es", after=cursor)
dades = stream["data"]


for dada in dades:
	user_id = dada["user_id"]
	user_name = dada ["user_name"]
	game_id = dada["game_id"]
	game_name = dada["game_name"]
	title = dada["title"]
	viewers_count = dada["viewer_count"]
	started_at = dada['started_at']
	is_mature = dada["is_mature"]
	captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)


	cursor = streams["pagination"]["cursor"]
	crida(cursor) 
crida(cursor_dummy)

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)

```

A la última pàgina no existeix cursor perquè no hi ha pàgina següent, per tant:

```Python
data_frame = [] #el treiem fora per no maxacar la llista
cursor_dummy = None
def crida():
	stream= twitch.get_streams(first=20, language="ca", after=cursor)
	dades = stream["data"]


		for dada in dades:
			user_id = dada["user_id"]
			user_name = dada ["user_name"]
			game_id = dada["game_id"]
			game_name = dada["game_name"]
			title = dada["title"]
			viewers_count = dada["viewer_count"]
			started_at = dada['started_at']
			is_mature = dada["is_mature"]
			captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)
				print(len(llista_dataframes))
				if streams["pagination"]["cursor"]:
				cursor = streams["pagination"]["cursor"]
				print(cursor)
				crida(cursor)
				


	cursor = streams["pagination"]["cursor"]
	crida(cursor) 
crida(cursor_dummy)

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)

```

La API de Twitch no permet consultes al servidor tot el rato, per tant hem d'afegir una llibreria.

```python
import time

```

Aleshores

```Python
data_frame = [] #el treiem fora per no maxacar la llista
cursor_dummy = None
def crida():
	stream= twitch.get_streams(first=20, language="ca", after=cursor)
	dades = stream["data"]


		for dada in dades:
			user_id = dada["user_id"]
			user_name = dada ["user_name"]
			game_id = dada["game_id"]
			game_name = dada["game_name"]
			title = dada["title"]
			viewers_count = dada["viewer_count"]
			started_at = dada['started_at']
			is_mature = dada["is_mature"]
			captured_at = now


df = pd.DataFrame({
				   "captured_at": captured_at,
				   "user_id": user_id,
				   "user_name": user_name,
				   "game_id": game_id,
				   "game_name": game_name,
				   "title": title,
				   "viewer_count": viewer_count,
				   "started_at": started_at,
				   "is_mature": is_mature,
				   }, index=[0])
				   llista_dataframes.append(df)
				print(len(llista_dataframes))
				
				
				try:
					streams["pagination"]["cursor"]:
					cursor = streams["pagination"]["cursor"]
					print(cursor)
					print ("dormint")
					time.slepp(1)
					crida(cursor)
				except KeyError:
					print("ultima pagina")
					pass
			
				


	cursor = streams["pagination"]["cursor"]
	crida(cursor) 
crida(cursor_dummy)

final_dataframe = pd.concat(llista_dataframe)
final_dataframe.to_csv("export.csv", index = False)
print (final_dataframe)
```


