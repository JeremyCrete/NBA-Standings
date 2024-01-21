import json
import http.client

def make_api_request(api_path, parameters=None):
    connect = http.client.HTTPSConnection("v2.nba.api-sports.io")

    headers = {
        'x-rapidapi-host': "v2.nba.api-sports.io",
        'x-rapidapi-key': "YOUR_API_KEY"  #ADD YOUR API KEY HERE
    }

    # Build the query string
    query_string = f"/{api_path}"
    if parameters:
        query_string += "?" + "&".join([f"{key}={value}" for key, value in parameters.items()])

    connect.request("GET", query_string, headers=headers)

    res = connect.getresponse()
    data = res.read()

    return data.decode("utf-8")


api_path = "standings"
parameters = {"league": "standard", "season": "2023"}  

# Used to make the API request
api_response = make_api_request(api_path, parameters)

# Process the JSON response
if api_response:
    standings_data = json.loads(api_response)
    teams = standings_data.get("response", [])

    if not teams:
        print("No team data found in the response.")
    else:
        # Separate teams into East and West conferences
        east_teams = [team for team in teams if team.get('conference', {}).get('name') == 'east']
        west_teams = [team for team in teams if team.get('conference', {}).get('name') == 'west']

        # Function to sort teams
        def custom_sort(team):
            return team.get('conference', {}).get('rank', 0)

        # Sort the teams based on confererences
        sorted_east_teams = sorted(east_teams, key=custom_sort)
        sorted_west_teams = sorted(west_teams, key=custom_sort)

        # East conference
        print("East Conference:")
        for idx, team in enumerate(sorted_east_teams, start=1):
            name = team.get('team', {}).get('name', 'N/A')
            wins = team.get('conference', {}).get('win', 'N/A')
            losses = team.get('conference', {}).get('loss', 'N/A')
            print(f"{idx}. {name} -  Wins: {wins}, Losses: {losses}")

        # West conference
        print("\nWest Conference:")
        for idx, team in enumerate(sorted_west_teams, start=1):
            name = team.get('team', {}).get('name', 'N/A')
            wins = team.get('conference', {}).get('win', 'N/A')
            losses = team.get('conference', {}).get('loss', 'N/A')
            print(f"{idx}. {name} -  Wins: {wins}, Losses: {losses}")