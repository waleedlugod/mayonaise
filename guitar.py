from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == "__main__":
    keyboard = "q2we4r5ty7u8i9op-[=]"
    stdkeys.create_window()

    #  create strings
    strings = [None] * len(keyboard)
    for key_idx in range(len(keyboard)):
        strings[key_idx] = GuitarString(440 * 1.059463 ** (key_idx - 12))

    strings[0].pluck()
    i = 0
    while True:
        print(i)
        i += 1
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key == "a":
                play_sample(0.5)
                # strings[0].pluck()

        # play_sample(strings[0].sample())

        # strings[0].tick()
