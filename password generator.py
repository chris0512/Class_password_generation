from random import choices
from string import ascii_letters, punctuation


class Password:
    """
    A password of customize strength and length

    Encapsulate a randomly generate
    :param strength: a measure of the password's effectiveness against brute-force guessing
    :type strength: str, optional

    :param length: the length of the password
    :type length: int, optional
    """

    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuation": list(punctuation)
    }

    DEFAULT_LENGTHS = {
        "low": 8,
        "mid": 12,
        "high": 16
    }

    @classmethod
    def show_input_universe(cls):
        """return the complete input universe from which characters and sample
        :return: The universe of characters from which random sampling is done to generate password
        :rtype: dict (of list-s)
        """
        return cls.INPUT_UNIVERSE

    def __init__(self, strength="mid", length=None):
        """Constructor method"""
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):

        population = self.INPUT_UNIVERSE["letters"]
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuation"]
        else:
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))


if __name__ == "__main__":
    p_weak = Password(strength="low")
    print("Weak password: " + p_weak.password)

    p_mid = Password(strength="mid", length=40)
    print("Mid password: " + p_mid.password)

    p_high = Password(strength="high")
    print("High password: " + p_high.password)
