# class UnderAgeError(Exception):
#     pass
# class InvalidAgeError(Exception):
#     pass


# class AgeVerification:

#     def set_age(self,age):
#         try:
#             if age < 0:
#                 raise ValueError('please enter a valid number') 
#             elif age < 18:
#                 raise UnderAgeError('Under Age error')
#             elif age > 100:
#                 raise InvalidAgeError('Invalid Age Error')

#             else:
#                 print('Valid Age')
            
#         except Exception as err:
#             print(f'error occured as {err}')

#         finally:
#             print('age verification completer')

# A = AgeVerification()
# A.set_age(5)



# 2 problem

class LoginSystem:
    __password = 'python@123'
    __attempts = 3
    
    def Login(self,password):
        try:
            if password != self.__password:
                self.__attempts -= 1
                print(f'Please enter correct password, "remaining_attempts": {self.__attempts}')

            elif self.__attemtps < 0:
                raise ValueError('Account is locked')
            
            elif password == self.__password:
                print('login successful')
            
        except Exception as e:
            print(f'account is locked as no attempt left')

l = LoginSystem()
l.Login('password')
l.Login('password')
l.Login('password')
l.Login('password')









    