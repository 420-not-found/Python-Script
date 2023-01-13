import logging
import math
import os
import wave
from time import time

from stego_lsb.bit_manipulation import lsb_deinterleave_bytes, lsb_interleave_bytes

def recover_data(sound_path, output_path, num_lsb, bytes_to_recover):
    """Recover data from the file at sound_path to the file at output_path"""
    if sound_path is None:
        raise ValueError("WavSteg recovery requires an input sound file path")
    if output_path is None:
        raise ValueError("WavSteg recovery requires an output file path")
    if bytes_to_recover is None:
        raise ValueError("WavSteg recovery requires the number of bytes to recover")

    start = time()
    sound = wave.open(sound_path, "r")

    # num_channels = sound.getnchannels()
    sample_width = sound.getsampwidth()
    num_frames = sound.getnframes()
    sound_frames = sound.readframes(num_frames)
    

    if sample_width != 1 and sample_width != 2:
        # Python's wave module doesn't support higher sample widths
        raise ValueError("File has an unsupported bit-depth")

    start = time()
    data = lsb_deinterleave_bytes(
        sound_frames, 8 * bytes_to_recover, num_lsb, byte_depth=sample_width
    )
    

    start = time()
    output_file = open(output_path, "wb+")
    output_file.write(bytes(data))
    output_file.close()
recover_data("StarWars3.wav","test2.txt",1,10)




