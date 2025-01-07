import rich
import requests

import config


def github(email):
    try:
        response = requests.get(
            url = f"https://api.github.com/search/users?q={email}+in:email",
            headers = config.HEADERS
        )

        if response.status_code == 200:
            result = response.json()

            if result["total_count"] > 0:
                for user in result["items"]:
                    rich.print(
f"""
[ GITHUB RESULTS ]

[green]->[/green] GitHub (github.com) account found

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
                rich.print(
"""
[ GITHUB RESULTS ]

[red]-> GitHub (github.com) account not found![/red]

[ --- ]

"""
                )
        else:
            rich.print(
f"""
[ GITHUB RESULTS ]

[red]-> GitHub (github.com) account not found! (error {response.status_code})[/red]

[ --- ]

"""
            )
    except Exception as e:
        rich.print(
f"""
[ GITHUB RESULTS ]

[red]-> GitHub (github.com) account not found! (raised {e})[/red]

[ --- ]

"""
        )

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

[green]->[/green] Pinterest (www.pinterest.com) account found

[ --- ]

"""
                )
            else:
                rich.print(
"""
[ PINTEREST RESULTS ]

[red]-> Pinterest (www.pinterest.com) account not found![/red]

[ --- ]

"""
                )
        else:
            rich.print(
"""
[ PINTEREST RESULTS ]

[red]-> Pinterest (www.pinterest.com) account not found![/red]

[ --- ]

"""
            )

    except Exception as e:
        rich.print(
f"""
[ PINTEREST RESULTS ]

[red]-> Pinterest (www.pinterest.com) account not found! (raised {e})[/red]

[ --- ]

"""
        )

def spotify(email):
    try:
        response = requests.get(
            url = f"https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email={email}",
            headers = config.HEADERS
        )

        if response.status_code == 200:
            responseData = response.json()

            if responseData.get("status") == 20:
                rich.print(
"""
[ SPOTIFY RESULTS ]

[green]->[/green] Spotify (spotify.com) account found

[ --- ]

"""
                )
            else:
                rich.print(
"""
[ SPOTIFY RESULTS ]

[red]-> Spotify (spotify.com) account not found![/red]

[ --- ]

"""
                )
        else:
            rich.print(
"""
[ SPOTIFY RESULTS ]

[red]-> Spotify (spotify.com) account not found![/red]

[ --- ]

"""
            )

    except Exception as e:
        rich.print(
f"""
[ SPOTIFY RESULTS ]

[red]-> Spotify (spotify.com) account not found! (raised {e})[/red]

[ --- ]

"""
        )

def twitter(email):
    try:
        response = requests.get(
            url = f"https://api.twitter.com/i/users/email_available.json?email={email}",
            headers = config.HEADERS
        )

        if response.status_code == 200:
            data = response.json()

            if not data["valid"]:
                rich.print(
"""
[ TWITTER RESULTS ]

[green]->[/green] Twitter (twitter.com) account found

[ --- ]

"""
                )
            else:
                rich.print(
"""
[ TWITTER RESULTS ]

[red]-> Twitter (twitter.com) account not found![/red]

[ --- ]

"""
                )
    except Exception as e:
        rich.print(
f"""
[ TWITTER RESULTS ]

[red]-> Twitter (twitter.com) account not found! (raised {e})[/red]

[ --- ]

"""
        )

def chess(email):
    try:
        response = requests.get(
            url = f"https://www.chess.com/callback/email/available?email={email}",
            headers = config.HEADERS
        )
        data = response.json()

        if data.get("isEmailAvailable") == True:
            rich.print(
"""
[ CHESS RESULTS ]

[red]-> Chess (www.chess.com) account not found![/red]

[ --- ]

"""
            )
        elif data.get("isEmailAvailable") == False:
            rich.print(
"""
[ CHESS RESULTS ]

[green]->[/green] Chess (www.chess.com) account found

[ --- ]

"""
            )
    except Exception as e:
        rich.print(
f"""
[ CHESS RESULTS ]

[red]-> Chess (chess.com) account not found! (raised {e})[/red]

[ --- ]

"""
        )
