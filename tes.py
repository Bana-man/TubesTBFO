import sys

if len(sys.argv) >= 2:
    input_file = sys.argv[2]
    print("Nama file input:", input_file)
else:
    print("Usage: python main.py pda.txt \"[nama_file].html\"")
