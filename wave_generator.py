# Audio will contain a long list of samples (i.e. floating point numbers describing the
# waveform).  If you were working with a very long sound you'd want to stream this to
# disk instead of buffering it all in memory list this.  But most sounds will fit in
# memory.

import math
import wave
import struct

audio = []
sample_rate = 44100.0


def append_silence(duration_milliseconds=500):
    """
    Adding silence is easy - we add zeros to the end of our array
    """
    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(0.0)

    return


def append_sinewave(
        freq=440.0,
        duration_milliseconds=500,
        volume=1.0):
    """
    The sine wave generated here is the standard beep.  If you want something
    more aggresive you could try a square or saw tooth waveform.   Though there
    are some rather complicated issues with making high quality square and
    sawtooth waves... which we won't address here :)
    """

    global audio # using global variables isn't cool.

    num_samples = duration_milliseconds * (sample_rate / 1000.0)

    for x in range(int(num_samples)):
        audio.append(volume * math.sin(2 * math.pi * freq * ( x / sample_rate )))

    return


def save_wav(file_name):
    # Open up a wav file
    wav_file=wave.open(file_name,"w")

    # wav params
    nchannels = 1

    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
    nframes = len(audio)
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
    for sample in audio:
        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

    wav_file.close()

    return

def read_wav(path):
    bits = []
    datas = []
    sample_length = 22050
    with wave.open(path, "rb") as wavefile:
        # wave.Wave_read(wavefile)
        length = wavefile.getnframes()
        for i in range(0, length):
            wavedata = wavefile.readframes(1)
            data = struct.unpack("<h", wavedata)
            datas.append(data[0] != 0)
            if len(datas) == sample_length:
                bits.append(datas.count(True) > sample_length * 0.9)
                datas = []
    print(bits)
    return bits

if __name__ == '__main__':
    append_sinewave(volume=0.25)
    append_silence()
    append_sinewave(volume=0.5)
    append_silence()
    append_sinewave()
    save_wav("output.wav")