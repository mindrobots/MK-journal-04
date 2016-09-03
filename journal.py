import os


def load(name):
    filename = get_full_pathname(name)
    print('...reading from: {}'.format(filename))
    data = []
    if os.path.exists(filename):
        with open(filename) as file_in:
            for entry in file_in.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):

    filename = get_full_pathname(name)
    print('...saving to: {}'.format(filename))

    with open(filename, 'w') as file_out:
        for entry in journal_data:
            file_out.write(entry + '\n')


def get_full_pathname(name):
    return os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))


def add_entry(text, data):
    data.append(text)
