# NBA-Standings
## Usage

1. Download the script file.

2. Open the terminal and navigate to the directory where you saved the script.

3. Open the script file in a text editor and update the API key in the `headers` dictionary with your own RapidAPI key. You can get your key by following the steps in the authentication section: https://api-sports.io/documentation/basketball/v1 

   ```python
   headers = {
       'x-rapidapi-host': "v2.nba.api-sports.io",
       'x-rapidapi-key': "YOUR_RAPIDAPI_KEY_HERE"
   }
   ```

4. Run the script by executing the following command in the terminal:

   ```bash
   python your_script_filename.py
   ```
   or if you are running python3
   ```bash
   python3 your_script_filename.py
   ```

6. The script will make an API request to retrieve NBA standings data for the specified season (update the `season` parameter if needed) and display the results in a structured format.
