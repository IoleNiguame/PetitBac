from tkinter import *
import random
import time

animaux = "anaconda Quetzal Zèbre Jaguar Iguane Xérus EléphanT Wapiti Yack Narval Urubu ânesse Koala Serpent Rat Faon Babouin Tortue ÂNE Ours Hibou Kangourou Vipère Dauphin Otarie Vache Girafe Dindon Chat Gorille Renard Guépard Vautour ÉLAN Épagneul Breton Hérisson Unau Lion Baleine Yak Tigre Souris Loutre Anaconda Écureuil gris Chien Autruche Lapin Dinde Abeille Antilope Dromadaire Marmotte Kiwi Mouton Araignée Faucon Poule Raton laveur Panda Furet Hippopotame ÉLÉPHANTEAU épagneule breton Éléphant écureuil épinoche Wallaby Singe Paon Grenouille Escargot Panthère Taupe Loup Biche Léopard Fourmi Mouche Hamster Varan Naja Aigle Dodo Héron Rhinocéros Mangouste Wombat Zébu Jument Mammouth Tapir Daim Ornithorynque Canard Orque Lama Requin Veau Manchot Hiboux marsoin"
list_animaux = animaux.lower().split()
print(list_animaux)

villes = "Îl Istanbul Washington Istanbul Paris Quimper Grenoble Jérusalem Québec Florence Zagreb Xérès Zurich York Marseille Utrech Hambourg Xi'an Nantes Zanzibar Rouen Jakarta Lille Venise Toulouse Eaubonne Lyon Dijon Valence Caen Kaboul Orange Ussel Orléans Ushuaïa Francfort Étables Éden bourg Érode Strasbourg Rome Tours Yaoundé Nice Ulm Dunkerque Oslo Kyoto Istres Madrid étang-salé Épargnes Bruxelles Erevan Rennes Amiens Waterloo Vienne Reims Kiev Amsterdam Bordeaux Grenade Kinshasa Uccle Varsovie Porto Helsinki Hong Kong Yerres Angers Ypres Johannesburg Barcelone Dublin Cannes Orlando Espelette Wellington Édam Écuisses Oran Genève Yalta Ibiza Ermont Ottawa Houston Toronto Kingston Nîmes New York Brest Londres Tunis Nancy Berlin Deauville Indianapolis Fribourg "
list_villes = villes.lower().split()
print(list_villes)

pays = "xi an Qatar Danemark Yémen Hongrie Zimbabwe Venezuela Lituanie Uruguay Roumanie France Jordanie Espagne Kenya Ouganda Estonie Ukraine Finlande Belgique Italie Ouzbékistan Portugal Géorgie Zambie Émirat Arabe émirats arabes unies Turquie Norvège Pologne Kazakhstan Russie Tanzanie Japon Allemagne émirats arabes Nigeria Jamaïque Yougoslavie Canada Irlande Vatican Vietnam Chine Maroc Bulgarie ÉGYPTE Suisse Suède Croatie Colombie Mongolie Inde Tunisie Oman Namibie Grèce Luxembourg Bolivie Albanie Lettonie Groenland Moldavie Honduras Guatemala Népal Watt Autriche Gabon Somalie Serbie Rwanda Hollande Slovaquie Slovénie Thaïlande Algérie Arménie Madagascar Wally et Futuna Koweït Mauritanie Islande Birmanie Argentine Pakistan Soudan Liban Cameroun wallys et Futuna Australie Nicaragua Pérou Brésil Iran Nouvelle Zélande Malaisie Mexique Macédoine Niger Angleterre "
list_pays = pays.lower().split()
print(list_pays)

FL = "Églantines Yuzu Vitelotte Endive Jujube Quetsche Tomate Banane Datte WASABI Salade Haricot usnée Igname Kiwi Orange Ximénia Radis Mangue Fraise Litchi Grenade Navet Laitue Zoé Abricot Carotte Ananas Kaki icaque Goyave Olive Raisin ZESTE zone Xanthium poire Figue Pomme Noix Nectarine Mandarine Zestes de citron Framboise Courgette Groseille Concombre Xio Cerise Durian Haricots Dattes Pastèque patate Salsifí Aubergine Melon Gingembre Fenouil Noix de coco Noisette Prune Betterave Lentille Asperge Haricot vert Endives Papaye Quetsches Topinambour Rutabaga Salsifis Citron Williams rouge Amande Artichaut Avocat Clémentine soja Rhubarbe oignon urbain Pomme de terre Pêche mure Wendy Mâche Tomates Myrtille Marron Courge Poireau Jacquier Pamplemousse Cassis Lentilles Potiron Ugus usnées Urbi "
list_FL = FL.lower().split()
print(list_FL)

objets = "Xylophone Wagon Quille Yoyo Zip îlot centrale Hache îlot de cuisine Urne Nappe Kayak Lampe Ordinateur Jupe imprimante écarteur Jouet Interrupteur Roue Gourde Urinoir Table Montre Enveloppe Livre Râteau Vélo étiquette Oreiller Ustensile Niche Voiture Image Jarre Marteau Kimono Enclume Horloge Sac Armoire Porte eTAGERE Ukulélé Képi Feuille dentier Vase Katana Yacht Arc éthylotest Guitare Zodiac Ampoule Gant Quad Fourchette Entonnoir Yo-Yo Lit Ballon Poutre Dague Nounours Verre flute Loupe Javelot Valise Grenade Vitre Hélicoptère instrument Klaxon Nain de jardin Serviette Zappette Imperméable Balle Journal Kart Chaise Four Règle zeppelin Bouteille Nid Encre Harpe Violon Trousse Arme Doudou Outil ouvre boite boite Fil Disque Aspirateur souris "
list_objets = objets.lower().split()
print(list_objets)

pFeminin = "Zoé Ursula Xavière Wendy Olivia Béatrice Émeline Pauline Tatiana Hélène Éléonore Karine Patricia Julie Yvette Isabelle Géraldine Romane Xenia Valérie Inès élise Iris Nathalie Yvonne Marie Fanny Yasmine Sarah Danielle Valentine Wanda Sophie Nina Barbara Océane Léa Tania Estelle Yolande Elena Noémie eLISA Henriette Gaëlle Juliette Emma Ophélie Camille Victoria Ursule Françoise Fabienne Kelly Irène Rose Laura Jeanne Bernadette Delphine Huguette Rachel Véronique Manon Gabrielle Fiona Lucie Marine Caroline Brigitte Charlotte Nadia Julia Denise Héloïse Alice Yasmina Théa Nicole Diane Justine Kim Tina Amélie Diana Hermione Nadine Lola Viviane Mathilde qualia Oriane Louise Anna Katia Héléna Eva Sylvie Karima Violette "
list_pFeminin = pFeminin.lower().split()
print(list_pFeminin)

pM = "Xavier Quentin Olivier Ulysse Zack William Valentin Eric Victor Paul Nathan Karim Éloi Julien Ugo Zian Ivan Émeric Patrick Damien Nicolas Thomas Hector Théo Yves Romain Hugo Léo Daniel Pierre François Zakaria Vincent David Charles Ursule Fabien Yann Igor Gérard Corentin Oscar Louis Bastien Élias Henri Yanis Antoine Killian Ilan Bernard Yvan Sylvain Walid Samuel Simon Laurent Martin Kylian Baptiste Jules Jean Marc Didier Kilian Harry Fabrice Tom Ethan Gabriel Henry Dorian Mathieu Guillaume Walter Clément Florian Arthur Noé Sébastien Zacharie Benoit Jordan Robert Bob Esteban Zachary Édit Élis élie Éthane Tristan Maurice Cédric Lucas Karl Camille Willy Grégoire Ian Titouan "
list_pM = pM.lower().split()
print(list_pM)

lettres = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
lettre = random.choice(lettres)

root = Tk()
root.title('Petit Bac')
root.configure(bg="#ff8c8f")
root.resizable(0, 0)

label_lettre = Label(root, text="Le lettre est \"%s\"" % lettre.upper(), font=('Arial', 35), bg="#ff8c8f")
label_lettre.pack(side=TOP)


    



frame1 = Frame(root)
frame1.pack(side=TOP)
frame2 = Frame(root)
frame2.pack(side=TOP)
frame3 = Frame(root)
frame3.pack(side=TOP)
frame4 = Frame(root)
frame4.pack(side=TOP)

correct = 0
incorrect = 0

class Categorie:
    def __init__(self, categorie, label, side, frame):
        self.categorie = categorie
        self.frame = Frame(frame, relief=RAISED, bg="#ff8c8f")
        self.frame.pack(side=side, padx=10, pady=10)
        self.label = Label(self.frame, text=label, font=('Arial', 25), bg="#ff8c8f")
        self.label.pack(side=TOP)
        self.entry = Entry(self.frame, font=('Arial', 25), justify=CENTER)
        self.entry.pack(side=RIGHT, padx=5, pady=5)
        self.liste = categorie
    
    def verification(self):
        global correct
        #self.entry.insert(0, ' ')
        self.tentative = self.entry.get().lower()
        if self.tentative:
            if self.tentative[0] == lettre:
                if self.tentative.lower() in self.liste:
                    self.entry.configure(state=DISABLED)
                    self.frame.configure(bg="green")
                    self.label.configure(bg="green")
                    correct += 1
                else:
                    self.entry.configure(state=DISABLED)
                    self.frame.configure(bg="red")
                    self.label.configure(bg="red")
                    print("Le mot n'est pas dans la liste", self.tentative)
                
            else:
                self.entry.configure(state=DISABLED)
                self.frame.configure(bg="red")
                self.label.configure(bg="red")
                print('Ce n\'est pas la bonne lettre', self.tentative)
        
        else:
                self.entry.configure(state=DISABLED)
                self.frame.configure(bg="red")
                self.label.configure(bg="red")
                print("Il n'y a rien ecrit")
      
C_animaux = Categorie(list_animaux, "Animaux", LEFT, frame1)
C_villes = Categorie(list_villes, 'Villes', RIGHT, frame1)
C_pays = Categorie(list_pays, 'Pays', LEFT, frame2)
C_FL = Categorie(list_FL, 'Fruits/Legumes', RIGHT, frame2)
C_pFeminin = Categorie(list_pFeminin, 'Prenoms Feminins', LEFT, frame3)
C_pM = Categorie(list_pM, 'Prenoms Masculins', RIGHT, frame3)
C_objets = Categorie(list_objets, 'Objets', TOP, frame4)


def verifier():
    C_animaux.verification()
    C_villes.verification()
    C_pays.verification()
    C_FL.verification()
    C_pFeminin.verification()
    C_pM.verification()
    C_objets.verification()
    if correct == 7:
        root.configure(bg="green")
        label_lettre.configure(bg="green")
        rootG = Tk()
        labelG = Label(rootG, text="Victoire", font=('Arial', 100), bg="green")
        labelG.pack()
        rootG.mainloop()
    else:
        root.configure(bg="red")
        label_lettre.configure(bg="red")
        rootG = Tk()
        labelG = Label(rootG, text="Defaite", font=('Arial', 100), bg="red")
        labelG.pack()
        rootG.mainloop()

root.after(300000,  verifier)

btn = Button(root, text="Valider", font=('Arial', 30), bg='green', relief=RAISED, command=verifier)
btn.pack(side=BOTTOM, fill=X)




root.mainloop()


        