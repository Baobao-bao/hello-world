# contacts.py
#
# Create and manage a list of contacts. This version of the program includes
# code for Week 3 Lab Exercise 3: addinfo and delinfo.
#
# Author: Rob Neilson
#

def get_cmd():
    user_input = input("Enter a command: ")
    input_list = user_input.split()
    command = input_list[0]
    args = input_list[1:]
    return command, args


def add_contact(arg_list):
    new_contact = " ".join(arg_list)
    info = {}
    _contacts[new_contact] = info


def show_contacts():
    print(_contacts)


def delete_contact(arg_list):
    contact_to_delete = " ".join(arg_list)
    del (_contacts[contact_to_delete])


def rename_contact(arg_list):
    contact_to_rename = " ".join(arg_list)
    new_name = input("Enter a new name for " + contact_to_rename + ": ")
    info = _contacts[contact_to_rename]
    _contacts[new_name] = info
    delete_contact(arg_list)


def show_info(arg_list):
    contact_to_display = " ".join(arg_list)
    info = _contacts[contact_to_display]
    print("%s: %s" % (contact_to_display, info))


def add_info(arg_list):
    contact_name = " ".join(arg_list)
    info = _contacts[contact_name]
    user_input = input("Enter contact info for " + contact_name + ": ")
    info_type, info_value = user_input.split(':')
    info[info_type] = info_value
    _contacts[contact_name] = info


def delete_info(arg_list):
    contact_name = " ".join(arg_list)
    info = _contacts[contact_name]
    contact_type = input("Enter type of contact info to delete: ")
    del (info[contact_type])


if __name__ == "__main__":

    _contacts = {}
    cmd, args = get_cmd()
    while cmd != 'quit':

        if cmd == 'add':
            add_contact(args)
        if cmd == 'show':
            show_contacts()
        if cmd == 'delete':
            delete_contact(args)
        if cmd == 'rename':
            rename_contact(args)
        if cmd == 'info':
            show_info(args)
        if cmd == 'addinfo':
            add_info(args)
        if cmd == 'delinfo':
            delete_info(args)

        cmd, args = get_cmd()

    exit()
