from openpyxl import load_workbook
from openpyxl import Workbook



class Manager_API_Users:
     def __init__(self, name, last_name, city, age):
         self.name = name
         self.last_name = last_name
         self.city = city
         self.age = age

     def get_user_information(self):
          return {
               'name': self.name,
               'last_name': self.last_name,
               'city': self.city,
               'age': self.age
          }

     def add_user(self):
          pass

     def charge_user_information(self):
          pass

     def delete_user():
          pass

     def search_user():
          pass

     # def save_in_xlsx(self, key, value):
     #      wb = Workbook()
     #      sheet = wb.active

     #      sheet['A1'] = 'name'
     #      sheet['B1'] = 'last name'
     #      sheet['C1'] = 'city'
     #      sheet['D1'] = 'age'

     #      for row, (key, value) in enumerate(dict_users.items(), start=2):
     #           print(value)
     #           sheet[f'A{row}'] = value
     #           sheet[f'B{row}'] = value
     #           sheet[f'C{row}'] = value
     #           sheet[f'D{row}'] = value

     #      wb.save('dict_users.xlsx')
     #      wb.close()

first_user = Manager_API_Users('vasya', 'ivanov', 'kyiv', 33)
q = first_user.get_user_information()
print(q)

# w = first_user.add_user('ivan', 'krone', 'lviv', 22)
# print(w)

first_user.charge_user_information()

# first_user.save_in_xlsx('key', 'value')
