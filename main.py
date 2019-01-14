# parse sys arg for client, article and amount
import os
import io
import sys, getopt
from configparser import SafeConfigParser
from pyexcel_ods import get_data
import json

def addInvoice():
    print('')
    userdata=list(get_data('data/users.ods').values())[0]
    #print(userdata)
    users = [item[7] for item in userdata]
    for i, user in enumerate(users):
        print(i,' ', user)
    user = int(input('User:\n'))
    clientdata=list(get_data('data/clients.ods').values())[0]
    clients = [item[1] for item in clientdata]
    for i, client in enumerate(clients):
        print(i,' ',client)
    client = int(input('Client:\n'))
    articledata = list(get_data('data/articles.ods').values())[0]
    articles = [article[1] for article in articledata]
    for i, article in enumerate(articles):
        print(i, ' ', article)
    article = int(input('Article:\n'))
    amount = int(input('Amount:\n'))
    print("\nINVOICE DATA:\n", 'User: ', users[user],  '\nClient: ', clients[client], '\nArticle: ', articles[article], '\nAmount: ', amount, '\nCreate Invoice?\n[Y]es, [n]o')
    #print(json.dumps(userdata))
    #users = userdata[1:]
    #print users
    #user=input('User:')
    #print client list
    #client=input('Client:')

def help_me():
    f = open('README.md', 'r')
    f_content = f.read()
    print(f_content)
    f.close

try:
    opts, args = getopt.getopt(sys.argv[1:], 'u:c', ['u=', 'c='])
except getopt.GetoptError:
    print('Error: invalid argument')
    help_me()
    sys.exit(2)
exit = False
while(exit == False):
    choice = input('\n1 Create invoice\n2 See business data\n0 Exit\n')
    if choice == '1':
        addInvoice()
    elif choice == '2':
        print('NOT IMPLEMENTED YET')
    elif choice == '0':
        print('exiting..')
        exit = True
    else:
        print('Invalid input!')


