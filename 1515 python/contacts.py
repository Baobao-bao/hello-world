# contacts.py
#
# [replace this line with a description of what your program does]
#
# Author: Jinbiao Liao, 1C , A01057463
#

def get_cmd():
    command = input("Enter a command: ")
    command = command.split(' ')
    cmd = command[0]
    name = command[1:]
    name = ''.join(name)
    print(cmd, name)  #remember to delete it
    return cmd,name


def add_contact(name):  ### replace this with your function, and put other functions below
    contacts[name] = input('Enter the phone number: ')
def delete_contacts(name):
    del contacts[name]   #contacts.pop(name,None)
def rename_contacts(name):
    pass

if __name__ == "__main__":
    contacts = {}
    cmd,name = get_cmd()
    while cmd != 'quit':

        if cmd == 'add':  ### update this so that it runs your function
            add_contact(name)
        if cmd == "delete":
            delete_contacts(name)
        if cmd == 'rename':
            rename_contacts(name)
        if cmd == 'show':
            print(contacts)

        cmd, name = get_cmd()

    exit()

# a = [1,3,'5']

# a[2] = '3'
# print(a)
# print(a.index(3))

# dict = {"bob":"3728"}
# print(dict)


