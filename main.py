from network import network

def suggestFriends(name):
   
    #Goes to network dict and returns the list of friends that "name" has
    relationship = network[name]

    #list of recommended friends
    recommendedFriends = []

    #Iterates through every name the relationships that "Name" has
    for relation in relationship:
        nameRelationships = network[relation]
        nameRelationships.remove(name)
        for friend in nameRelationships:
            recommendedFriends.append(friend)
    
    recommendedFriends = set(recommendedFriends)
    recommendedFriends = list(recommendedFriends)
    
    print("Suggested friends for " + name + ":")
    for person in recommendedFriends:
        print(person)
        
name = input("Enter a name to suggest friends for: ")
suggestFriends(name)

