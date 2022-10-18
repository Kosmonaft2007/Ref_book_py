import sys

import user_interface.interface as us_if
import model.user_input as inp
import model.contact_actions_handler as cah
import model.import_contacts as imp
import model.export_contacts as exp


def run(path):
    print('=' * 50)
    print('Добро пожаловать в наш телефонный справочник')
    us_if.main_menu()
    i = inp.choice_menu_input(4)
    while(True):

        if i == 1:
            us_if.contact_handler()
            i = inp.choice_menu_input(3)
            if i == 1:
                print('-' * 50)
                print('Вы выбрали "Создать контакт"')
                print('-' * 50)

                cc_list = cah.create_contact()
                print('=' * 60)
                print('||', cc_list[0].center(15), '||', cc_list[1].center(15), '||', cc_list[2].center(15), '||')
                print('=' * 60)
                imp.import_to_csv(cc_list, path, 'a')
                print(exp.show_all_contacts(path))
            elif i == 2:
                print('-' * 50)
                print('Вы выбрали "Удалить контакт"')
                print('-' * 50)
                cah.delete_contact(path)
            elif i == 3:
                print('-' * 50)
                print("Программа завершила работу")
                print('-' * 50)
                sys.exit()

        elif i == 2:
            us_if.export_menu()
            i = inp.choice_menu_input(3)
            if i == 1:
                print('-' * 50)
                print('Вы выбрали "Вывод всех данных"')
                print('-' * 50)
                exp.show_all_contacts(path)
            elif i == 2:
                print('-' * 50)
                print('Вы выбрали "Вывод информации о контакте"')
                print('-' * 50)
                exp.show_selected_contact(path)
            elif i == 3:
                print('-' * 50)
                print("Программа завершила работу")
                print('-' * 50)
                sys.exit()

        elif i == 3:
            i = inp.choice_menu_input()


        # match i:
        #     case 1:
        #         console.Interface("Contact_action")
        #         i = ex.digit()
        #         if i == 1:#create
        #             print('-'*50)
        #             print('Вы выбрали "Создать контакт"')
        #             print('-'*50)
        #             ls = cah.create_contact()
        #             print(ls)
        #             imp.import_csv(ls, path, 'a')
        #             print(exp.show_all_contacts(path))
        #         elif i == 2: #delete
        #             print('-'*50)
        #             print('Вы выбрали "Удалить контакт"')
        #             print('-'*50)
        #             cah.delete_contact(path)
        #         elif i == 3:
        #             print('-'*50)
        #             print("Программа завершила работу")
        #             print('-'*50)
        #             break
        #         else:
        #             print('-'*50)
        #             print("Вы ввели неправильные данные")
        #             print('-'*50)
        #
        #
        #
        #     case 2:
        #         console.Interface("Export")
        #         i = ex.digit()
        #         if i == 1:
        #             print('-'*50)
        #             print('Вы выбрали "Вывод всех данных"')
        #             print('-'*50)
        #             exp.show_all_contacts(path)
        #         elif i == 2:
        #             print('-'*50)
        #             print('Вы выбрали "Вывод информации о контакте по указанным фамилии и имени"')
        #             print('-'*50)
        #             exp.show_selected_contact(path)
        #         elif i == 3:
        #             print('-'*50)
        #             print("Программа завершила работу")
        #             print('-'*50)
        #             break
        #         else:
        #             print('-'*50)
        #             print("Вы ввели неправильные данные")
        #             print('-'*50)
        #
        #
        #     case 3:
        #         data =input('Так я не поняла как это работает')
        #         imp.import_csv(data,path,'a')
        #
        #     case 4:
        #         print('-'*50)
        #         print("Программа завершила работу")
        #         print('-'*50)
        #         break
        #     case _:
        #         print('-'*50)
        #         print("Нет данных")