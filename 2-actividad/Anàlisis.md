## repercussió del polític a twitter mitjançant Tableau

A partir de l'extracció de dades amb Python hem volgut analitzar la repercussió dels polítics representats a l'ajuntament de Barcelona a la xarxa social Twitter.

Per poder portar a terme aquest anàlisis hem decidit treure una sèrie de variàbles que ens ajudin a determinar quins polítics tenen més influència sobre la població en base a un conjunt de tweets. Les variables escollides són les següents:
- Número d'usuaris que han parlat sobre un dels representants
- Número de likes dels tweets sobre els representats
- Número de retweets sobre tweets on es mencionen els  representats
- Número de quoted retweets sobre els tweets que mencionen el representats
- Número de respostes que han rebut els tweets que mencionen els representants

En base a aquestes variables hem extret els següents gràfics.

### Número d'usuaris que han parlat sobre els representats a l'ajuntament de Barcelona
[Nº mencions](https://user-images.githubusercontent.com/128310035/235765029-05f18ed9-17ad-4cdd-b108-2b7313b6affc.png)


Podem veure en aquest gràfic que l'actual alcadesa de Barcelona és la personalitat amb més mencions dins la xarxa social amb un total de 22.966 mencions, seguit per Xavier Trias amb 2.807 mencions, Eva Parera amb 1.119 mencions, Basha Changue amb 1.009 mencions, Anna Grau amb 835 mencions, Jaume Collboni amb 707 mencions i, per acabar, Daniel Sirera amb 601 mencions.

Es pot apreciar que la diferència de mencions és molt alta en quant a l'alcadesa amb els altres canditats a l'alcaldia de la capital de Catalunya.

### Número d'usuaris que han parlat sobre un dels candidats
[Nº usuaris](https://user-images.githubusercontent.com/128310035/235765091-6be253a7-3b76-4d46-b3e8-72573f08b8a5.png)


En aquest gràfic podem apreciar com, un altre cop, Ada Colau torna a liderar el gràfic amb un total de 14.528 usuaris que l'han mencionat, marcant una gran diferència amb la resta de candidats. Segueix Xavier Trias amb 2.070 usuaris diferents, Eva Parera amb 872, Basha Changue amb 693 usuaris, Anna Grau amb 610, Jaume Collboni 580 i Daniel Sirera amb 358 mencions.

### Mitjana de likes que tenen les mencions dels candidats
[Likes](https://user-images.githubusercontent.com/128310035/235765125-925c822b-3b9c-4d7c-bf05-069bc43e5e13.png)


Amb aquest gràfic podem analitzar que Jaume Collboni, representant del PSC a l'ajuntament de Barcelona, lidera el gràfic amb una mitjana de 3,27 likes per menció a la xarxa social de Twitter, seguit per Ada Colau amb molt poca diferència, Basha Changue posicionant-se per sota dels 2,8 likes de mitjana, Anna Grau, Xavier Trias, Eva Parera situant-se amb una mitjana de 1,6 likes per menció i finalitza amb Daniel Sirera i una mitjana al voltant de 1,3 likes per menció.

### Mitjana de Retweets pel conjunt de  tweets mencionats
[Retweets](https://user-images.githubusercontent.com/128310035/235765179-6dafbee3-c7ee-4d46-909a-a4be61d822a5.png)


En aquest gràfic veiem com els tweets on es parla d'Ada Colau reben una mitjana de 791 retweets, més del doble que la candidata del partit liberal Valents que se situa amb una mitjana de 318,4 retweets. A continuació trobem Jaume Collboni amb una mitjana de 105,4 retweets, seguit per Xavier Trias amb 68,4 retweets, Anna Grau amb 44,8 retweets, Basha Changue amb 37,3 i Daniel Sirera amb 27,9 retweets de mitjana.

### Mitjana de Quoted retweets
[Quoted](https://user-images.githubusercontent.com/128310035/235765214-cba7df47-54de-4be5-adc6-b71662b8474a.png)


En aquest apartat analitzem la mitjana de respostes citades que reben els tweets on es mencionen els polítics. Aquesta variable és útil per conèixer la repercursió dels tweets, doncs s'acostuma a veure que com més respostes citades al tweet s'acostuma a relacionar amb un tweet polèmic, doncs més gent està opinant sobre el tema.

### Respostes als tweets 

[Reply](https://user-images.githubusercontent.com/128310035/235765248-9dffadd0-8154-4bc5-ad3f-dbd16aba031d.png)


Els tweets amb més respostes són aquells que mencionen a la candidata de la CUP Basha Changue, seguit de Jaume Collboni, Anna Grau, Ada colau, Xavier Trias, Daniel Sirera i deixant en últim lloc a Eva Parera.

Aquests gràfics que hem analitzat ens donen a entendre una sèrie de punts que si es miren un per un poden donar a entendre poques conclusions, però si es miren en conjunt es pot treure un punt de vista interessant en relació al comportament dels usuaris amb els candidats a l'alcadia.

### Conclusions en les mencions amb Tableau


Primer destacar que l'alcaldesa de Barcelona no té twitter, però és la persona amb més repercursió a la xarxa amb diferència. Amb aquest estudi no podem analitzar si la seva repercussió és positiva o negativa amb una simple ullada, però només pel fet que amb la seva menció existeixi una activitat tan alta en comparació als demès, no poden ser bones notícies per a la candidata a renovar alcaldia. El que podem veure és que els tweets referents a Ada Colau tenen un bon feedback en relació al número de m’agrades, però no se situa en primera posició. En comparació amb el número de mencions podem dir que Jaume Collboni té molts millors resultats que l’alcaldesa tot i situar-se dècimes per sobre d’ella.

Tot i això, Jaume Collboni surt primer en les dades que fan referència a respostes citades d’un tweet. Com bé hem comentat anteriorment, tenir moltes respostes citades no acostuma a ser bo perquè representa que té molta repercussió. De la mateixa manera que se situa en segona posició amb les respostes als tweets mencionats, tercer amb una mitjana de retweets i tenint en compte que se situa en primera posició de likes, podriem parlar que, a l’igual que l’alcadesa, és una personalitat que l’audiència té molt a comentar, però no tant a compartir.

Els resultats que semblen ser curiosos son els de la Basha Changue que situantse en 4a posició de número de mencions, se situa poc per sota de la representant de Podem i el del PSC en quant a mitjana de m’agrades i primera en mitjana de respostes als tweets.

## Graph dels polítics

[graph](https://user-images.githubusercontent.com/128310035/235765276-502073c5-d823-4121-bce1-1f705f09ee84.png)


Aquest Graph té diferents eixos centrals. Cada un d'ells representa una personalitat política. En lila trobem l'actual alcadesa de Barcelona, Ada colau, en groc la Basha Changue, en blau turquesa en Jaume Collboni i en Xavier Trias, en blau fosc l'Eva Parera, en tarona l'Anna Grau i, per últim, en Daniel Sirera en vermell.

El primer que veiem és una esfera que rodeja l'etiqueta Ada Colau, fent referència la gran quantitat de mencions que ha rebut durant aquests últims mesos a la xarxa social. Podem definir que com més aprop està el cercle de sortida, més cops ha mencionat al node principal.

El segon node que més destaca és el de Xavier Trias que, per una banda, apareixen petits nodes de la part superior com a punt de sortida, però el que més crida l'atenció són aquells que no només es dediquen a parlar sobre el candidat de Junts, si no que també sobre l'actual alcadesa de la ciutat.

El mateix passa amb la resta de nodes que fan referència als altres candidats, sobretot el de la representant de Valents que sembla ser que les mateixes persones que parlen sobre Eva Parera també tenent a dir sobre Ada Colau.

A tot això, el cas que més crida l'atenció és el de Basha Changue que se situa molt per sobre dels altres candidats mantenint una distància prudencial sobre l'eix de les y respecta a la resta de candidats sense tenir en compte a l'Ada Colau.
