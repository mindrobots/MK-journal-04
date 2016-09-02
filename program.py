# Program #4 from Michael Kennedy's Jumpstart Python

import journal


def main():
    print_headers()
    run_event_loop()


def print_headers():
    print('---------------------------------')
    print('         JOURNAL PROGRAM')
    print('---------------------------------')


def list_entries(data):
    print('Your journal entries:')
    entries = reversed(data)
    length = len(data)
    for idx, entry in enumerate(entries):
        print('* [{}]: {}'.format(length-idx, entry))


def add_entries(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


def run_event_loop():

    print('What do you want to do with your journal?')

    cmd = None
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x':

        cmd = input('[L]ist entries, [A]dd entry, E[x]it: ').lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x':
            print("Sorry, I don't understand '{}'.".format(cmd))

    print('Done. Goodbye!')

    journal.save(journal_name, journal_data)

if __name__ == '__main__':
    main()
