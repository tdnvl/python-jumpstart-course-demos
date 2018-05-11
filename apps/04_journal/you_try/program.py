import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print("-----------------------------------")
    print("        JOURNAL APP")
    print("-----------------------------------")


def run_event_loop():

    print("What do you want to do with your journal?")

    cmd = None # Nice way to initialize a variable with no real value
    journal_name = "default"
    journal_data = journal.load(journal_name)

    while cmd != "x":
        cmd = input("[L]ist entries, [A]dd entries, or E[x]it: ").lower().strip()

        # the lower and strip methods make the app more forgiving of entry
        # strip returns a copy of the string with leading and trailing whitespace removed

        if cmd == "l":
            list_entries(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x":
            print("Sorry, we don't understand '{}'".format(cmd))

    print("Done! Goodbye.")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("{}. {}".format(idx, entry))


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    data.append(text)


main()
