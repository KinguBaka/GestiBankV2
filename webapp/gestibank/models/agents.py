from webapp import db
from webapp.gestibank.models.user import User

#Classe Agent  héritant du compte User et contenant les methodes:
#Valider et cree  les demande de creation de compte,filtrer les demandes d'ouvertures de comptes,
#Configurer et modifier les comptes client, effectuer des recherche aves et sans filtres sur les compte client,
#Afficher les opperation d'un client sur les 12 derniers mois,valider les demande de chequier et les facilité de caisses
class Agent(User):
    __tablename__ = 'agent'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    debut_contrat = db.Column(db.Date)
    # client = db.relationship('Clients', backref='client', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'agent',
    }



    # def flitre_compte(self):  # Retourne les demande de création de compte avec le id agent
    #     return self.query.filter_by(self.id)
    #
    # def validation_Crea(self, objet_demandecrea, valid_crea: bool):  # Validation création d'ouverture de compte
    #     objet_demandecrea.validation(valid_crea)
    #     if objet_demandecrea.valide is True:  # Si la demande est validé, création du compte, envoi un mail avec login/mdp + mis en True
    #         # TODO envoi de mail avec id/mdp
    #         # TODO création de compte banquaire
    #         objet_demandecrea.creation_compte_User()
    #     elif objet_demandecrea.valide is False:  # Si la demande n'est pas valider = envoi de mail demande info + mis en False
    #         pass  # TODO envoi de mail avec une demande d'info supplementaire
    #     else:  # Erreur
    #         print("Erreur/En attente")
    #
    # """
    #
    #     def modif_compte_User(self):  # Modification compte client
    #         pass
    #
    #     def valid_cheque(self):  # Validation demande chéquier
    #         pass
    #
    #     def valid_facilite(self):  # Validation facilité de caisse
    #         pass
    # """