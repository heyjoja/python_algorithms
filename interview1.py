"""
Q1: Giving the following string
sample = "aaabbbccbacdeb"



Print the 3 most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.



Note: order by letter if the number repeats



The sample output would be:
b : 5
a : 4
c : 3
"""
def question1(sample):
    order_by_letter = {}
    for letter in sample:
        if order_by_letter.get(letter):
            order_by_letter[letter] += 1
        else:
            order_by_letter[letter] = 1

    sort_letters = sorted(order_by_letter.items(), key=lambda x: x[1], reverse=True)
    for item in sort_letters:
        print(f'{item[0]}:{item[1]}')


"""
Q2: Giving two words please provide a list in alphabetical order of common characters found in both words, please avoid using nested loops
Sample input:
word_1 = 'maria'
word_2 = 'marcela'



The sample output would be:
['a', 'm', 'r']
"""

def question2(word1, word2):
    word1 = [value for value in word1]
    word2 = [value for value in word2]
    intersectionLetters = sorted(set(word1).intersection(word2))
    print(intersectionLetters)


if __name__ == '__main__':
    question1('aaabbbccbacdeb')
    question2('maria', 'marcela')
