import time


user_dict = {}

intro_msg = """
Hi {},
I am Botty The ChatBot,
Ujjwal is currently busy somewhere (idk where ¯\_(ツ)_/¯).

Either you can wait for him to get back, or talk to me!

    send: Botty <message>

(to talk to Botty start your message with Botty)

You can ask for Ujjwal's phone number, email as of now, I am under development.


"""

botty_msg = """
Ah, so want to talk to Botty!\n{}
"""

def get_message(msg, user_id, username):
    print("{}: {}".format(user_id, msg))

    if 'botty' in msg.lower():
        if ('menu' in msg.lower()):
            return intro_msg.format(username)

        elif ('phone' in msg.lower()):
            return botty_msg.format("789-774-5889")

        elif ('email' in msg.lower()):
            return botty_msg.format("ujjwalraizada@gmail.com")

        elif ('surprise' in msg.lower()):
            return botty_msg.format("My brain in currently under development!")
        
        else:
            return botty_msg.format("Hey Botty here! you want something?")


    if user_id not in user_dict:
        user_dict[user_id] = time.time()
        return intro_msg.format(username)

    else:
        if ((time.time() - user_dict[user_id]) > 600):
            user_dict[user_id] = time.time()
            text = "Hi there! Botty here again. \nHow can I help you?\n (send 'Botty menu' to get menu)"
            return text
    return None

