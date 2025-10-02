|             Liste légos             | Couleur | Resultat attendu |                 Raison du test                  |
|:-----------------------------------:|:-------:|:----------------:|:-----------------------------------------------:|
|      ["rouge", "bleu", "bleu"]      | "bleu"  |      33.33       |            Vérifier l'arrondissment             |
| ["rouge", "jaune", "bleu", "bleu"]  | "bleu"  |      50.00       |              Fonctionnement normal              |
| ["rouge", "jaune", "bleu", "bleu"]  | "vert"  |       0.00       |           Gérer les couleurs absentes           |
|                 []                  | "vert"  |       0.00       |             Gérer les listes vides              |
| ["rouge", "jaune", "bleu", "bleu"]  | "Jaune" |      25.00       | Gérer les majsucules dans la couleur à chercher |
| ["Rouge", "jaune", "bleu", "bleu"]  | "rouge" |      25.00       |       Gérer les majsucules dans la liste        |
| ["Rouge", "jaUNe", "BLEU", "BLEU"]  | "JAUNE" |      25.00       |          Gérer les majsucules partout           |
| ["a", "b", "c", "c", "c", "c", "c"] |   "c"   |   71.43 (5/7)    |            Vérifier l'arrondissment             |