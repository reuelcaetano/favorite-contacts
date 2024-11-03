menu = """
Menu do Gerenciador de Contatos:
1. Adicionar um contato
2. Listar contatos
3. Listar contatos favoritos
4. Editar um contato
5. Favoritar um contato
6. Desfavoritar um contato
7. Remover um contato
8. Sair
Digite sua escolha: 
"""

contacts = {}
index = 0

def listContacts(favorite=False):
  print('== AGENDA DE CONTATOS ==')
  for key, contact in contacts.items():
    mark = 'x' if contact['favorite'] == True else ''
    if favorite and mark:
      print(f'{key}. [{mark}] - nome: {contact['name']}, telefone: {contact['phone']}, email: {contact['email']}, ')
    elif not favorite:
      print(f'{key}. [{mark}] - nome: {contact['name']}, telefone: {contact['phone']}, email: {contact['email']}, ')

def addContact(name, phone, email):
  contacts[index] = {
    'name': name,
    'phone': phone,
    'email': email,
    'favorite': False,
  }
  print(f'O contato [{name}] foi adicionado com sucesso!')

def favoriteContact(contactId):
  contacts[contactId]['favorite'] = True

def unfavoriteContact(contactId):
  contacts[contactId]['favorite'] = False

def updateContact(contactId, name, phone, email):
  contacts[contactId]['name'] = name
  contacts[contactId]['phone'] = phone
  contacts[contactId]['email'] = email

def removeContact(contactId):
  contact = contacts[contactId]
  contacts.pop(contactId)
  print(f'O contato [{contact['name']}] foi removido com sucesso!')

while True:
  cmd = int(input(menu))
  
  if cmd == 1:
    name = input('Digite o nome: ')
    phone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    index = index + 1
    addContact(name, phone, email)
  
  if cmd == 2:
    listContacts()
  
  if cmd == 3:
    listContacts(favorite=True)
  
  if cmd == 4:
    contactId = int(input('Digite o id do contato: '))
    name = input('Digite o novo nome do contato: ')
    phone = input('Digite o novo telefone do contato: ')
    email = input('Digite o novo email do contato: ')
    updateContact(contactId, name, phone, email)
  
  if cmd == 5:
    contactId = int(input('Digite o id do contato: '))
    favoriteContact(contactId)
  
  if cmd == 6:
    contactId = int(input('Digite o id do contato: '))
    unfavoriteContact(contactId)
  
  if cmd == 7:
    contactId = int(input('Digite o id do contato: '))
    removeContact(contactId)
  
  if cmd == 8:
    break