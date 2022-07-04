# Text Replacement

The Text Replacement module lets a user replace one typed sequence of characters with another. If a string of characters you type matches an entry in your dictionary, it gets deleted and replaced with the corresponding replacement string.

Potential uses:

- Rudimentary auto-correct: replace `yuo` with `you`
- Text expansion, à la [espanso](https://github.com/federico-terzi/espanso): when `:sig` is typed, replace it with `John Doe`, or turn `idk` into `I don't know`

## Usage

The Text Replacement module takes a single argument to be passed during initialization: a user-defined dictionary where the keys are the text to be replaced and the values are the replacement text.

Example is as follows:

```python
from kmk.modules.text_replacement import TextReplacement

my_dictionary = {
    'yuo': 'you',
    ':sig': 'John Doe',
    'idk': "I don't know"
}
text_replacement = TextReplacement(dictionary=my_dictionary)
keyboard.modules.append(text_replacement)
```

### Recommendations

1. Consider prefixing text expansion entries with a symbol to prevent accidental activations: `:sig`, `!email`, etc.
2. If you want multiple similar replacements, consider adding a number to prevent unreachable matches: `replaceme1`, `replaceme2`, etc.

### Limitations

1. Since this runs on your keyboard, it is not context-aware. It can't tell if you are typing in a valid text field or not.
2. In the interest of a responsive typing experience, the first valid match will be used as soon as it is found. If your dictionary contains "abc" and "abcd", "abcd" will not be matchable.