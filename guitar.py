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

    activeStrings = set()

    n_iters = 0
    while True:
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            index = keyboard.find(key)
            if index != -1:
                strings[index].pluck()
                activeStrings.add(strings[index])

        sample = 0
        newActiveStrings = activeStrings.copy()
        for string in activeStrings:
            sample += string.sample()
            if string.ticks_after_plucked() > 80000:
                newActiveStrings.remove(string)
        activeStrings = newActiveStrings

        play_sample(sample)

        for string in activeStrings:
            string.tick()
