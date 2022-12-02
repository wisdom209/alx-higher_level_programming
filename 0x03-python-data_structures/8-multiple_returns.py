#!/usr/bin/python3
if __name__ == '__main__':
    def multiple_returns(sentence):
        sentence_len = len(sentence)
        if (sentence_len == 0):
            return (0, None)
        return (sentence_len, sentence[0])
