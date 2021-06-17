class Recept:
    def __init__(self, name, author, type_rec, esse_rec, list_ingred,_kuchen_name):
        self.name = name
        self.author = author
        self.type_rec = type_rec
        self.esse_rec = esse_rec
        self.list_ingred = list_ingred
        self.kuchen_name = _kuchen_name

    def __repr__(self):
        return f'{self.author}."{self.name}"'


class ReceptBase:
    def __init__(self):
        self.recepten = {}

    def add_recept(self,name, author, type_rec, esse_rec, list_ingred,_kuchen_name):
        recept = Recept(name, author, type_rec, esse_rec, list_ingred,_kuchen_name)
        self.recepten[name] = recept

    def delet_recept(self, name):
        try:
            self.recepten.pop(name)
        except KeyError:
            print('Такого рецепта нет')    

    def get_recept_by_name(self, name):
        recept = self.recepten[name] 
        recept_dict = {
            'название рецепта':recept.name,
            'автор рецепта':recept.author,
            'тип рецепта':recept.type_rec,
            'текстовое описание рецепта':recept.esse_rec,
            'список ингредиентов':recept.list_ingred,
            'название кухни':recept.kuchen_name
        }
        return recept_dict 

    def get_all_recepten(self):
        return self.recepten.values()
