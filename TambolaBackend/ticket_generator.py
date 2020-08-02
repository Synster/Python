import random

import numpy as np
from tabulate import tabulate


def get_tickets(num_of_tickets):
    all_tickets = []
    for j in range(num_of_tickets):
        ticket = np.full(27, 1).reshape(9, 3)
        ticket[:4, :] *= 0
        [np.random.shuffle(ticket[:, i]) for i in range(3)]

        for i in range(9):
            num = np.arange(1, 11)
            np.random.shuffle(num)
            num = np.sort(num[:3])
            ticket[i, :] *= (num + i * 10)
            all_tickets.append(ticket.T)
    return all_tickets


def get_all_corners(ticket):
    corners = []
    corners.extend(list(filter(lambda x: x != 0, ticket[0]))[slice(0, 5, 4)])
    corners.extend(list(filter(lambda x: x != 0, ticket[2]))[slice(0, 5, 4)])
    return corners


def get_first_line(ticket):
    return list(filter(lambda x: x != 0, ticket[0]))


def get_second_line(ticket):
    return list(filter(lambda x: x != 0, ticket[1]))


def get_third_line(ticket):
    return list(filter(lambda x: x != 0, ticket[1]))


def get_full_house(all_tickets):
    return [i for ticket in all_tickets for i in list(filter(lambda x: x != 0, ticket))]


generated_nums = [1, 2, 3, 5, 6, 8, 9]


def get_next_number():
    n = random.randint(1, 10)
    if n in generated_nums:
        return get_next_number()
    else:
        generated_nums.append(n)
        return n


if __name__ == '__main__':
    tickets = get_tickets(10)
    print(tabulate(tickets[7], tablefmt="fancy_grid"))
    print(tabulate(tickets[1], tablefmt="fancy_grid"))
    print(tabulate(tickets[2], tablefmt="fancy_grid"))
    print(tabulate(tickets[3], tablefmt="fancy_grid"))
    print(get_all_corners(tickets[7]))
    print(get_first_line(tickets[7]))
    print(get_second_line(tickets[7]))
    print(get_third_line(tickets[7]))
    print(get_full_house(tickets[7]))
    print(get_next_number())
