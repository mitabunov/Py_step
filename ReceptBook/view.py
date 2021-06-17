class UserInterface:
    def wait_user_answer(self):
        print('Ввод пользователя'.center(60,'$'))
        print('Что сделать?')
        print('Вы хотите:'
            '\n1 -Добавить рецепт? '
            '\n2- Удалить рецепт '
            '\n3- Посмотреть конкретный рецепт '
            '\n4- Посмотреть все рецепты '
            '\nq - Выйти из программы ')
        user_answer = input('Выберите действие: ')
        print('-'*60)
        return user_answer

    def add_man_recept(self):
        dict_recept = {
            'название рецепта':None,
            'автор рецепта':None,
            'тип рецепта':None,
            'текстовое описание рецепта':None,
            'список ингредиентов':None,
            'название кухни':None
        }
        # print('Добавление рецепта'.center('*' * 60))
        for key in dict_recept:
            dict_recept[key] = input(f'Введите {key} рецепта')
        # print('*' * 60)
        return dict_recept

    def get_user_recept(self):
        user_recept = input('Название рецепта: ')
        return user_recept
 
    def show_user_recept(self, recept):
        print('О рецепте')
        for key in recept:
            print(f'{key} рецепта: \n{recept[key]}')

    def user_show_all_recepten(self, recepten):
        print('Все рецепты')  
        for recept in recepten:
            print(recept)      