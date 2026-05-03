from datetime import datetime


def log_packet(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"

    with open("packets.log", "a") as file:
        file.write(formatted_message + "\n")
        