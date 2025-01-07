import rich
import requests

import config


def check_phone(phone):
    response = requests.get(
        url = f"http://phone-number-api.com/json/",
        params = {
            "number": phone
        },
        headers = config.HEADERS
    )
    data = response.json()


    if response.status_code == 200:
        rich.print(
f"""
[ PHONE NUMBER RESULTS ]

[green]-> Found some info[/green]

| DETAILS
|
|    Is valid?:
|        [green]->[/green] {data["numberValid"]}
|
|    Number type:
|        [green]->[/green] {data["numberType"]}
|
|    Country:
|        [green]->[/green] {data["countryName"]}
|
|    Region:
|        [green]->[/green] {data["regionName"]}
|
|    City:
|        [green]->[/green] {data["city"]}

[ --- ]

"""
        )
    else:
        rich.print("[yellow]-> Couldn't find any information![/yellow]")
