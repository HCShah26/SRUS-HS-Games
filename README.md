# SRUS-HS-Games
## Double Linked List Implementation
This project demonstrates the implementation of a Double Linked List in Python. This version is based on a Player Linked List that has a header and tail node. 

The **PlayerList** stores a list **PlayerNodes** which all have next and a previous reference point to the other nodes in the list. This helps to track all the nodes in the list.

The **PlayerNode** stores the **Player** data (Unique Identifier and Name)

###Player
The **Player** class has an initialiser method and two getters and a print method

###PlayeNode
The **PlayerNode** has an initialise method and the getters and setters methods and also a print method to display the contents of a node

###PLayerList
The **PlayerList** has the following methods

**initaliser** to set up an empty PlayerList

**is_empty** to check if the list is empty

**insert_at_head** to insert a new player to the top of the list

**insert_at_tail** to insert a new player to the bottom of the list

**delete_from_the_head** to delete the top most player from the list

**delete_from_the_tail** to delete the last player from the list

**delete_by_key** to delete a specific player node

**search_by_key** to find a player node by Key (UID) value

**search_by_name** to find a player node by player name

**find** to find player node by taking Player object and searchByKey: bool, and will call either **search_by_key** or **search_by_name**

**__iter__** method to iterate through the PlayerList moving forward from the Head to the Tail

**__reversed__** method to iterate through the PlayerList moving in reverse from the Tail to the Head

**__len__** method to return the size of the PlayerList, this method has been optimised 
        by adding a property "size" in the PlayerList that keeps track of inserts and deletes as they happen. 
        By doing so we same a call to iterate through the entire list to get the lenght of the PlayerList.
        As the list grows in size and starts to hold a large number of players, we can possibly get a delay 
        had we used the method to iterate throught the entire list to get it's length
