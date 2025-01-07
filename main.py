import os
import time

import rich

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
            rich.print(f"Searching info about [blue]`{self.email}`[/blue]...\n")

            time.sleep(1)

            rich.print("Checking [bold]github.com...[/bold]")
            email_checker.github(
                email = self.email
            )
            print("\n")

            rich.print("Checking [bold]pinterest.com...[/bold]")
            email_checker.pinterest(
                email = self.email
            )
            print("\n")

            rich.print("Checking [bold]spotify.com...[/bold]")
            email_checker.spotify(
                email = self.email
            )
            print("\n")

            rich.print("Checking [bold]twitter.com...[/bold]")
            email_checker.twitter(
                email = self.email
            )
            print("\n")

            rich.print("Checking [bold]chess.com...[/bold]")
            email_checker.chess(
                email = self.email
            )
            print("\n")
        else:
            rich.print("[red]Missing value![/red]")

            time.sleep(1)

            os.system("cls || clear")
            self.menu()


        input("Press <Enter> to continue")
        os.system("cls || clear")
        self.menu()

    def check_phone(self):
        self.phone = input("Enter phone number\n: ")
        print("\n")

        if len(self.phone) > 0:
            rich.print(f"Searching info about [blue]`{self.phone}`[/blue]...\n")

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
            rich.print(f"Searching info about [blue]`{self.ip}`[/blue]...\n")

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
