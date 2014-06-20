import pickle 
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('command', help='What do you want to do with the phonebook?')
parser.add_argument('args', nargs='*')

args = vars(parser.parse_args())


class Phonebook:
    def __init__(self, _original, _reversed):
        self.original = _original
        self.reversed = _reversed


def create(phonebook_name):
    empty_phonebook = Phonebook({}, {})
    dump(phonebook_name, empty_phonebook)

    return "%s has been created." %(phonebook_name)

def add(person, number, phonebook_name):
    phonebook = load(phonebook_name)
    # now phonebook is just a regular dictionary

    first = person.split()[0]

    return_msg = ""

    # update original phonebook
    if first in phonebook.original:
        if person in phonebook.original[first]:
            return_msg = "%s is already in the phonebook." %(person)
        else:
            phonebook.original[first][person] = number
            return_msg = "%s has been added to the phonebook." %(person)

    else:
        phonebook.original[first] = {person: number}
        return_msg = "%s has been added to the phonebook." %(person)

    phonebook.reversed[number] = person

    # dump hashtable back into pickle file
    dump(phonebook_name, phonebook)

    return return_msg

def lookup(person, phonebook_name):
    # we now have first and last name

    return_msg = ""

    first = person.split()[0]
    phonebook = load(phonebook_name)

    if first in phonebook.original:
        persons = phonebook.original[first]

        if person in persons:
            return_msg = "%s %s" %(person, persons[person])

        else:
            people = ""
            for someone in persons:
                people += "%s %s\n" %(someone, persons[someone])

            return_msg = people

    else:
        return_msg = "%s could not be found." %(person)

    return return_msg

def change(person, new_num, phonebook_name):
    first = person.split()[0]
    phonebook = load(phonebook_name)

    return_msg = ""

    if first in phonebook.original:
        persons = phonebook.original[first]

        if person in persons:
            persons[person] = new_num

            return_msg = "%s %s" %(person, persons[person])

        else:
            return_msg = "Nothing to change."

    else: 
        return_msg = "Nothing to change."

    dump(phonebook_name, phonebook)
    return return_msg

def remove(person, phonebook_name):
    first = person.split()[0]
    return_msg = ""
    phonebook = load(phonebook_name)
    if first in phonebook.original:
        persons = phonebook.original[first]

        if person in persons:
            del persons[person]
            return_msg = "Removed %s from the phonebook." %(person)

        else: 
            return_msg = "Can't remove someone that doesn't exist."

    else: 
        return_msg = "Can't remove someone that doesn't exist."

    dump(phonebook_name, phonebook)

    return return_msg

def reverse_lookup(number, phonebook_name):
    phonebook = load(phonebook_name)
    return_msg = ""

    if number in phonebook.reversed:
        return_msg = "%s %s" %(phonebook.reversed[number], number)

    else:
        return_msg = "%s could not be found" %(number)

    return return_msg

def load(filename):
    with open(filename, "rb") as f:
            try:
                phonebook = pickle.load(f)
                return phonebook
            except:
                return "Loading %s failed. No such phonebook." %(filename)


def dump(filename, hashtable):
        try:
            with open(filename, "wb") as f:
                pickle.dump(hashtable, f)
    
        except:
            return "Saving to %s failed." %(filename)


if __name__ == "__main__":
    command = args['command']
    rest = args['args']

    if command == "create":
        print create(rest[0])

    elif command == "add":
        print add(rest[0], rest[1], rest[2])

    elif command == "lookup":
        print lookup(rest[0], rest[1])

    elif command == "change":
        print change(rest[0], rest[1], rest[2])

    elif command == "remove":
        print remove(rest[0], rest[1])

    elif command == "reverse-lookup":
        print reverse_lookup(rest[0], rest[1])
