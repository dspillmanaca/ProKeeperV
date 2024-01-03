import string

lalphabet = []
lalphabet = list(string.ascii_lowercase)
ualphabet = []
ualphabet = list(string.ascii_uppercase)

def pcode(lps, ups):

    code = f"""    if len(home_ps_{lps}_var.get()) > 0 and not re.match(r'^[A-Za-z\'\s\-]+$', home_ps_{lps}_var.get()):
        home_roster_errors.append("Invalid characters in Home Player ({ups})")
    elif len(home_ps_{lps}_var.get()) > 0 and len(home_ps_{lps}_num_var.get()) == 0:
        home_roster_errors.append("No number for Home Player ({ups})")"""
    print(code)

for i in range(0,26):
    pcode(lalphabet[i], ualphabet[i])


# for item in alphabet:
#     for i in range (0,2):
#         print(item)

# for j in range (0,26):
#     for k in range (0,1):
#         print(j)

# home_roster = {
#     "Co": "a",
#     "ACo": "a",
#     "Ca": "a",
#     "CaNum": "a",
#     "ACa": "a",
#     "ACaNum": "a",
#     "LE": "a",
#     "LENum": "a",
#     "LF": "a",
#     "LFNum": "a",
#     "PSG": "a",
#     "PSGNum": "a",
#     "PSH": "a",
#     "PSHNum": "a",
#     "PSI": "a",
#     "PSINum": "a",
#     "PSJ": "a",
#     "PSJNum": "a",
#     "PSK": "a",
#     "PSKNum": "a",
#     "PSL": "a",
#     "PSLNum": "a",
#     "PSM": "a",
#     "PSMNum": "a",
#     "PSN": "a",
#     "PSNNum": "a",
#     "PSO": "a",
#     "PSONum": "a",
#     "PSP": "a",
#     "PSPNum": "a",
#     "PSQ": "a",
#     "PSQNum": "a",
#     "PSR": "a",
#     "PSRNum": "a",
#     "PSS": "a",
#     "PSSNum": "a",
#     "PST": "a",
#     "PSTNum": "a",
#     "PSU": "a",
#     "PSUNum": "a",
#     "PSV": "a",
#     "PSVNum": "a",
#     "PSW": "a",
#     "PSWNum": "a",
#     "PSX": "a",
#     "PSXNum": "a",
#     "PSY": "a",
#     "PSYNum": "a",
#     "PSZ": "a",
#     "PSZNum": "a",
# }
# for key in home_roster.keys():
#     print(key)