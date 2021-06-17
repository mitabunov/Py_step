from model import ReceptBase
from view import UserInterface

class Controller:
    def __init__(self) -> None:
        self.recepten_base = ReceptBase()
        self.user_interface = UserInterface()

    def arbeit(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_man_answer(answer)

    def check_man_answer(self, answer):
        if answer == '1':
            self.add_recept()
        elif answer == '2':
            self.remove_recept()    
        elif answer == '3':
            self.show_recept()
        elif answer =='4':
            self.show_all_recepten()    
        else:
            print('Нет такой команды')   


    def add_recept(self):
        recept = self.user_interface.add_man_recept()
        self.recepten_base.add_recept(*recept.values())
    
    def show_recept(self):
        user_recept = self.user_interface.get_user_recept()
        recept = self.recepten_base.get_recept_by_name(user_recept)
        self.user_interface.show_user_recept(recept)

    def remove_recept(self):
        user_recept = self.user_interface.get_user_recept()
        self.recepten_base.delet_recept(user_recept) 

    def show_all_recepten(self):
        recepten = self.recepten_base.get_all_recepten()
        self.user_interface.user_show_all_recepten(recepten)
