import unittest

from kmk.keys import ALL_ALPHAS, ALL_NUMBERS, KC
from kmk.modules.text_replacement import Character, Phrase, Rule, TextReplacement
from tests.keyboard_test import KeyboardTest


class TestTextReplacement(unittest.TestCase):
    def setUp(self) -> None:
        self.symbols = '`-=[]\\;\',./~!@#$%^&*()_+{}|:\"<>?'
        self.everything = ALL_NUMBERS + ALL_ALPHAS + ALL_ALPHAS.lower() + self.symbols
        self.test_dictionary = {'aa': 'b', 'b': 'aa', '!': '@', 'dccc': 'dcbb'}
        self.text_replacement = TextReplacement(self.test_dictionary)
        self.keyboard = KeyboardTest(
            [self.text_replacement],
            [
                [KC.A, KC.B, KC.N1, KC.LSHIFT, KC.LCTRL, KC.C, KC.D],
            ],
            debug_enabled=True,
        )

        return super().setUp()

    def test_keyboard_events_are_correct(self):
        # backspace doesn't have to fire for the final key pressed
        # that results in a corresponding match, as that key is never sent
        # the matching key also never sends a keyup event
        self.keyboard.test(
            'multi-character key, single-character value',
            [(0, True), (0, False), (0, True), (0, False)],
            [{KC.A}, {}, {KC.BACKSPACE}, {}, {KC.B}, {}],
        )
        # note: the pressed key is never sent here, as the event is
        # intercepted and the replacement is sent instead
        self.keyboard.test(
            'multi-character value, single-character key',
            [(1, True), (1, False)],
            [{KC.A}, {}, {KC.A}, {}],
        )
        # modifiers are force-released if there's a match,
        # so the keyup event for them isn't sent
        self.keyboard.test(
            'shifted alphanumeric or symbol in key and/or value',
            [(3, True), (2, True), (2, False), (3, False)],
            [{KC.LSHIFT}, {KC.LSHIFT, KC.N2}, {}],
        )
        self.keyboard.test(
            'backspace is only tapped as many times as necessary to delete the difference between the key and value',
            [
                (6, True),
                (6, False),
                (5, True),
                (5, False),
                (5, True),
                (5, False),
                (5, True),
                (5, False),
            ],
            [
                {KC.D},
                {},
                {KC.C},
                {},
                {KC.C},
                {},
                {KC.BACKSPACE},
                {},
                {KC.B},
                {},
                {KC.B},
                {},
            ],
        )

    def test_invalid_character_in_dictionary_throws_error(self):
        dict = {
            'illegal_character_in_key': {'é': 'a'},
            'illegal_character_in_value': {'a': 'é'},
        }
        self.assertRaises(ValueError, TextReplacement, dict['illegal_character_in_key'])
        self.assertRaises(
            ValueError, TextReplacement, dict['illegal_character_in_value']
        )

    def test_character_constructs_properly(self):
        unshifted_character = Character(KC.A, False)
        shifted_letter = Character(KC.A, True)
        shifted_symbol = Character(KC.N1, True)
        self.assertEqual(
            unshifted_character.key_code,
            KC.A,
            'unshifted character key code is correct',
        )
        self.assertEqual(
            shifted_letter.key_code.__dict__,
            KC.LSHIFT(KC.A).__dict__,
            'shifted letter key code is correct',
        )
        self.assertEqual(
            shifted_symbol.key_code.__dict__,
            KC.LSHIFT(KC.N1).__dict__,
            'shifted symbol key code is correct',
        )

    def test_phrase_constructs_properly(self):
        combination = ALL_NUMBERS + ALL_ALPHAS + ALL_ALPHAS.lower()
        multi_character_phrase = Phrase(combination)

        # lower case
        for letter in ALL_ALPHAS:
            letter = letter.lower()
            phrase = Phrase(letter)
            self.assertEqual(
                phrase.get_character_at_index(0).key_code,
                KC[letter],
                f'Test failed when constructing phrase with lower-case letter {letter}',
            )
        # upper case
        for letter in ALL_ALPHAS:
            phrase = Phrase(letter)
            self.assertEqual(
                phrase.get_character_at_index(0).key_code.__dict__,
                KC.LSHIFT(KC[letter]).__dict__,
                f'Test failed when constructing phrase with upper-case letter {letter}',
            )
        # numbers
        for letter in ALL_NUMBERS:
            phrase = Phrase(letter)
            self.assertEqual(
                phrase.get_character_at_index(0).key_code,
                KC[letter],
                f'Test failed when constructing phrase with number {letter}',
            )
        # multi-character phrase
        for i, character in enumerate(combination):
            self.assertEqual(
                multi_character_phrase.get_character_at_index(i).key_code.__dict__,
                KC.LSHIFT(KC[character]).__dict__
                if combination[i].isupper()
                else KC[character].__dict__,
                f'Test failed when constructing phrase with character {character}',
            )

    def test_phrase_with_symbols_constructs_properly(self):
        phrase = Phrase(self.symbols)
        for i, symbol in enumerate(self.symbols):
            self.assertEqual(
                phrase.get_character_at_index(i).key_code.__dict__,
                KC[symbol].__dict__,
                'Test failed for symbol {}'.format(symbol),
            )

    def test_phrase_indexes_correctly(self):
        phrase = Phrase(ALL_ALPHAS.lower())
        i = 0
        while not phrase.index_at_end():
            self.assertTrue(
                phrase.character_is_at_current_index(phrase.get_character_at_index(i)),
                'Current character in the phrase is not the expected one',
            )
            self.assertEqual(
                phrase.get_character_at_index(i).key_code.__dict__,
                KC[ALL_ALPHAS[i]].__dict__,
                f'Character at index {i} is not {ALL_ALPHAS[i]}',
            )
            phrase.next_character()
            i += 1
            self.assertLess(
                i, len(ALL_ALPHAS) + 1, 'While loop checking phrase index ran too long'
            )
        phrase.reset_index()
        self.assertEqual(
            phrase.get_character_at_current_index().key_code,
            KC[ALL_ALPHAS[0]],
            'Phrase did not reset its index to 0',
        )

    def test_sanity_check(self):
        '''Test character/phrase construction with every letter, number, and symbol, shifted and unshifted'''
        phrase = Phrase(self.everything)
        for i, character in enumerate(self.everything):
            self.assertEqual(
                phrase.get_character_at_index(i).key_code.__dict__,
                KC.LSHIFT(KC[character]).__dict__
                if self.everything[i].isupper()
                else KC[character].__dict__,
                f'Test failed when constructing phrase with character {character}',
            )

    def test_rule(self):
        phrase1 = Phrase(self.everything)
        phrase2 = Phrase(self.everything)
        rule = Rule(phrase1, phrase2)
        self.assertEqual(
            rule.to_substitute, phrase1, "Rule's entry to be substituted is correct"
        )
        self.assertEqual(
            rule.substitution, phrase2, "Rule's substitution entry is correct"
        )
        rule.to_substitute.next_character()
        rule.substitution.next_character()
        rule.restart()
        self.assertEqual(
            rule.to_substitute.get_character_at_index(0).key_code,
            KC[self.everything[0]],
            'Rule did not call to_substitute.reset_index() when rule.restart() was called',
        )
        self.assertEqual(
            rule.substitution.get_character_at_index(0).key_code,
            KC[self.everything[0]],
            'Rule did not call substitution.reset_index() when rule.restart() was called',
        )


if __name__ == '__main__':
    unittest.main()
