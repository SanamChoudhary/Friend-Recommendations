from network import network

def suggestFriends(name):
    allPeople = []
    for person in network:
        if person not in allPeople:
            allPeople.append(person)

    currentPerson = ""
    for person in allPeople:
        if name == person:
            currentPerson = person
            break





name = input("Enter a name to suggest friends for: ")
suggestFriends(name)

