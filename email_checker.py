import rich
import requests

import config


def github(email):
    try:
        response = requests.get(
            url = "https://api.github.com/search/users",
            params = {
                "q" : email,
                "in": "email"
            },
            headers = config.HEADERS
        )

        if response.status_code == 200:
            data = response.json()

            if data["total_count"] > 0:
                for user in data["items"]:
                    rich.print(
f"""
[ GITHUB RESULTS ]

[green]-> GitHub (github.com) account found[/green]

| DETAILS
|
|    Username
|        [green]->[/green] @{user["login"]}
|
|    User ID
|        [green]->[/green] {user["id"]}
|
|    Link to profile
|        [green]->[/green] https://github.com/{user["login"]}

[ --- ]
"""
                    )
            else:
                rich.print("[yellow]-> GitHub (github.com) account not found![/yellow]")
        else:
            rich.print(f"[red]-> GitHub (github.com) account not found! Error {response.status_code}[/red]")
    except Exception as e:
        rich.print(f"[red]-> GitHub (github.com) account not found! Raised error: {e}[/red]")

def pinterest(email):
    try:
        response = requests.get(
            url = "https://www.pinterest.com/resource/EmailExistsResource/get/",
            params = {
                "source_url": "/",
                "data": '{"options": {"email": "' + email + '"}, "context": {}}'
            },
            headers = config.HEADERS
        )
    
        if response.status_code == 200:
            data = response.json()

            if not data["resource_response"]["data"]:
                rich.print(
"""
[ PINTEREST RESULTS ]

[green]-> Pinterest (www.pinterest.com) account found[/green]

| DETAILS
|
|    None

[ --- ]
"""
                )
            else:
                rich.print("[yellow]-> Pinterest (www.pinterest.com) account not found![/yellow]")
        else:
            rich.print("[yellow]-> Pinterest (www.pinterest.com) account not found![/yellow]")

    except Exception as e:
        rich.print(f"[red]-> Pinterest (www.pinterest.com) account not found! Raised error: {e})[/red]")

def spotify(email):
    try:
        response = requests.get(
            url = "https://spclient.wg.spotify.com/signup/public/v1/account",
            params = {
                "validate": 1,
                "email": email
            },
            headers = config.HEADERS
        )

        if response.status_code == 200:
            responseData = response.json()

            if responseData.get("status") == 20:
                rich.print(
"""
[ SPOTIFY RESULTS ]

[green]-> Spotify (spotify.com) account found[/green]

| DETAILS
|
|    None
[ --- ]
"""
                )
            else:
                rich.print("[yellow]-> Spotify (spotify.com) account not found![/yellow]")
        else:
            rich.print("[yellow]-> Spotify (spotify.com) account not found![/yellow]")

    except Exception as e:
        rich.print(f"[red]-> Spotify (spotify.com) account not found! Raised error: {e}[/red]")

def twitter(email):
    try:
        response = requests.get(
            url = "https://api.twitter.com/i/users/email_available.json",
            params = {
                "email": email
            },
            headers = config.HEADERS
        )

        if response.status_code == 200:
            data = response.json()

            if not data["valid"]:
                rich.print(
"""
[ TWITTER RESULTS ]

[green]-> Twitter (twitter.com) account found[/green]

| DETAILS
|
|    None

[ --- ]
"""
                )
            else:
                rich.print("[yellow]-> Twitter (twitter.com) account not found![/yellow]")
    except Exception as e:
        rich.print(f"[red]-> Twitter (twitter.com) account not found! Raised {e}[/red]")

def chess(email):
    try:
        response = requests.get(
            url = "https://www.chess.com/callback/email/available",
            params = {
                "email": email
            },
            headers = config.HEADERS
        )
        data = response.json()

        if data.get("isEmailAvailable") == True:
            rich.print("[yellow]-> Chess (www.chess.com) account not found![/yellow]")
        elif data.get("isEmailAvailable") == False:
            rich.print(
"""
[ CHESS RESULTS ]

[green]-> Chess (www.chess.com) account found[/green]

| DETAILS
|
|    None

[ --- ]
"""
            )
    except Exception as e:
        rich.print(f"[red]-> Chess (chess.com) account not found! (raised {e})[/red]")
