import fire 
import click
import emoji
<<<<<<< HEAD
import sys
sys.path.append('../week7_afraa_simrun_fortune_cookie/')
from lib import fetch_value_from_db,random_no, createDB
=======
#import sys
#sys.path.append('../week7_afraa_simrun_fortune_cookie/src/main.py')
from .lib import fetch_value_from_db,random_no, createDB
>>>>>>> b41439f00d3736dda4e4cfd335aa72b0f5623174

# try:
#     import lib
# except ModuleNotFoundError:
#     sys.path.insert(1, './src')
#     import lib

@click.command()

def main():
    createDB()
    # print("\nFortune db created \n")
    randNum = random_no()
    # print("Random number Generated is: ", randNum)
    fortune_text = fetch_value_from_db(randNum)
    x = emoji.emojize(":sparkles:")
    print(f"\nYour fortune for the day is:\n{x} {fortune_text} {x}")
    print("\n")

if __name__ == "__main__":
    fire.Fire(main)