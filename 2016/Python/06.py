from collections import Counter

with open("inputs/06.txt") as f:
    messages=f.read().splitlines()
    message_length=len(messages[0]) # Extract messages length as parameter
    messages=''.join(messages) # Built a single string with the concatenation of messages

initial_message=''
for i in range(message_length):
    message=messages[i::message_length] # Extract the message
    message=Counter(message) # Count the occurences
    message=message.most_common(1)[0] # Extract the 1 most common characters
    message=list(message)[0] # Convert to list and take the first element of the pair
    initial_message+=message # Concatene it to form the initial message

print('After analysis, the initial message is',initial_message)

initial_message=''.join([list((Counter(messages[i::message_length]).most_common()[-1]))[0] for i in range(message_length)]) # One line equivalent
print('Ok, we just told me the repetition code has been modified. The new message therefore is', initial_message)
