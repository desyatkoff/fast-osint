import rich
import requests

import config


def check_ip(ip):
    response = requests.get(
        url = f"https://ipwhois.app/json/{ip}",
        headers = config.HEADERS
    )

    if response.status_code == 200:
        result = response.json() 

        rich.print(
f"""
[ IP RESULTS ]

[green]->[/green] Found some info

| DETAILS
|
|    IP
|        [green]->[/green] {result.get("ip")}
|
|    Country
|        [green]->[/green] {result.get("country")}
|
|    Region
|        [green]->[/green] {result.get("region")}
|
|    City
|        [green]->[/green] {result.get("city")}
|
|    Location
|        [green]->[/green] {result.get("latitude")}, {result.get("longitude")}
|
|    Internet Service Provider (ISP)
|        [green]->[/green] {result.get("isp")}
|
|    Organization
|        [green]->[/green] {result.get("org")}

[ --- ]

"""
        )
    else:
        rich.print(
"""
[ IP RESULTS ]

[red]-> Couldn't find any information[/red]

[ --- ]

"""
        )
