from bitstring import BitArray
from wave_generator import *

def convert_file_to_wave(path):
    with open(path, "rb") as file:
        content = file.read()
        bitsring = convert_file_to_bitstring(content)
        convert_bitstring_to_wave(bitsring)


def convert_wave_to_file(path):
    # with open(path, "rb") as file:
    #     content = file.read()
    #     bitstring = convert_wave_to_bitstring(content)
    #     write_bitstring_to_file(bitstring)
    bitstring = read_wav(path)
    # data = int(''.join(['1' if i else '0' for i in bitstring]), 2)
    write_bitstring_to_file(bitstring)


def convert_bitstring_to_wave(bits):
    for bit in bits:
        if bit:
            append_sinewave(volume=1.0)
        else:
            append_silence()
    save_wav("geklauter-sound.wav")


def convert_wave_to_bitstring(wave_bits):
    bits = []
    read_wav
    print(wave_bits)



def convert_file_to_bitstring(file):
    bits = BitArray(bytes=file)
    return bits


def print_bit_array(bits):
    for bit in bits:
        print(bit)

def write_bitstring_to_file(bitstring):
     with open('somefile.txt', 'wb') as file:
        BitArray(auto=bitstring).tofile(file)

if __name__ == '__main__':
    # convert_file_to_wave("file.txt")
    convert_wave_to_file("geklauter-sound.wav")
    # convert_wave_to_file("output.wav")