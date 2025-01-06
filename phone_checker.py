import rich
import requests

import config


def check_phone(phone):
    response = requests.get(
        url = f"http://phone-number-api.com/json/?number={phone}",
        headers = config.HEADERS
    )


    if response.status_code == 200:
        rich.print(
f"""
[ PHONE NUMBER RESULTS ]

[green]->[/green] Found some info

| DETAILS
{response.json()}

[ --- ]

"""
        )
    else:
        rich.print(
f"""
[ PHONE NUMBER RESULTS ]

[red]-> Information about `{phone}` not found![/red]

[ --- ]

"""
        )
