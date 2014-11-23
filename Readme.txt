1. To run the project, two laptops each with 1 Gigabit Ethernet is required.

2. The two laptops should have Ubuntu 64-bit and must have GNURadio and UHD installed.

3. Connect the laptops with USRP via ethernet.

4. On one laptop run any of the transmitter files, e.g. sine wave transmitter, by running command
		sudo ./sine_wave_transmitter.py

5. On the other laptop run the corresponding receiver file, e.g. sine_wave_recevier by running command
		sudo ./sine_wave_receiver.py

6. After running, wait for few seconds for the FFT to display on the screen.