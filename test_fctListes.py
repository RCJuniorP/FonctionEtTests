import pytest
from fctListes import fonction1, fonction2, moyenne_par_couleur




# Arrange
@pytest.mark.parametrize("liste_lego, resultat_attendu", [
    (["rouge", "bleu", "jaune"], 1.00),
    (["rouge", "rouge", "bleu", "bleu", "jaune", "jaune"], 2.00),
    ([], 0.00), # Les listes vides devraient retourner 0
    (["rouge", "bleu", "jaune", "jaune"], 1.33),  # On doit arrondir à deux chiffres
    (["rouge", "rouge", "bleu", "bleu", "JAUNE", "jaune"], 2.00),  # Les majuscules devraient être ignorées
    (["rouge", "bleu", "vert", "vert", "jaune", "jaune"], 1.50),
])
# Act
def test_fonction3(liste_lego, resultat_attendu):
    resultat_obtenu = moyenne_par_couleur(liste_lego)

    # Assert
    assert isinstance(resultat_obtenu, float)
    assert resultat_attendu == resultat_obtenu
