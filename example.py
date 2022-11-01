def create_user(name, attributes):
    if name == 'Maurice':
        return print('this user already exists')

    return {name: attributes}

def hello_world(message):
    return print(f'Hello World {message}')

if __name__ == '__main__':
    create_user('Maurice', ['1', 2, 3])
    hello_world('First example')
