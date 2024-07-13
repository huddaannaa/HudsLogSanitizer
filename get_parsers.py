from functions import read

# GET PARSERS FROM TXT AND ARRANGE TO DICT
indicators = {}
for n in read('parse.hud'):
    if '#' in n:pass
    else:
        try:
            parser = n.split('=')[0]
            pattern = n.split('=')[1]
            indicators[parser.strip()] = pattern.strip()
        except:pass

# ORVERRIDE AND ADD, CUSTOM INDICATORS ASIDE PARCE.HUD
# this section is not controlled by parce.hud but switches
# from the arg parser
indicators['numbers'] = "\d{4,}"
