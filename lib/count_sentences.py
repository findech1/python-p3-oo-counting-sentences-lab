class MyString:
    def __init__(self, value="Hello."):
        if not isinstance(value, str):
            raise ValueError("Value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self.value.split('?') if sentence.strip()]
        sentences += [sentence.strip() for sentence in self.value.split('!') if sentence.strip()]
        return len(sentences)

# Example usage:
my_string = MyString("Hello.")
print(my_string.is_sentence())  # Output: False
print(my_string.is_question())  # Output: False
print(my_string.is_exclamation())  # Output: False
print(my_string.count_sentences())  # Output: 0
