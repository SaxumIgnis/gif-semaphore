# Générateur de messages semaphore GIF

Petit projet qui consiste à automatiser la création de messages en sémaphore sous forme de gif animés   

Maintenant il a une GUI ^^

## Utilisation

Télécharger et decompresser la release correspondant à votre OS

Exécuter le fichier gif-semaphore (gif-semaphore.exe pour Windows)


### Ajouts de modèles

Les modèles doivent être ajoutés dans le dossier _resources_.

Chaque modèle doit être placé dans son propre dossier.

Un modèle est composé de :
-   une image par lettre, en majuscule (A.png - Z.png)
-   une image +.png pour l'espace
-   une image -.png pour la fin de message
-   une image 0.png pour le passage en numérique

Dans le doute, prendre exemple sur le modèle _basic_

Tous les formats d'image sont acceptés cependant le format doit être le même pour toutes les images d'un modèle

## Informations pour les développeurs

### Build

Les fichiers exécutables sont générés avec [pyinstaller](https://github.com/pyinstaller/pyinstaller) dans le dossier dist

`$ pyinstaller -F -n gif-semaphore sources/gui.py`


### Dépendances

-   [python 3.4+](https://www.python.org)
-   [imageio](https://pypi.org/project/imageio/)
-   [tkinter](https://docs.python.org/3/library/tkinter.html)

## License

Ce programme est un logiciel libre : vous pouvez le redistribuer et/ou le modifier
selon les termes de la licence publique générale GNU publiée par
la Free Software Foundation, soit la version 3 de la licence, ou
(à votre choix) toute version ultérieure.

Ce programme est distribué dans l'espoir qu'il sera utile,
mais SANS AUCUNE GARANTIE ; sans même la garantie implicite de
la qualité marchande ou l'adéquation à un usage particulier.  Voir le
Licence publique générale GNU pour plus de détails.

Vous devriez avoir reçu une copie de la licence publique générale de GNU
en même temps que ce programme.  Si ce n'est pas le cas, voir <https://www.gnu.org/licenses/>.
