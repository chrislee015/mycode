#!/usr/bin/env python3
user_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)")
user_char = input("What statistic do you want to know about? (real name, powers, archenemy)")

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"She-Hulk":
  {"real name": "jennifer walters",
  "powers": "super strength & intelligence",
  "archenemy": "Titania"}
             }
result = marvelchars[user_name].user_char
cName = char_name.title()
cPower = user_char.lower()
print(f"{char_name}'s {char_stat} is: {result}")


