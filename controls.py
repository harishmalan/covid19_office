# flake8: noqa

# In[]:
# Controls for webapp
COUNTIES = {
    "001": "Albany",
    "003": "Allegany",
    "005": "Bronx",
    "007": "Broome",
    "009": "Cattaraugus",
    "011": "Cayuga",
    "013": "Chautauqua",
    "015": "Chemung",
    "017": "Chenango",
    "019": "Clinton",
    "021": "Columbia",
    "023": "Cortland",
    "025": "Delaware",
    "027": "Dutchess",
    "029": "Erie",
    "031": "Essex",
    "033": "Franklin",
    "035": "Fulton",
    "037": "Genesee",
    "039": "Greene",
    "041": "Hamilton",
    "043": "Herkimer",
    "045": "Jefferson",
    "047": "Kings",
    "049": "Lewis",
    "051": "Livingston",
    "053": "Madison",
    "055": "Monroe",
    "057": "Montgomery",
    "059": "Nassau",
    "061": "New York",
    "063": "Niagara",
    "065": "Oneida",
    "067": "Onondaga",
    "069": "Ontario",
    "071": "Orange",
    "073": "Orleans",
    "075": "Oswego",
    "077": "Otsego",
    "079": "Putnam",
    "081": "Queens",
    "083": "Rensselaer",
    "085": "Richmond",
    "087": "Rockland",
    "089": "St. Lawrence",
    "091": "Saratoga",
    "093": "Schenectady",
    "095": "Schoharie",
    "097": "Schuyler",
    "099": "Seneca",
    "101": "Steuben",
    "103": "Suffolk",
    "105": "Sullivan",
    "107": "Tioga",
    "109": "Tompkins",
    "111": "Ulster",
    "113": "Warren",
    "115": "Washington",
    "117": "Wayne",
    "119": "Westchester",
    "121": "Wyoming",
    "123": "Yates",
}

WELL_STATUSES = dict(
    AC="Active",
    AR="Application Received to Drill/Plug/Convert",
    CA="Cancelled",
    DC="Drilling Completed",
    DD="Drilled Deeper",
    DG="Drilling in Progress",
    EX="Expired Permit",
    IN="Inactive",
    NR="Not Reported on AWR",
    PA="Plugged and Abandoned",
    PI="Permit Issued",
    PB="Plugged Back",
    PM="Plugged Back Multilateral",
    RE="Refunded Fee",
    RW="Released - Water Well",
    SI="Shut-In",
    TA="Temporarily Abandoned",
    TR="Transferred Permit",
    UN="Unknown",
    UL="Unknown Located",
    UM="Unknown Not Found",
    VP="Voided Permit",
)

WELL_TYPES = dict(
    BR="Brine",
    Confidential="Confidential",
    DH="Dry Hole",
    DS="Disposal",
    DW="Dry Wildcat",
    GD="Gas Development",
    GE="Gas Extension",
    GW="Gas Wildcat",
    IG="Gas Injection",
    IW="Oil Injection",
    LP="Liquefied Petroleum Gas Storage",
    MB="Monitoring Brine",
    MM="Monitoring Miscellaneous",
    MS="Monitoring Storage",
    NL="Not Listed",
    OB="Observation Well",
    OD="Oil Development",
    OE="Oil Extension",
    OW="Oil Wildcat",
    SG="Stratigraphic",
    ST="Storage",
    TH="Geothermal",
    UN="Unknown",
)

WELL_COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)
COUNTIES_ISO ={
'Afghanistan': 'AF',
 'Albania': 'AL',
 'Algeria': 'DZ',
 'American Samoa': 'AS',
 'Andorra': 'AD',
 'Angola': 'AO',
 'Anguilla': 'AI',
 'Antarctica': 'AQ',
 'Antigua and Barbuda': 'AG',
 'Argentina': 'AR',
 'Armenia': 'AM',
 'Aruba': 'AW',
 'Australia': 'AU',
 'Austria': 'AT',
 'Azerbaijan': 'AZ',
 'Bahamas': 'BS',
 'Bahrain': 'BH',
 'Bangladesh': 'BD',
 'Barbados': 'BB',
 'Belarus': 'BY',
 'Belgium': 'BE',
 'Belize': 'BZ',
 'Benin': 'BJ',
 'Bermuda': 'BM',
 'Bhutan': 'BT',
 'Bolivia, Plurinational State of': 'BO',
 'Bonaire, Sint Eustatius and Saba': 'BQ',
 'Bosnia and Herzegovina': 'BA',
 'Botswana': 'BW',
 'Bouvet Island': 'BV',
 'Brazil': 'BR',
 'British Indian Ocean Territory': 'IO',
 'Brunei Darussalam': 'BN',
 'Bulgaria': 'BG',
 'Burkina Faso': 'BF',
 'Burundi': 'BI',
 'Cambodia': 'KH',
 'Cameroon': 'CM',
 'Canada': 'CA',
 'Cape Verde': 'CV',
 'Cayman Islands': 'KY',
 'Central African Republic': 'CF',
 'Chad': 'TD',
 'Chile': 'CL',
 'China': 'CN',
 'Christmas Island': 'CX',
 'Cocos (Keeling) Islands': 'CC',
 'Colombia': 'CO',
 'Comoros': 'KM',
 'Congo': 'CG',
 'Congo, the Democratic Republic of the': 'CD',
 'Cook Islands': 'CK',
 'Costa Rica': 'CR',
 'Country name': 'Code',
 'Croatia': 'HR',
 'Cuba': 'CU',
 'Curaçao': 'CW',
 'Cyprus': 'CY',
 'Czech Republic': 'CZ',
 "Côte d'Ivoire": 'CI',
 'Denmark': 'DK',
 'Djibouti': 'DJ',
 'Dominica': 'DM',
 'Dominican Republic': 'DO',
 'Ecuador': 'EC',
 'Egypt': 'EG',
 'El Salvador': 'SV',
 'Equatorial Guinea': 'GQ',
 'Eritrea': 'ER',
 'Estonia': 'EE',
 'Ethiopia': 'ET',
 'Falkland Islands (Malvinas)': 'FK',
 'Faroe Islands': 'FO',
 'Fiji': 'FJ',
 'Finland': 'FI',
 'France': 'FR',
 'French Guiana': 'GF',
 'French Polynesia': 'PF',
 'French Southern Territories': 'TF',
 'Gabon': 'GA',
 'Gambia': 'GM',
 'Georgia': 'GE',
 'Germany': 'DE',
 'Ghana': 'GH',
 'Gibraltar': 'GI',
 'Greece': 'GR',
 'Greenland': 'GL',
 'Grenada': 'GD',
 'Guadeloupe': 'GP',
 'Guam': 'GU',
 'Guatemala': 'GT',
 'Guernsey': 'GG',
 'Guinea': 'GN',
 'Guinea-Bissau': 'GW',
 'Guyana': 'GY',
 'Haiti': 'HT',
 'Heard Island and McDonald Islands': 'HM',
 'Holy See (Vatican City State)': 'VA',
 'Honduras': 'HN',
 'Hong Kong': 'HK',
 'Hungary': 'HU',
 'ISO 3166-2:GB': '(.uk)',
 'Iceland': 'IS',
 'India': 'IN',
 'Indonesia': 'ID',
 'Iran, Islamic Republic of': 'IR',
 'Iraq': 'IQ',
 'Ireland': 'IE',
 'Isle of Man': 'IM',
 'Israel': 'IL',
 'Italy': 'IT',
 'Jamaica': 'JM',
 'Japan': 'JP',
 'Jersey': 'JE',
 'Jordan': 'JO',
 'Kazakhstan': 'KZ',
 'Kenya': 'KE',
 'Kiribati': 'KI',
 "Korea, Democratic People's Republic of": 'KP',
 'Korea, Republic of': 'KR',
 'Kuwait': 'KW',
 'Kyrgyzstan': 'KG',
 "Lao People's Democratic Republic": 'LA',
 'Latvia': 'LV',
 'Lebanon': 'LB',
 'Lesotho': 'LS',
 'Liberia': 'LR',
 'Libya': 'LY',
 'Liechtenstein': 'LI',
 'Lithuania': 'LT',
 'Luxembourg': 'LU',
 'Macao': 'MO',
 'Macedonia, the former Yugoslav Republic of': 'MK',
 'Madagascar': 'MG',
 'Malawi': 'MW',
 'Malaysia': 'MY',
 'Maldives': 'MV',
 'Mali': 'ML',
 'Malta': 'MT',
 'Marshall Islands': 'MH',
 'Martinique': 'MQ',
 'Mauritania': 'MR',
 'Mauritius': 'MU',
 'Mayotte': 'YT',
 'Mexico': 'MX',
 'Micronesia, Federated States of': 'FM',
 'Moldova, Republic of': 'MD',
 'Monaco': 'MC',
 'Mongolia': 'MN',
 'Montenegro': 'ME',
 'Montserrat': 'MS',
 'Morocco': 'MA',
 'Mozambique': 'MZ',
 'Myanmar': 'MM',
 'Namibia': 'NA',
 'Nauru': 'NR',
 'Nepal': 'NP',
 'Netherlands': 'NL',
 'New Caledonia': 'NC',
 'New Zealand': 'NZ',
 'Nicaragua': 'NI',
 'Niger': 'NE',
 'Nigeria': 'NG',
 'Niue': 'NU',
 'Norfolk Island': 'NF',
 'Northern Mariana Islands': 'MP',
 'Norway': 'NO',
 'Oman': 'OM',
 'Pakistan': 'PK',
 'Palau': 'PW',
 'Palestine, State of': 'PS',
 'Panama': 'PA',
 'Papua New Guinea': 'PG',
 'Paraguay': 'PY',
 'Peru': 'PE',
 'Philippines': 'PH',
 'Pitcairn': 'PN',
 'Poland': 'PL',
 'Portugal': 'PT',
 'Puerto Rico': 'PR',
 'Qatar': 'QA',
 'Romania': 'RO',
 'Russian Federation': 'RU',
 'Rwanda': 'RW',
 'Réunion': 'RE',
 'Saint Barthélemy': 'BL',
 'Saint Helena, Ascension and Tristan da Cunha': 'SH',
 'Saint Kitts and Nevis': 'KN',
 'Saint Lucia': 'LC',
 'Saint Martin (French part)': 'MF',
 'Saint Pierre and Miquelon': 'PM',
 'Saint Vincent and the Grenadines': 'VC',
 'Samoa': 'WS',
 'San Marino': 'SM',
 'Sao Tome and Principe': 'ST',
 'Saudi Arabia': 'SA',
 'Senegal': 'SN',
 'Serbia': 'RS',
 'Seychelles': 'SC',
 'Sierra Leone': 'SL',
 'Singapore': 'SG',
 'Sint Maarten (Dutch part)': 'SX',
 'Slovakia': 'SK',
 'Slovenia': 'SI',
 'Solomon Islands': 'SB',
 'Somalia': 'SO',
 'South Africa': 'ZA',
 'South Georgia and the South Sandwich Islands': 'GS',
 'South Sudan': 'SS',
 'Spain': 'ES',
 'Sri Lanka': 'LK',
 'Sudan': 'SD',
 'Suriname': 'SR',
 'Svalbard and Jan Mayen': 'SJ',
 'Swaziland': 'SZ',
 'Sweden': 'SE',
 'Switzerland': 'CH',
 'Syrian Arab Republic': 'SY',
 'Taiwan, Province of China': 'TW',
 'Tajikistan': 'TJ',
 'Tanzania, United Republic of': 'TZ',
 'Thailand': 'TH',
 'Timor-Leste': 'TL',
 'Togo': 'TG',
 'Tokelau': 'TK',
 'Tonga': 'TO',
 'Trinidad and Tobago': 'TT',
 'Tunisia': 'TN',
 'Turkey': 'TR',
 'Turkmenistan': 'TM',
 'Turks and Caicos Islands': 'TC',
 'Tuvalu': 'TV',
 'Uganda': 'UG',
 'Ukraine': 'UA',
 'United Arab Emirates': 'AE',
 'United Kingdom': 'GB',
 'United States': 'US',
 'United States Minor Outlying Islands': 'UM',
 'Uruguay': 'UY',
 'Uzbekistan': 'UZ',
 'Vanuatu': 'VU',
 'Venezuela, Bolivarian Republic of': 'VE',
 'Viet Nam': 'VN',
 'Virgin Islands, British': 'VG',
 'Virgin Islands, U.S.': 'VI',
 'Wallis and Futuna': 'WF',
 'Western Sahara': 'EH',
 'Yemen': 'YE',
 'Zambia': 'ZM',
 'Zimbabwe': 'ZW',
 'Åland Islands': 'AX'
}