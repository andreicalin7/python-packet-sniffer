def log_packet(message):
    with open("packets.log", "a") as file:
        file.write(message + "\n")