import controller
import vue
import model
from datetime import datetime, date

class TestController(controller.Controller):

    def __init__(self):
        """Initialise les modèles et les vues."""
        self.state = model.State()
        self.vue = TestVue()

    def test_creer_nouveau_tournoi(self):
        nouveau_tournoi = model.Tournoi(nom='Tournoi_TEST',
                                        lieu = 'lieu_test',
                                        date_debut=datetime.today(),
                                        date_fin= datetime.today(),
                                        controle_du_temps = model.ControleDuTemps.BLITZ,
                                        description = 'Remarques',
                                        rounds = [],
                                        )
        self.state.creer_nouveau_tournoi(nouveau_tournoi)

    def test_ajouter_joueurs(self, nombre_joueur: int):
        joueurs = self.vue.test_ajouter_joueurs(nombre_joueur)
        self.state.ajouter_joueurs(joueurs)

class TestVue(vue.Vue):

    def test_ajouter_joueurs(self, nombre_joueur: int):
        joueurs = []
        for i in range(1, nombre_joueur + 1):
            joueurs.append(model.Joueur(nom_de_famille='Nom de Famille Joueur '+ str(i),
                                  prenom = 'Prenom Joueur ' + str(i),
                                  date_de_naissance = date.today(),
                                  sexe =  model.Sex.MALE,
                                  classement = i * 13
                                ))
        return joueurs


if __name__ == '__main__':

    init_controller = TestController()
    init_controller.test_creer_nouveau_tournoi()
    init_controller.test_ajouter_joueurs(nombre_joueur=4)
    init_controller.creer_nouveau_round()
    init_controller.generer_paires_joueurs()
    init_controller.entrer_scores()
    print(init_controller.state.actual_round.match_liste)
