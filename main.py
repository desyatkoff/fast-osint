import os
import time
import random

import bs4
import rich
import requests

import config
import email_checker
import phone_checker
import ip_checker


ASCII_LOGO = """
███████╗ █████╗ ███████╗████████╗      
██╔════╝██╔══██╗██╔════╝╚══██╔══╝      
█████╗  ███████║███████╗   ██║         
██╔══╝  ██╔══██║╚════██║   ██║         
██║     ██║  ██║███████║   ██║         
╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝         
                                       
 ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║   ██║███████╗██║██╔██╗ ██║   ██║   
██║   ██║╚════██║██║██║╚██╗██║   ██║   
╚██████╔╝███████║██║██║ ╚████║   ██║   
 ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
"""


class Main:
    def __init__(self):
        os.system("cls || clear")
        self.menu()


    def menu(self):
        rich.print(f"{ASCII_LOGO}\nMade by [blue]@desyatkoff[/blue]\n\n\n")

        rich.print(
"""
[ MAIN MENU ]

You want to get information about ...?

[bold red]0.[/bold red] [red]Exit[/red]

[bold green]1.[/bold green] [green]Email[/green]
[bold blue]2.[/bold blue] [blue]Phone number[/blue]
[bold yellow]3.[/bold yellow] [yellow]Internet Protocol address (IPv4)[/yellow]

[ --- ]
"""
        )


        self.option = input("Choose\n: ")
        print("\n")


        if self.option == "0":
            self.are_you_sure = input("Are you sure? [Y/n]\n: ")

            if self.are_you_sure.lower() == "y" or len(self.are_you_sure) < 1:
                quit(0)
            else:
                os.system("cls || clear")
                self.menu()
        elif self.option == "1":
            self.check_email()
        elif self.option == "2":
            self.check_phone()
        elif self.option == "3":
            self.check_ip()
        else:
            rich.print("[red]Incorrect value![/red]")

            time.sleep(1)

            os.system("cls || clear")
            self.menu()

    def check_email(self):
        self.email = input("Enter email\n: ")
        print("\n")

        if len(self.email) > 0:
            rich.print(f"Searching info about [blue]`{self.email}`[/blue]...")

            time.sleep(1)

            rich.print("Checking [bold]GitHub...[/bold]\n")
            email_checker.github(
                email = self.email
            )

            rich.print("Checking [bold]Pinterest...[/bold]\n")
            email_checker.pinterest(
                email = self.email
            )

            rich.print("Checking [bold]Spotify...[/bold]\n")
            email_checker.spotify(
                email = self.email
            )

            rich.print("Checking [bold]Twitter...[/bold]\n")
            email_checker.twitter(
                email = self.email
            )
        else:
            rich.print("[red]Missing value![/red]")

            time.sleep(1)

            os.system("cls || clear")
            self.menu()


        input("Press <Enter> to continue")
        os.system("cls || clear")
        self.menu()

    def check_phone(self):
        self.phone = input("Enter phone number (for example: +123456789)\n: ")
        print("\n")

        if len(self.phone) > 0:
            rich.print(f"Searching info about [blue]`{self.phone}`[/blue]...")

            phone_checker.check_phone(
                phone = self.phone
            )
        else:
            rich.print("[red]Missing value![/red]")

            time.sleep(1)

            os.system("cls || clear")
            self.menu()


        input("Press <Enter> to continue")
        os.system("cls || clear")
        self.menu()

    def check_ip(self):
        self.ip = input("Enter IP\n: ")
        print("\n")


        if len(self.ip) > 0:
            rich.print(f"Searching info about [blue]`{self.ip}`[/blue]...")

            ip_checker.check_ip(
                ip = self.ip
            )
        else:
            rich.print("[red]Missing value![/red]")

            time.sleep(1)

            os.system("cls || clear")
            self.menu()


        input("Press <Enter> to continue")
        os.system("cls || clear")
        self.menu()


if __name__ == "__main__":
    app = Main()
