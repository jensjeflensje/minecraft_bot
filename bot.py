from helpers import auth, conn, chat
import random
import sys
import time

address = input("Wat is het server ip?\n")
port = int(input("Wat is de server port?\n"))
version = int(input("Wat is de server versie code?\n"))

accounts = []

alts_file = open("alts.txt")
alts = alts_file.readlines()

for alt in alts:
    alt = alt.replace("\n", "")
    user, passw = alt.split(":")
    print(f"User {user} stored")
    accounts.append({"username": user, "password": passw})

print(f"Total accounts: {len(accounts)}")

tokens = []

for account in accounts:
    token = auth.auth_account(account)
    if token:
        tokens.append(token)
        print(f"User login for {account['username']}: SUCCESS")
        continue
    print(f"User login for {account['username']}: FAILED")
    time.sleep(1)

print(f"Total logged in: {len(tokens)}/{len(accounts)}")

mc_conns = []

for token in tokens:
    mc_conn = conn.create_conn(address, port, version, token)
    mc_conns.append(mc_conn)
    print(f"User connected...")
    time.sleep(5)

print("All users connected.")

chat_choice = int(input("Welke chatmodus wil je gebruiken?\n1: Zelf chatten\n2: Random getal\n"))

if chat_choice == 1:
    print("Je mag nu chatten:")
    while True:
        try:   
            msg = input("")
            for mc_conn in mc_conns:
                chat.send_message(mc_conn, msg)
        except KeyboardInterrupt:
            print("Aanval gestopt, DOEI!")
            sys.exit()
elif chat_choice == 2:
    print("Random getal aanval begint nu.")
    while True:
        try:   
            random_int = random.randint(0, 1000000)
            for mc_conn in mc_conns:
                chat.send_message(mc_conn, random_int)
        except KeyboardInterrupt:
            print("Aanval gestopt, DOEI!")
            sys.exit()
        print(1)
else:
    print("Chatmodus niet gevonden.")
