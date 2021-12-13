_list = []

class Users:


     def __init__(self, user_name, last_name, age, city):
          self.user_name = user_name
          self.last_name = last_name
          self.age = age
          self.city = city

     def get_info(self):

          return{
               'user_name': self.user_name,
               'last_name': self.last_name,
               'age': self.age,
               'city': self.city,
          }

     def change_name(self, new_name):
          self.user_name = new_name

     def change_by_key_field(self, field_name, new_value):

          if getattr(self, field_name):
               setattr(self, field_name, new_value)





user_1 = Users('vasya', 'ivanov', 33, 'kyiv')
user_2 = Users(user_name='aaa')
print(user_1.last_name)

print(getattr(user_1, 'last_name'))
user_1.get_info()
user_1.change_name('ivan')

_list.append(user_1)


for index, user in enumerate(_list):
     print(user.get_info())
     user.change_by_key_field('user_name', user.user_name + str(index))
     print(user.get_info())