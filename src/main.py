from lib import fetch_value_from_db,random_no, createDB
import fire 
import click

@click.command()
@click.option()

def main():
    createDB()
    print("\nFortune db created \n")
    randNum = random_no()
    print("Random number Generated is: ", randNum)
    fortune_text = fetch_value_from_db(randNum)
    print("\nDecrypted Fortune is: ", fortune_text)
    print("\n")

if __name__ == "__main__":
    fire.Fire(main)