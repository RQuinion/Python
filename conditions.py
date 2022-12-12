import random
#conditions
if True:
    print("vrai")
    print("code exécuté")
if False:
    print("faux")
    print("code non exécuté")

condition_vente = True 
if condition_vente == True:
    print("utilisateur ok")
else: 
    print("utilisateur pas ok")

if condition_vente != True:
    print("utilisateur pas ok")

if not condition_vente:
    print("utilisateur pas ok")
else: 
    print("utilisateur ok")


emails =  random.randint(0, 3)
if emails == 1:
    print("1 mail")
elif emails > 1:
    print(f"vous avez {emails} nouveaux mails")
else:
    print("pas de mail")

windows_closed = bool(random.randint(0,1))
eclectricity_off = bool(random.randint(0,1))
print(f'{windows_closed =}')
print(f'{eclectricity_off=}')
if windows_closed and  eclectricity_off:
    print("fenêtres fermées")
    print("l'élécricité est fermée")
elif not windows_closed and eclectricity_off:
    print("fenêtres pas fermées")
    print("l'élécricité est fermée")
elif windows_closed and not eclectricity_off:
    print("fenêtres fermées")
    print("l'élécricité pas fermée")
else:
    print("fenêtres pas fermées")
    print("l'élécricité pas fermée")

bank_card = True
cash = True
print(f'{bank_card = }')
print(f'{cash = }')
if bank_card or cash:
    print("on a un moyen de paiement")
    if bank_card:
        print("on a la CB")
    if cash:
        print("on a du cash")
else:
    print("aucun moyen de paiement")

# quand on melange or et and il fait utilisr les parenthèses
ticket = bool(random.randint(0,1))
vip = bool(random.randint(0,1))
registration = bool(random.randint(0,1))
if (ticket or vip) and registration :
    print("access authorized")
else:
    print("access not authorized")

product_count = random.randint(0, 50)
if product_count > 20:
    print("+ de 20")
elif 5 < product_count <= 20:
    print("+ de 5")
elif 0 < product_count <= 5:
    print("+ de 0")
else:
    print("0")