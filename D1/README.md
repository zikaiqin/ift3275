# Méthodologie

### Question 1

Nous avons calculé la racine à l'aide du script `nth_root.py`

### Question 4

Dans un premier temps, nous obtenons la représentation hexadécimale du message chiffré avec `bin2hex.py`

Par la suite, nous utilisons `crack.py` pour effectuer l'attaque crib drag avec les
[5000 mots les plus fréquents de la langue française.](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French/OpenSubtitles_Top_20K)

Finalement, à l'aide des résultats obtenus à l'étape précédente, nous utilisons l'outil `index.html` pour déchiffrer le message davantage.
