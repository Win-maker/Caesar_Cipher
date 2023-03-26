
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    final_text = ''
    if direction == 'decode':
        shift = shift * -1
        for char in text:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = position + shift
                final_text += alphabets[new_position]
            else:
                final_text += char
    elif direction == 'encode':
        for char in text:
            if char in alphabets:
                position = alphabets.index(char)
                new_position = position + shift
                final_text += alphabets[new_position]

    print(f'Your {direction} result is: {final_text}')

conti = True
while conti:
    direction = input('Choose encode or decode')
    text = input('Enter your text')
    shift = int(input('Enter your shift number'))
    shift = shift % 26
    caesar(text, shift, direction)
    end = input("Enter 'Y' or 'y' to continue or enter 'e' or 'E' to exit")
    if end == 'y' or end == 'Y':
        conti = True
    else:
        conti = False
        print('Thank For Using This Program')
