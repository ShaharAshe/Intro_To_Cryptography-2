import numpy as np

class VigenereCipher:
    def __init__(self, text:str, time:int=1):
        self.text = text
        self.text_str = [float(c) for c in text if c.isnumeric()]
        self.frequencies_vector = []
        self.__get_frequencies_vector()
        self.time = time
    
    def __get_frequencies_vector(self):
        for i in range(len(self.text_str)):
            if self.text_str[i] == 0:
                self.frequencies_vector.append(0.7)
            elif self.text_str[i] == 1:
                self.frequencies_vector.append(0.2)
            elif self.text_str[i] == 2:
                self.frequencies_vector.append(0.1)

    def encrypt(self):
        sum = 0

        while True:
            temp_frequencies_vector:list = self.frequencies_vector[self.time:]+self.frequencies_vector[0:self.time]
            temp_sum = 0
            for i in range(len(temp_frequencies_vector)):
                if self.frequencies_vector[i] == temp_frequencies_vector[i]:
                    temp_sum += 1
            if temp_sum > sum:
                sum = temp_sum
                self.time += 1
            else:
                self.time -= 1
                return (sum, self.time)


    def __str__(self) -> str:
        return f'{self.text = }\n -> {self.text_str = }\n -> {self.frequencies_vector = }'



if __name__ == '__main__':
    Encrypted_text:str = "01221 22102 21211"
    cipher = VigenereCipher(Encrypted_text, 2)
    print(cipher)
    print(cipher.encrypt())
