#!/usr/bin/env python3
'''Reads through the e-mail file from the text, mbox-short.txt, 
finds all of the lines that start with From: and To:, 
processes the e-mail addresses, 
and prints output as described by the assignment.

Usage: python fromto.py
'''

def update_dict(dict, entry):
    '''Helper method to use a dictionary as a counter.'''
    try:
        dict[entry] += 1
    except KeyError:
        dict[entry] = 1


def parse_file(filename):
    '''Parse the mbox file.
    
    We want the users and hosts of the "From:" and "To:" sections.
    '''
    from_user, from_host, to_user, to_host = {}, {}, {}, {}
    with open(filename) as f:
        for line in f:
            if line.startswith("From:") or line.startswith("To:"):
                # line == "From: user@host\n"
                head, email = line.split(": ")
                # line.split(": ") == ["From", "user@host\n"]
                # head == "From"
                # email == "user@host\n"
                user, host = email.strip().split("@")
                if head == "From":
                    update_dict(from_user, user)
                    update_dict(from_host, host)
                elif head == "To":
                    update_dict(to_user, user)
                    update_dict(to_host, host)
    return from_user, from_host, to_user, to_host


if __name__ == "__main__":
    
    from_user, from_host, to_user, to_host = parse_file("mbox-short.txt")
    
    print('--- FROM USER ---')
    for user, count in sorted(from_user.items()):
        print(f'{user},{count}\n')
    
    print('--- FROM HOST ---')
    for host, count in sorted(from_host.items()):
        print(f'{host},{count}\n')
    
    print('--- TO USER ---')
    for user, count in sorted(to_user.items()):
        print(f'{user},{count}\n')
    
    print('--- TO HOST ---')
    for host, count in sorted(to_host.items()):
        print(f'{host},{count}\n')
