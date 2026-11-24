from os import system
from rich import print

system("clear||cls")

print("[red on white]Welcome to the world. You are born![/red on white]")

print("Today you will start your journey as a [bold red underline]human[/bold red underline].")
print("")
print("First select your gender!")
print("1 [bold blue] MALE [/bold blue]")
print("2 [bold violet] FEMALE [/bold violet]")

choice_gender = input("Make a choice!: ")
if choice_gender == "1":
    print("You are[bold blue] male [/bold blue]")
elif choice_gender == "2":
    print("You are[bold violet] female [/bold violet]")

print("You have a normal childhood. Now you are in highschool. What do you want to do next?")
print("1 [bold green] go to college [/bold green]")
print("2 [bold red] stop your education and do a trait [/bold red]")

choice_education = input("Make a choice!: ")

if choice_education =="1":
    print("You start your education [bold green]at the college[/bold green]!")
    print("Now choose your major!")
    print("1 become a [bold blue]lawyer [/bold blue]")
    print("2 become a [bold red]entrepreneur [/bold red]")
    print("3 become a [bold yellow]teacher [/bold yellow]")
    choice_job_college = input("Make a choice!: ")
    if choice_job_college == "1":
            print("You are a [bold blue]laywer [/bold blue]")
    elif choice_job_college == "2":
            print("You are a [bold red]entrepreneur [/bold red]")
    elif choice_job_college == "3":
        print("You are a [bold yellow]teacher [/bold yellow]")


elif choice_education == "2":
    print("You [bold red]stop your education[/bold red] and go to a [bold red]traitschool[/bold red].")