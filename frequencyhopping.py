import time

# List of frequencies to hop to
frequencies = [2.4e9, 2.45e9, 2.5e9]


# Function to change the frequency
def hop_frequency(frequency):
    # Code to change the frequency of the wireless device goes here
    print(f'Hopping to frequency {frequency} Hz')


# Frequency hopping loop
while True:
    for frequency in frequencies:
        hop_frequency(frequency)
        time.sleep(1)
