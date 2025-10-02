import pytest
from fctListes import fonction1, fonction2, moyenne_par_couleur




# Arrange
@pytest.mark.parametrize("liste_lego, resultat_attendu", [
    (["rouge", "bleu", "jaune"], 1.00),
    (["rouge", "rouge", "bleu", "bleu", "jaune", "jaune"], 2.00),
    ([], 0.00),
    (["rouge", "bleu", "jaune", "jaune"], 1.33),
])
# Act
def test_fonction3(liste_lego, resultat_attendu):
    resultat_obtenu = moyenne_par_couleur(liste_lego)

    # Assert
    assert type(resultat_obtenu) == float
    assert resultat_attendu == resultat_obtenu