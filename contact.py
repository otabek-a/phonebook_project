class Contact:
   def __init__(self,first_name:str,last_name:str,phone_number:str):
      self.first_name=first_name
      self.last_name=last_name
      self.phone_number=phone_number
   def check_name(self):
      if self.first_name[0].isupper() and self.last_name[0].isupper():
         return True
      return False
   def check_phone_number(self,name=False):
      self.name=name

      indeks=len('+998 93 123 45 67')
      if len(self.name)==indeks:
         return True
      return False
   


      
      


