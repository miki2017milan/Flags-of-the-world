import pygame as py
import sys

from scr.Flashcard import Flashcard

class Assets:
    res_path: str
    GLOBE_IMG: py.surface.Surface
    UN_STATES: list[str]
    EUROPE: list[str]
    NORTH_LATIN_AMERICA: list[str]
    SOUTH_AMERICA: list[str]
    AFRICA: list[str]
    ASIA: list[str]
    OCEANIA: list[str]
    OTHER: list[str]
    TEST: list[str]

    FLAGS: dict[int | str, str | Flashcard]

    @staticmethod
    def load_set(set_name: str) -> list[str]:
        data = []

        with open(Assets.res_path + "Sets\\" + set_name, "r") as file:
           data = [line.rstrip() for line in file]

        return data
    
    @staticmethod
    def load() -> None:
        Assets.res_path = sys.path[0] + "\\res\\"

        # Images
        Assets.GLOBE_IMG = py.image.load(Assets.res_path + "Globe.png")

        # Sets
        Assets.UN_STATES = Assets.load_set("UN_States.txt")
        Assets.EUROPE = Assets.load_set("Europe.txt")
        Assets.NORTH_LATIN_AMERICA = Assets.load_set("North_Latein_America.txt")
        Assets.SOUTH_AMERICA = Assets.load_set("South_America.txt")
        Assets.AFRICA = Assets.load_set("Africa.txt")
        Assets.ASIA = Assets.load_set("Asia.txt")
        Assets.OCEANIA = Assets.load_set("Oceania.txt")
        Assets.OTHER = Assets.load_set("Other.txt")
        Assets.TEST = Assets.load_set("Test.txt")

        Assets.FLAGS = {
            0: "Abkhazia",
            1: "Afghanistan",
            2: "Albania",
            3: "Algeria",
            4: "Andorra",
            5: "Angola",
            6: "Antigua and Barbuda",
            "Argentina": Flashcard("Argentina", "Un-States"),
            8: "Armenia",
            9: "Australia",
            10: "Austria",
            11: "Azerbaijan",
            12: "Bahamas",
            13: "Bahrain",
            14: "Bangladesh",
            15: "Barbados",
            16: "Belarus",
            17: "Belgium",
            18: "Belize",
            19: "Benin",
            20: "Bhutan",
            "Bolivia": Flashcard("Bolivia", "Un-States"),
            22: "Bosnia and Herzegovina",
            23: "Botswana",
            24: "Brazil",
            25: "Brunei",
            26: "Bulgaria",
            27: "Burkina Faso",
            28: "Burundi",
            29: "Cambodia",
            30: "Cameroon",
            31: "Canada",
            32: "Cape Verde",
            33: "Central African Republic",
            34: "Chad",
            35: "Chile",
            36: "China",
            37: "Colombia",
            38: "Comoros",
            39: "Costa Rica",
            40: "Croatia",
            41: "Cuba",
            42: "Cyprus",
            43: "Czech Republic",
            44: "Democratic Republic of the Congo",
            45: "Denmark",
            46: "Djibouti",
            47: "Dominica",
            48: "Dominican Republic",
            49: "East Timor",
            50: "Ecuador",
            51: "Egypt",
            52: "El Salvador",
            53: "Equatorial Guinea",
            54: "Eritrea",
            55: "Estonia",
            56: "Eswatini",
            57: "Ethiopia",
            58: "Fiji",
            59: "Finland",
            60: "France",
            61: "Gabon",
            62: "Georgia",
            63: "Germany",
            64: "Ghana",
            65: "Greece",
            66: "Grenada",
            67: "Guatemala",
            68: "Guinea",
            69: "Guinea-Bissau",
            70: "Guyana",
            71: "Haiti",
            72: "Honduras",
            73: "Hungary",
            74: "Iceland",
            75: "India",
            76: "Indonesia",
            77: "Iran",
            78: "Iraq",
            79: "Ireland",
            80: "Israel",
            81: "Italy",
            82: "Ivory Coast",
            83: "Jamaica",
            84: "Japan",
            85: "Jordan",
            86: "Kazakhstan",
            87: "Kenya",
            88: "Kiribati",
            89: "Kosovo",
            90: "Kuwait",
            91: "Kyrgyzstan",
            92: "Laos",
            93: "Latvia",
            94: "Lebanon",
            95: "Lesotho",
            96: "Liberia",
            97: "Libya",
            98: "Liechtenstein",
            99: "Lithuania",
            100: "Luxembourg",
            101: "Madagascar",
            102: "Malawi",
            103: "Malaysia",
            104: "Maldives",
            105: "Mali",
            106: "Malta",
            107: "Marshall Islands",
            108: "Mauritania",
            109: "Mauritius",
            110: "Mexico",
            111: "Micronesia",
            112: "Moldova",
            113: "Monaco",
            114: "Mongolia",
            115: "Montenegro",
            116: "Morocco",
            117: "Mozambique",
            118: "Myanmar",
            119: "Namibia",
            120: "Nauru",
            121: "Nepal",
            122: "Netherlands",
            123: "New Zealand",
            124: "Nicaragua",
            125: "Niger",
            126: "Nigeria",
            127: "North Korea",
            128: "North Macedonia",
            129: "Northern Cyprus",
            130: "Norway",
            131: "Oman",
            132: "Pakistan",
            133: "Palau",
            134: "Palestine",
            135: "Panama",
            136: "Papua New Guinea",
            137: "Paraguay",
            138: "Peru",
            139: "Philippines",
            140: "Poland",
            141: "Portugal",
            142: "Qatar",
            143: "Republic of the Congo",
            144: "Romania",
            145: "Russia",
            146: "Rwanda",
            147: "Saint Kitts and Nevis",
            148: "Saint Lucia",
            149: "Saint Vincent and the Grenadines",
            150: "Samoa",
            151: "San Marino",
            152: "Saudi Arabia",
            153: "Senegal",
            154: "Serbia",
            155: "Seychelles",
            156: "Sierra Leone",
            157: "Singapore",
            158: "Slovakia",
            159: "Slovenia",
            160: "Solomon Islands",
            161: "Somalia",
            162: "Somaliland",
            163: "South Africa",
            164: "South Korea",
            165: "South Ossetia",
            166: "South Sudan",
            167: "Spain",
            168: "Sri Lanka",
            169: "Sudan",
            170: "Suriname",
            171: "Sweden",
            172: "Switzerland",
            173: "Syria",
            174: "São Tomé and Príncipe",
            175: "Taiwan",
            176: "Tajikistan",
            177: "Tanzania",
            178: "Thailand",
            179: "The Gambia",
            180: "Togo",
            181: "Tonga",
            182: "Transnistria",
            183: "Trinidad and Tobago",
            184: "Tunisia",
            185: "Turkey",
            186: "Turkmenistan",
            187: "Tuvalu",
            188: "Uganda",
            189: "Ukraine",
            190: "United Arab Emirates",
            191: "United Kingdom",
            192: "United States",
            193: "Uruguay",
            194: "Uzbekistan",
            195: "Vanuatu",
            196: "Vatican City",
            197: "Venezuela",
            198: "Vietnam",
            199: "Western Sahara",
            200: "Yemen",
            201: "Zambia",
            202: "Zimbabwe"
        }
        