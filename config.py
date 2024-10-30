import os
import re

my_name = "Fred Li"
# One sentence bio means how you would introduce yourself before submitting a query to ChatGPT
one_sentence_bio = "I am a top student in Quantitative Finance at Washington University in St. Louis with a GPA of 3.95/4.00"

# Store your Notion page ID here
page_id = ""
# Store your ChatGPT API key here
api_key = ""
# Store your Notion API key here
notion_api_key = ""
# Store your Google Maps API key here
gmap_api_key = ""


# Store your Notion website URL here
website = f"https://fredhl.notion.site/Fred-H-Li-{page_id}"

# System used
if re.match(r"^[A-Za-z]\:", os.getcwd()):
    system_used = "Windows"
elif re.match(r"^/Users", os.getcwd()):
    system_used = "Mac"

# root is the folder that you store your CV and outputs
root = "./"
download_folder = f"{root}/Cover Letter"
cv_folder = f"{root}/CV"
package_folder = f"{root}/Package"

# Chromedriver path
binary_location = "C:/Program Files/chrome-win32/chrome.exe" if system_used == "Windows" else "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
path_to_chromedriver = 'D:/Dropbox/Downloads/tools/chrome-win-x64/chromedriver' if system_used == "Windows" else '/Users/fred/Downloads/tools/chromedriver-mac-arm64/chromedriver'

# CV Data
# CV1: CV for Trader, Quant and Data Roles
cv_trader_quant_data = """

"""
# CV2: CV for Research Roles
cv_research = """

"""
# CV3: CV for Equity Research Roles
cv_equity_research = """

"""
# CV4: CV for Pan Finance Roles
cv_pan_finance = """


"""
# CV5: CV for IBD Roles
cv_ibd = """

"""
# CV6: CV for Operation Roles
cv_operation = """


"""
# CV7: CV for Risk Roles
cv_risk = """

"""

cv_dict = {
    "trader_quant_data": cv_trader_quant_data,
    "research": cv_research,
    "equity_research": cv_equity_research,
    "pan_finance": cv_pan_finance,
    "ibd": cv_ibd,
    "operation": cv_operation,
    "risk": cv_risk,
}

cv_location_dict = {
    "trader_quant_data": "trader.pdf",
    "research": "research.pdf",
    "equity_research": "equity research.pdf",
    "pan_finance": "pan-finance.pdf",
    "ibd": "ibd.pdf",
    "operation": "operation.pdf",
    "risk": "risk.pdf",
}

us_state_dict = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
}

ca_province_dict = {
    "AB": "Alberta",
    "BC": "British Columbia",
    "MB": "Manitoba",
    "NB": "New Brunswick",
    "NL": "Newfoundland and Labrador",
    "NS": "Nova Scotia",
    "NT": "Northwest Territories",
    "NU": "Nunavut",
    "ON": "Ontario",
    "PE": "Prince Edward Island",
    "QC": "Quebec",
    "SK": "Saskatchewan",
    "YT": "Yukon",
}
