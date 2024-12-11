def calculate_checksum(data):
    """
    Calculate the checksum for the given data string.
    """
    checksum = 0
    for char in data:
        checksum += ord(char)  # Add the ASCII value of each character
    checksum = ~checksum & 0xFF  # Perform bitwise NOT and mask with 8 bits
    return checksum


def verify_checksum(data, checksum):
    """
    Verify the checksum for the received data.
    """
    calculated_checksum = calculate_checksum(data)
    combined = (calculated_checksum + checksum) & 0xFF
    return combined == 0xFF  # If all bits are 1, the checksum is valid


def main():
    # Sender side
    message = "1"  # Example message
    print("Sender Side:")
    print(f"Original Message: {message}")
    sender_checksum = calculate_checksum(message)
    print(f"Calculated Checksum: {sender_checksum}")

    # Simulating data and checksum sent to the receiver
    transmitted_message = message  # Message remains unchanged in this simulation
    transmitted_checksum = sender_checksum

    # Receiver side
    print("\nReceiver Side:")
    print(f"Received Message: {transmitted_message}")
    print(f"Received Checksum: {transmitted_checksum}")

    # Verify checksum
    if verify_checksum(transmitted_message, transmitted_checksum):
        print("Checksum is valid. Data received correctly.")
    else:
        print("Checksum is invalid. Data corruption detected.")


if __name__ == "__main__":
    main()
