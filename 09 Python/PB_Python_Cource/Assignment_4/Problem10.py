#Q.Mini Project - OOP's Chat System
#Let's create a Chat System using OOPs concepts. We have to create classes:
#User
#Message
#ChatRoom

#And we have to implement function:
#sending messages   
#viewing chat history
#user joining and leaving the Chatroom

import datetime

# 1. The Message Class
# Represents a single message containing the sender, content, and time.
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        # Adding a timestamp for realism
        self.timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        # Defines how the message looks when printed
        return f"[{self.timestamp}] {self.sender.name}: {self.content}"


# 2. The ChatRoom Class
# Manages users and the message history.
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.active_users = []  # List to track who is currently in the room
        self.message_history = []  # List to store Message objects

    def join(self, user):
        """Allows a user to join the room."""
        self.active_users.append(user)
        print(f"--> {user.name} has joined '{self.room_name}'.")

    def leave(self, user):
        """Allows a user to leave the room."""
        if user in self.active_users:
            self.active_users.remove(user)
            print(f"<-- {user.name} has left '{self.room_name}'.")
        else:
            print(f"{user.name} is not in this room.")

    def receive_message(self, user, content):
        """Receives a message from a user and stores it."""
        if user in self.active_users:
            new_message = Message(user, content)
            self.message_history.append(new_message)
        else:
            print(f"Error: {user.name} cannot send a message. They are not in the room.")

    def show_history(self):
        """Prints the entire chat history."""
        print(f"\n--- Chat History for {self.room_name} ---")
        if not self.message_history:
            print("No messages yet.")
        else:
            for msg in self.message_history:
                print(msg)
        print("---------------------------------------")


# 3. The User Class
# Represents a participant in the system.
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chat_room, content):
        """User triggers the chatroom to receive their message."""
        chat_room.receive_message(self, content)


# --- MAIN EXECUTION (Testing the Project) ---

if __name__ == "__main__":
    # 1. Create the ChatRoom
    general_chat = ChatRoom("General Discussion")

    # 2. Create Users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    print("--- STARTING CHAT SYSTEM ---")

    # 3. Users join the room
    general_chat.join(alice)
    general_chat.join(bob)

    # 4. Sending messages
    alice.send_message(general_chat, "Hello everyone!")
    bob.send_message(general_chat, "Hey Alice, good to see you.")

    # 5. User joining later
    general_chat.join(charlie)
    charlie.send_message(general_chat, "Am I late to the party?")
    
    # 6. User leaving
    general_chat.leave(alice)
    
    # 7. Alice tries to send a message after leaving (Should fail)
    alice.send_message(general_chat, "I forgot to say bye!") 

    # 8. View Chat History
    general_chat.show_history()

#     --- STARTING CHAT SYSTEM ---
# --> Alice has joined 'General Discussion'.
# --> Bob has joined 'General Discussion'.
# --> Charlie has joined 'General Discussion'.
# <-- Alice has left 'General Discussion'.
# Error: Alice cannot send a message. They are not in the room.

# --- Chat History for General Discussion ---
# [12:12:34] Alice: Hello everyone!
# [12:12:34] Bob: Hey Alice, good to see you.
# [12:12:34] Charlie: Am I late to the party?
# ---------------------------------------
