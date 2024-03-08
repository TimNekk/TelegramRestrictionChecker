from pyrogram.types import Restriction
from tabulate import tabulate


def print_restrictions_table(username_restrictions: dict[str, list[Restriction]]):
    table_data = []
    headers = ["Username", "Platform", "Reason", "Text"]

    for username, restrictions in filter(lambda x: x[1], username_restrictions.items()):
        for restriction in restrictions:
            table_data.append([username, restriction.platform, restriction.reason, restriction.text])

    print(tabulate(table_data, headers, tablefmt="pretty"))
