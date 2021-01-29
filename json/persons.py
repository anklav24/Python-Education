# https://www.youtube.com/watch?v=t4FWQ9lP_Nk&list=PLlWXhlUMyooab9Tji3bNX8iyVDkllA3mP&index=3&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
import json
from random import choice


def gen_person():
    name = ''
    phone = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7']

    while len(name) != 5:
        name += choice(letters)

    while len(phone) != 7:
        phone += choice(nums)

    person = {
        "name": name,
        "phone": phone
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except:
        data = []

    data.append(person_dict)

    with open("persons.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    for i in range(5):
        write_json(gen_person())


if __name__ == '__main__':
    main()
