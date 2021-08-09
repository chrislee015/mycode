#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    start_date = input("Enter a start date in YYYY-MM-DD format:")
    startdate = "start_date=" + start_date

    end_date = input("Enter an end date in YYYY-MM-DD format:")
    enddate = "end_date=" + end_date

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata["element_count"])
    danger = 0
    for e in neodata["near_earth_objects"]:
        for x in neodata["near_earth_objects"][e]:
            #for y in x:
                if x["is_potentially_hazardous_asteroid"] == True:
                    danger += 1

    
    print(danger)


if __name__ == "__main__":
    main()

