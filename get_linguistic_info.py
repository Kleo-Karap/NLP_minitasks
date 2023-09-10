class GetLinguisticInfo:

    def __init__(self,text):
        """
        Accepts a string. Converts the case of all string characters into lower.
        Replaces all the ASCII printable characters with the whitespace character.
        Further replaces the special characters "»" and "«" with whitespace.
        :param text:
        """
        self.text=text
        self.word_frequencies={}
        clear_text=text.lower()
        for char1 in clear_text:
            if char1.isascii():
                clear_text=clear_text.replace(char1,' ')
        for char2 in "»,«":
            clear_text=clear_text.replace(char2,' ')
        self.words=clear_text.split()



    def generate_frequencies(self):
        """
        Iterates over each item in the list 'words' of the class.
        If a list item is already added in the dictionary as key with its value,
        modifies the dictionary's value for this key by adding 1
        or, if the list item is not included in the dictionary,
        adds the list item as key in the dictionary of the class with the value 1
        :param: None
        :return:Nothing
        """
        for word in self.words:
            if word in self.word_frequencies:
                self.word_frequencies[word] += 1
            else:
                self.word_frequencies[word]=1
        return




    def get_frequency(self,word):
        """
        Accepts a string checks if the given string is a key in the dictionary.
        If yes, it removes the key- value pair from the dictionary and returns
        the value of the specific key in the console.
        If the specified key does not exist in the dictionary, returns the value 0.

        :param word:
        :return: the frequency value of the specific key
        """
        word=word.lower()
        if word in self.word_frequencies.keys():
            value =self.word_frequencies.pop(word)
        else:
            value =self.word_frequencies.get(word,0)
        return f'The word "{word}" occurs {value} time(s) in the given text'



    def get_words(self):
        """
        :return: The list of the class,cleared from all possible ASCII characters
        (special characters, digits, upper and lowercase English letters)
        """
        return self.words

text_content="Για κύμα κακοκαιρίας που έρχεται  από την Italy και θα πλήξει τη χώρα από την ερχόμενη Παρασκευή έως την Κυριακή, προειδοποιεί ο μετεωρολόγος Κλέαρχος Μαρουσάκης." \
             "Χαρακτηρίζει, μάλιστα, το φαινόμενο ως «μετεωρολογική βόμβα» και σε ανάρτησή του εξηγεί τι είναι αυτό το φαινόμενο που θα επιφέρει χιόνια, ισχυρούς ανέμους και πτώση της θερμοκρασίας." \
             "Πάντως έως την Πέμπτη προβλέπεται διατήρηση του «θερμού σκηνικού», με τον υδράργυρο να παραμένει στην Αθήνα σε υψηλότερα από την εποχή επίπεδα κατά 6 με 8 βαθμούς."

text_1=GetLinguisticInfo(text_content)
text_1.generate_frequencies()
print(text_1.get_frequency("whatever"))
print(text_1.get_frequency("ΓιΑ"))
print(text_1.get_words())





