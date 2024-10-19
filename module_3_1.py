calls = 0
def cound_calls():
    global calls
    calls += 1

def string_info(word):
    global book_
    cound_calls()
    book_ = (len(word), word.upper(), word.lower())
    return book_

def is_contains(key: str, row: list) -> bool:
    global binar
    cound_calls()
    binar = False
    for i in row:
        if i.lower() == key.lower():
            return True
    return binar

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)