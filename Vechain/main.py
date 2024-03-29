from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from typing import Optional
from pydantic import BaseModel
import pandas as pd
from datetime import date
# import PyCurrency_Converter
from currency_converter import CurrencyConverter
from random import choice, randint
import re
import requests
# from flask_cors import CORS

app = FastAPI()
# CORS(app)  # This enables CORS for all routes and origins

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = pd.read_csv('main_carbon_data.csv')
country_df = pd.read_csv('countries.csv')
iso_df = pd.read_csv('country-code-to-currency-code-mapping.csv')


country = {}
iso = {}
c = CurrencyConverter()


for i in range(len(country_df)):
    country[f'{country_df.iloc[i,1]}'] = country_df.iloc[i,0]
    
for i in range(len(iso_df)):
    iso[f'{iso_df.iloc[i,1]}'] = iso_df.iloc[i,3]



URL = 'https://raw.githubusercontent.com/AnotherKamila/currency-exchange-rates/master/rates.csv'
cc = CurrencyConverter(URL, ref_currency='USD')

def calculate_carbon(country_code, amount, df, country, iso, mcc):
    euro_amount = cc.convert(amount, iso[country[country_code]], 'EUR', date=date(2018, 1, 20))
    row = pd.DataFrame(df[df['MCC Code']==mcc])[country_code]
    print(euro_amount, row)
    return euro_amount * row.to_list()[0]

class TypeCountry(str, Enum):
   b1 =  'Andorra',
   b2 = 'United Arab Emirates',
   b3 = 'Afghanistan',
   b4 = 'Antigua and Barbuda',
   b5 = 'Anguilla',
   b6 = 'Albania',
   b7 = 'Armenia',
   b8 = 'Angola',
   b9 = 'Antarctica',
   b10 = 'Argentina',
   b11 = 'American Samoa',
   b12 = 'Austria',
   b13 = 'Australia',
   b14 = 'Aruba',
   b15 = 'Aland Islands',
   b16 = 'Azerbaijan',
   b17 = 'Bosnia and Herzegovina',
   b18 = 'Barbados',
   b19 = 'Bangladesh',
   b20 = 'Belgium',
   b21 = 'Burkina Faso',
   b22 = 'Bulgaria',
   b23 = 'Bahrain',
   b24 = 'Burundi',
   b25 = 'Benin',
   b26 = 'Saint Barthelemy',
   b27 = 'Bermuda',
   b28 = 'Brunei',
   b29 = 'Bolivia',
   b30 = 'Bonaire, Saint Eustatius and Saba',
   b31 = 'Brazil',
   b32 = 'Bahamas',
   b33 = 'Bhutan',
   b34 = 'Bouvet Island',
   b35 = 'Botswana',
   b36 = 'Belarus',
   b37 = 'Belize',
   b38 = 'Canada',
   b39 = 'Cocos Islands',
   b40 = 'Democratic Republic of the Congo',
   b41 = 'Central African Republic',
   b42 = 'Republic of the Congo',
   b43 = 'Switzerland',
   b44 = 'Ivory Coast',
   b45 = 'Cook Islands',
   b46 = 'Chile',
   b47 = 'Cameroon',
   b48 = 'China',
   b49 = 'Colombia',
   b50 = 'Costa Rica',
   b51 = 'Cuba',
   b52 = 'Cabo Verde',
   b53 = 'Curacao',
   b54 = 'Christmas Island',
   b55 = 'Cyprus',
   b56 = 'Czechia',
   b57 = 'Germany',
   b58 = 'Djibouti',
   b59 = 'Denmark',
   b60 = 'Dominica',
   b61 = 'Dominican Republic',
   b62 = 'Algeria',
   b63 = 'Ecuador',
   b64 = 'Estonia',
   b65 = 'Egypt',
   b66 = 'Western Sahara',
   b67 = 'Eritrea',
   b68 = 'Spain',
   b69 = 'Ethiopia',
   b70 = 'Finland',
   b71 = 'Fiji',
   b72 = 'Falkland Islands',
   b73 = 'Micronesia',
   b74 = 'Faroe Islands',
   b75 = 'France',
   b76 = 'Gabon',
   b77 = 'United Kingdom',
   b78 = 'Grenada',
   b79 = 'Georgia',
   b80 = 'French Guiana',
   b81 = 'Guernsey',
   b82 = 'Ghana',
   b83 = 'Gibraltar',
   b84 = 'Greenland',
   b85 = 'Gambia',
   b86 = 'Guinea',
   b87 = 'Guadeloupe',
   b88 = 'Equatorial Guinea',
   b89 = 'Greece',
   b90 = 'South Georgia and the South Sandwich Islands',
   b91 = 'Guatemala',
   b92 = 'Guam',
   b93 = 'Guinea-Bissau',
   b94 = 'Guyana',
   b95 = 'Hong Kong',
   b96 = 'Heard Island and McDonald Islands',
   b97 = 'Honduras',
   b98 = 'Croatia',
   b99 = 'Haiti',
   b100 = 'Hungary',
   b101 = 'Indonesia',
   b102 = 'Ireland',
   b103 = 'Israel',
   b104 = 'Isle of Man',
   b105 = 'India',
   b106 = 'British Indian Ocean Territory',
   b107 = 'Iraq',
   b108 = 'Iran',
   b109 = 'Iceland',
   b110 = 'Italy',
   b111 = 'Jersey',
   b112 = 'Jamaica',
   b113 = 'Jordan',
   b114 = 'Japan',
   b115 = 'Kenya',
   b116 = 'Kyrgyzstan',
   b117 = 'Cambodia',
   b118 = 'Kiribati',
   b119 ='Comoros',
   b120 = 'Saint Kitts and Nevis',
   b121 = 'North Korea',
   b122 = 'South Korea',
   b123 = 'Kuwait',
   b124 = 'Cayman Islands',
   b125 = 'Kazakhstan',
   b126 = 'Laos',
   b127 = 'Lebanon',
   b128 = 'Saint Lucia',
   b129 = 'Liechtenstein',
   b130 = 'Sri Lanka',
   b131 = 'Liberia',
   b132 = 'Lesotho',
   b133 = 'Lithuania',
   b134 = 'Luxembourg',
   b135 = 'Latvia',
   b136 = 'Libya',
   b137 = 'Morocco',
   b138 = 'Monaco',
   b139 = 'Moldova',
   b140 = 'Montenegro',
   b141 = 'Saint Martin',
   b142 = 'Madagascar',
   b143 = 'Marshall Islands',
   b144 = 'North Macedonia',
   b145 = 'Mali',
   b146 = 'Myanmar',
   b147 = 'Mongolia',
   b148 = 'Macao',
   b149 = 'Northern Mariana Islands',
   b150 = 'Martinique',
   b151 = 'Mauritania',
   b152 = 'Montserrat',
   b153 = 'Malta',
   b154 = 'Mauritius',
   b155 = 'Maldives',
   b156 = 'Malawi',
   b157 = 'Mexico',
   b158 = 'Malaysia',
   b159 = 'Mozambique',
   b160 = 'Namibia',
   b161 = 'New Caledonia',
   b162 = 'Niger',
   b163 = 'Norfolk Island',
   b164 = 'Nigeria',
   b165 = 'Nicaragua',
   b166 = 'Netherlands',
   b167 = 'Norway',
   b168 = 'Nepal',
   b169 = 'Nauru',
   b170 = 'Niue',
   b171 = 'New Zealand',
   b172 = 'Oman',
   b173 = 'Panama',
   b174 = 'Peru',
   b175 = 'French Polynesia',
   b176 = 'Papua New Guinea',
   b177 = 'Philippines',
   b178 = 'Pakistan',
   b179 = 'Poland',
   b180 = 'Saint Pierre and Miquelon',
   b181 = 'Pitcairn',
   b182 = 'Puerto Rico',
   b183 = 'Palestinian Territory',
   b184 = 'Portugal',
   b185 = 'Palau',
   b186 = 'Paraguay',
   b187 = 'Qatar',
   b188 = 'Reunion',
   b189 = 'Romania',
   b190 = 'Serbia',
   b191 = 'Russia',
   b192 = 'Rwanda',
   b193 = 'Saudi Arabia',
   b194 = 'Solomon Islands',
   b195 = 'Seychelles',
   b196 = 'Sudan',
   b197 = 'Sweden',
   b198 = 'Singapore',
   b199 = 'Saint Helena',
   b200 = 'Slovenia',
   b201 = 'Svalbard and Jan Mayen',
   b202 = 'Slovakia',
   b203 = 'Sierra Leone',
   b204 = 'San Marino',
   b205 = 'Senegal',
   b206 = 'Somalia',
   b207 = 'Suriname',
   b208 = 'South Sudan',
   b209 = 'Sao Tome and Principe',
   b210 = 'El Salvador',
   b211 = 'Sint Maarten',
   b212 = 'Syria',
   b213 = 'Eswatini',
   b214 = 'Turks and Caicos Islands',
   b215 = 'Chad',
   b216 = 'French Southern Territories',
   b217 = 'Togo',
   b218 = 'Thailand',
   b219 = 'Tajikistan',
   b220 = 'Tokelau',
   b221 = 'Timor Leste',
   b222 = 'Turkmenistan',
   b223 = 'Tunisia',
   b224 = 'Tonga',
   b225 = 'Turkey',
   b226 = 'Trinidad and Tobago',
   b227 = 'Tuvalu',
   b228 = 'Taiwan',
   b229 = 'Tanzania',
   b230 = 'Ukraine',
   b231 = 'Uganda',
   b232 = 'United States Minor Outlying Islands',
   b233 = 'United States',
   b234 = 'Uruguay',
   b235 = 'Uzbekistan',
   b236 = 'Vatican',
   b237 = 'Saint Vincent and the Grenadines',
   b238 = 'Venezuela',
   b239 = 'British Virgin Islands',
   b240 = 'U.S. Virgin Islands',
   b241 = 'Vietnam',
   b242 = 'Vanuatu',
   b243 = 'Wallis and Futuna',
   b244 = 'Samoa',
   b245 = 'Yemen',
   b246 = 'Mayotte',
   b247 = 'South Africa',
   b248 = 'Zambia',
   b249 = 'Zimbabwe'

class TypeMCC(str, Enum):
    string742 = '742',
    string763 = '763',
    string780 = '780',
    string1520 = '1520',
    string1711 = '1711',
    string1731 = '1731',
    string1740 = '1740',
    string1750 = '1750',
    string1761 = '1761',
    string1771 = '1771',
    string1799 = '1799',
    string2741 = '2741',
    string2791 = '2791',
    string2842 = '2842',
    string3000_3350= '3000-3350',
    string3351_3499= '3351-3499',
    string3500_3999= '3500-3999',
    string4011= '4011',
    string4111= '4111',
    string4112= '4112',
    string4119= '4119',
    string4121= '4121',
    string4131= '4131',
    string4214= '4214',
    string4215= '4215',
    string4225= '4225',
    string4411= '4411',
    string4457= '4457',
    string4468= '4468',
    string4511= '4511',
    string4582= '4582',
    string4722= '4722',
    string4723= '4723',
    string4784= '4784',
    string4789= '4789',
    string4812= '4812',
    string4813= '4813',
    string4814= '4814',
    string4816= '4816',
    string4821= '4821',
    string4829= '4829',
    string4899= '4899',
    string4900= '4900',
    string5013= '5013',
    string5021= '5021',
    string5039= '5039',
    string5044= '5044',
    string5045= '5045',
    string5046= '5046',
    string5047= '5047',
    string5051= '5051',
    string5065= '5065',
    string5072= '5072',
    string5074= '5074',
    string5085= '5085',
    string5094= '5094',
    string5099= '5099',
    string5111= '5111',
    string5122= '5122',
    string5131= '5131',
    string5137= '5137',
    string5139= '5139',
    string5169= '5169',
    string5172= '5172',
    string5192= '5192',
    string5193= '5193',
    string5198= '5198',
    string5199= '5199',
    string5200= '5200',
    string5211= '5211',
    string5231= '5231',
    string5251= '5251',
    string5261= '5261',
    string5262= '5262',
    string5271= '5271',
    string5300= '5300',
    string5309= '5309',
    string5310= '5310',
    string5311= '5311',
    string5331= '5331',
    string5399= '5399',
    string5411= '5411',
    string5422= '5422',
    string5441= '5441',
    string5451= '5451',
    string5462= '5462',
    string5499= '5499',
    string5511= '5511',
    string5521= '5521',
    string5531= '5531',
    string5532= '5532',
    string5533= '5533',
    string5541= '5541',
    string5542= '5542',
    string5551= '5551',
    string5552= '5552',
    string5561= '5561',
    string5571= '5571',
    string5592= '5592',
    string5598= '5598',
    string5599= '5599',
    string5611= '5611',
    string5621= '5621',
    string5631= '5631',
    string5641= '5641',
    string5651= '5651',
    string5655= '5655',
    string5661= '5661',
    string5681= '5681',
    string5691= '5691',
    string5697= '5697',
    string5698= '5698',
    string5699= '5699',
    string5712= '5712',
    string5713= '5713',
    string5714= '5714',
    string5718= '5718',
    string5719= '5719',
    string5722= '5722',
    string5732= '5732',
    string5733= '5733',
    string5734= '5734',
    string5735= '5735',
    string5811= '5811',
    string5812= '5812',
    string5813= '5813',
    string5814= '5814',
    string5815= '5815',
    string5816= '5816',
    string5817= '5817',
    string5818= '5818',
    string5912= '5912',
    string5921= '5921',
    string5931= '5931',
    string5932= '5932',
    string5933= '5933',
    string5935= '5935',
    string5937= '5937',
    string5940= '5940',
    string5941= '5941',
    string5942= '5942',
    string5943= '5943',
    string5944= '5944',
    string5945= '5945',
    string5946= '5946',
    string5947= '5947',
    string5948= '5948',
    string5949= '5949',
    string5950= '5950',
    string5960= '5960',
    string5962= '5962',
    string5963= '5963',
    string5964= '5964',
    string5965= '5965',
    string5966= '5966',
    string5967= '5967',
    string5968= '5968',
    string5969= '5969',
    string5970= '5970',
    string5971= '5971',
    string5972= '5972',
    string5973= '5973',
    string5975= '5975',
    string5976= '5976',
    string5977= '5977',
    string5978= '5978',
    string5983= '5983',
    string5992= '5992',
    string5993= '5993',
    string5994= '5994',
    string5995= '5995',
    string5996= '5996',
    string5997= '5997',
    string5998= '5998',
    string5999= '5999',
    string6010= '6010',
    string6011= '6011',
    string6012= '6012',
    string6050= '6050',
    string6051= '6051',
    string6211= '6211',
    string6300= '6300',
    string6513= '6513',
    string6532= '6532',
    string6533= '6533',
    string6536= '6536',
    string6537= '6537',
    string6538= '6538',
    string6540= '6540',
    string7011= '7011',
    string7012= '7012',
    string7032= '7032',
    string7033= '7033',
    string7210= '7210',
    string7211= '7211',
    string7216= '7216',
    string7217= '7217',
    string7221= '7221',
    string7230= '7230',
    string7251= '7251',
    string7261= '7261',
    string7273= '7273',
    string7276= '7276',
    string7277= '7277',
    string7278= '7278',
    string7296= '7296',
    string7297= '7297',
    string7298= '7298',
    string7299= '7299',
    string7311= '7311',
    string7321= '7321',
    string7322= '7322',
    string7333= '7333',
    string7338= '7338',
    string7339= '7339',
    string7342= '7342',
    string7349= '7349',
    string7361= '7361',
    string7372= '7372',
    string7375= '7375',
    string7379= '7379',
    string7392= '7392',
    string7393= '7393',
    string7394= '7394',
    string7395= '7395',
    string7399= '7399',
    string7512= '7512',
    string7513= '7513',
    string7523= '7523',
    string7531= '7531',
    string7534= '7534',
    string7535= '7535',
    string7538= '7538',
    string7542= '7542',
    string7549= '7549',
    string7622= '7622',
    string7623= '7623',
    string7629= '7629',
    string7631= '7631',
    string7641= '7641',
    string7692= '7692',
    string7699= '7699',
    string7800= '7800',
    string7801= '7801',
    string7802= '7802',
    string7829= '7829',
    string7832= '7832',
    string7841= '7841',
    string7911= '7911',
    string7922= '7922',
    string7929= '7929',
    string7932= '7932',
    string7933= '7933',
    string7941= '7941',
    string7991= '7991',
    string7992= '7992',
    string7993= '7993',
    string7994= '7994',
    string7995= '7995',
    string7996= '7996',
    string7997= '7997',
    string7998= '7998',
    string7999= '7999',
    string8011= '8011',
    string8021= '8021',
    string8031= '8031',
    string8041= '8041',
    string8042= '8042',
    string8043= '8043',
    string8049= '8049',
    string8050= '8050',
    string8062= '8062',
    string8071= '8071',
    string8099= '8099',
    string8111= '8111',
    string8211= '8211',
    string8220= '8220',
    string8241= '8241',
    string8244= '8244',
    string8249= '8249',
    string8299= '8299',
    string8351= '8351',
    string8398= '8398',
    string8641= '8641',
    string8651= '8651',
    string8661= '8661',
    tring8675= '8675',
    string8699= '8699',
    string8734= '8734'


class BlogModel(BaseModel):
    amount: int
    country_code: TypeCountry
    mcc: TypeMCC
    

# calculate_carbon(country_code, amount, df, country, iso, mcc)


app = FastAPI()


# Assuming your lists c_shortened and mcc are defined in this script or imported
c_shortened = [
"United States", "China", "India", "United Kingdom", "France", "Germany", "Japan", "Brazil", "Italy", "Canada", "Russia", "Australia", "Spain", "Mexico", "South Korea", "Indonesia", "Turkey", "Saudi Arabia", "Switzerland", "Netherlands", "Sweden", "United Arab Emirates", "Singapore", "Egypt", "South Africa", "Thailand", "Argentina", "Malaysia", "Nigeria", "Poland"
    # Add the rest of the countries here
]

mcc = [
"742", "763", "780", "1520", "1711", "1731", "1740", "1750", "1761", "1771", "1799", "2741", "2791", "2842", "4011", "4111", "4112", "4119", "4121", "4131", "4214", "4215", "4225", "4411", "4468", "4511", "4582", "4722", "4723", "4784", "4789", "4812", "4813", "4814", "4816", "4821", "4829", "4899", "4900", "5013", "5021", "5039", "5044", "5045", "5046", "5047"
    # "5051", "5065", "5072", "5074", "5085", "5094", "5099", "5111", "5122", "5131", "5137", "5139", "5169", "5172", "5192", "5193", "5198", "5199", "5200", "5211", "5231", "5251", "5261", "5262", "5271", "5300", "5309", "5310", "5311", "5331", "5399", "5411", "5422", "5441", "5451", "5462", "5499", "5511", "5521", "5531", "5532", "5533", "5541", "5542", "5551", "5552", "5561", "5571", "5592", "5598", "5599", "5611", "5621", "5631", "5641", "5651", "5655", "5661", "5681", "5691", "5697", "5698", "5699", "5712", "5713", "5714", "5718", "5719", "5722", "5732", "5733", "5734", "5735", "5811", "5812", "5813", "5814", "5815", "5816", "5817", "5818", "5912", "5921", "5931", "5932", "5933", "5935", "5937", "5940", "5941", "5942", "5943", "5944", "5945", "5946", "5947", "5948", "5949", "5950", "5960", "5962", "5963", "5964", "5965", "5966", "5967", "5968", "5969", "5970", "5971", "5972", "5973", "5975", "5976", "5977", "5978", "5983", "5992", "5993", "5994", "5995", "5996", "5997", "5998", "5999", "6010", "6011", "6012", "6050", "6051", "6211", "6300", "6513", "6532", "6533", "6536", "6537", "6538", "6540", "7011", "7012", "7032", "7033", "7210", "7211", "7216", "7217", "7221", "7230", "7251", "7261", "7273", "7276", "7277", "7278", "7296", "7297", "7298", "7299", "7311", "7321", "7322", "7333", "7338", "7339", "7342", "7349", "7361", "7372", "7375", "7379", "7392", "7393", "7394", "7395", "7399", "7512", "7513", "7523", "7531", "7534", "7535", "7538", "7542", "7549", "7622", "7623", "7629", "7631", "7641", "7692", "7699", "7800", "7801", "7802", "7829", "7832", "7841", "7911", "7922", "7929", "7932", "7933", "7941", "7991", "7992", "7993", "7994", "7995", "7996", "7997", "7998", "7999", "8011", "8021", "8031", "8041", "8042", "8043", "8049", "8050", "8062", "8071", "8099", "8111", "8211", "8220", "8241", "8244", "8249", "8299", "8351", "8398", "8641", "8651", "8661", "8675", "8699", "8734"
    # Add the rest of the MCC values here
]

def process_text(input_text):
    # Simplified country names dictionary for demonstration
    country_names = {
        'Andorra': 'AD', 'United Arab Emirates': 'AE', 'Afghanistan': 'AF',
        # Add other countries as necessary...
    }

    # Convert the dictionary keys to a big regex pattern
    country_names_pattern = r'\b(' + '|'.join(re.escape(key) for key in country_names.keys()) + r')\b'

    # Regular expressions for amount and MCC
    amount_pattern = r"\b\d+(\.\d+)?\b"
    mcc_pattern = r"\b\d{4}\b"

    # Search for country names, amounts, and MCCs in the input text
    country_match = re.search(country_names_pattern, input_text, re.IGNORECASE)
    amount_matches = re.findall(amount_pattern, input_text)
    mcc_matches = re.findall(mcc_pattern, input_text)

    country_code = country_names[country_match.group()] if country_match else None
    amount = float(amount_matches[0]) if amount_matches else None
    mcc = mcc_matches[0] if mcc_matches else None

    return {
        "countryCode": country_code,
        "amount": amount,
        "mcc": mcc
    }

# Example usage
input_text = "The transaction was made in Andorra for an amount of 100.50 with MCC 5411."
result = process_text(input_text)
print(result)

@app.get("/random-data/{n}")
def get_random_data(n:int):
    l = [] 
    for i in range(n):
        random_country = choice(c_shortened)
        random_mcc = choice(mcc)
        random_amount = randint(1, 100)
        l.append({"country": random_country, "MCC": random_mcc, "amount": random_amount})
    return l

@app.get("/")
async def root():
    return {"message": "Hello there"}


@app.get("/blogs/all")
def get_all_blogs():
    return {"message": "all blogs "}


@app.get("/blogs/{id}")
def get_blogs(id:int):
    return {"message": f"blogs {id}"}


@app.get("/type/{country_code}")
def get_blogs(country_code:Optional[TypeCountry]='Andorra', amount:Optional[str]=10, mcc:Optional[TypeMCC]=2):
    return {calculate_carbon(country_code, amount, data, country, iso, mcc)}




@app.get("/image-search/{name}")
def get_random_data(name:str):
    query = name

    r = requests.get("https://api.qwant.com/v3/search/images",
        params={
            'count': 5,
            'q': query,
            't': 'images',
            'safesearch': 1,
            'locale': 'en_US',
            'offset': 0,
            'device': 'desktop'
        },
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
    )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response][0]


    return urls





# @app.get('/blogs')
# def get_blog(request: BlogModel):
#     return {"message": "blog post successfully stored",
#             "amount": request.amount,
#             "country_code": request.country_code,
#             "mcc": request.mcc}
