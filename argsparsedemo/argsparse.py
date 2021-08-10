# standard, don't need to install!
import argparse
# this object will hold all arguments the user passes in
parser_mcgee= argparse.ArgumentParser(description="Enter your favorite Pokemon.")
# acceptable values
acc_adj= ["Pikachu"]
# add some arguments!
parser_mcgee.add_argument("adj", choices=acc_adj, help="Your favorite pokemon.")
# add an optional argument
parser_mcgee.add_argument("-a", metavar="ADVERB", default="so", help="'Helper' words, like 'really, very, extremely', etc.")
# have the parser obj turn all those arguments into variables
arglebargle= parser_mcgee.parse_args()
print(f"Your favorite Pokemon is {arglebargle.a} {arglebargle.adj}!")
