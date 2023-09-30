from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys


if __name__ == "__main__":
    # set of keys
    keyboard = "q2we4r5ty7u8i9op-[=]"
    # initalize window
    stdkeys.create_window()
    # maximum amount of ticks since string was last plucked
    MAX_TICKS = 80000

    # create strings
    strings = [None] * len(keyboard)
    for key_idx in range(strings):
        strings[key_idx] = GuitarString(440 * 1.059463 ** (key_idx - 12))

    # strings being simulated
    plucked_strings = set()

    n_iters = 0
    while True:
        # reduce bottleneck
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # process typed keys
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            # if pressed key is part of keyboard, pluck corresponding string
            key_index = keyboard.find(key)
            if key_index != -1:
                strings[key_index].pluck()
                plucked_strings.add(strings[key_index])

        # compute superposition of samples and cull simulated strings
        sample = 0
        new_plucked_strings = plucked_strings.copy()
        for string in plucked_strings:
            # add to total sample
            sample += string.sample()
            # stop simulating string after max ticks have passed since it was first plucked
            if string.ticks_after_plucked() > MAX_TICKS:
                new_plucked_strings.remove(string)
        # update currently simulated strings
        plucked_strings = new_plucked_strings

        # play sample
        play_sample(sample)

        # advance simulation of currently active strings
        for string in plucked_strings:
            string.tick()
