# Addinfo and Delinfo.py
#
# It can not only add, delete, rename people in our contacts, but also show, add and delete infomation
#
# Author: Jinbiao Liao, 1C , A01057463


def get_cmd():
    command = input("Enter a command: ")
    command = command.split(' ')
    cmd = command[0]
    name = command[1:]
    name = ''.join(name)
    return cmd,name


def add_contact(name):  
    contacts[name] = {}
def delete_contacts(name):
    del contacts[name] 
def rename_contacts(name):
    number_str = contacts[name]
    del contacts[name]
    name = input('Enter a new name for %s: ' %name)
    contacts[name] = number_str
def addinfo_contacts(name):
    addinfo = input('Enter contact info for %s: ' %name)
    addinfo = addinfo.split(':')
    key = addinfo[0] 
    value = addinfo[1]
    contacts[name][key] = value
def delinfo_contacts(name):
    key = input('Enter type of contact info to delete: ')
    del contacts[name][key]

    
if __name__ == "__main__":
    contacts = {}
    cmd,name = get_cmd()
    while cmd != 'quit':

        if cmd == 'add':
            add_contact(name)
        if cmd == "delete":
            delete_contacts(name)
        if cmd == 'rename':
            rename_contacts(name)
        if cmd == 'show':
            print(contacts)
        if cmd == 'info':
            print('%s:' %name,contacts[name])
        if cmd == 'addinfo':
            addinfo_contacts(name)
        if cmd == 'delinfo':
            delinfo_contacts(name)
        cmd, name = get_cmd()
    exit()



