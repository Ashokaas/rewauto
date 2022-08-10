# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# ---- IMPORTATION DES LIBRAIRIES ----
# ____________________________________


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from time import sleep
from random import randint
import pyautogui
from win10toast import ToastNotifier
from playsound import playsound
import traceback
from login_ui import login_ui





# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# ---- EMAIL, MDP, LISTE ANIMAUX ----
# ____________________________________


email, mdp = login_ui()


liste_recherches = ['Canida', 'Felida', 'Ca', 'Cattl', 'Do', 'Donke', 'Goa', 'Guinea pi', 'Hors', 'Pi', 'Rabbi', 'Fancy rat varietie', 'laboratory rat strain', 'Sheep breed', 'Water buffalo breed', 'Chicken breed', 'Duck breed', 'Goose breed', 'Pigeon breed', 'Turkey breed', 'Aardvar', 'Aardwol', 'African buffal', 'African elephan', 'African leopar', 'Albatros', 'Alligato', 'Alpac', 'American buffalo (bison', 'American robi', 'Amphibia', 'lis', 'Anacond', 'Angelfis', 'Anglerfis', 'An', 'Anteate', 'Antelop', 'Antlio', 'Ap', 'Aphi', 'Arabian leopar', 'Arctic Fo', 'Arctic Wol', 'Armadill', 'Arrow cra', 'As', 'Ass (donkey', 'Baboo', 'Badge', 'Bald eagl', 'Bandicoo', 'Barnacl', 'Barracud', 'Basilis', 'Bas', 'Ba', 'Beaked whal', 'Bea', 'lis', 'Beave', 'Bedbu', 'Be', 'Beetl', 'Bir', 'lis', 'Biso', 'Blackbir', 'Black panthe', 'Black widow spide', 'Blue bir', 'Blue ja', 'Blue whal', 'Bo', 'Boa', 'Bobca', 'Bobolin', 'Bonob', 'Boob', 'Box jellyfis', 'Bovi', 'Buffalo, Africa', 'Buffalo, American (bison', 'Bu', 'Butterfl', 'Buzzar', 'Came', 'Cani', 'Cape buffal', 'Capybar', 'Cardina', 'Caribo', 'Car', 'Ca', 'lis', 'Catshar', 'Caterpilla', 'Catfis', 'Cattl', 'lis', 'Centiped', 'Cephalopo', 'Chameleo', 'Cheeta', 'Chickade', 'Chicke', 'lis', 'Chimpanze', 'Chinchill', 'Chipmun', 'Cla', 'Clownfis', 'Cobr', 'Cockroac', 'Co', 'Condo', 'Constricto', 'Cora', 'Couga', 'Co', 'Coyot', 'Cra', 'Cran', 'Crane fl', 'Crawda', 'Crayfis', 'Cricke', 'Crocodil', 'Cro', 'Cucko', 'Cicad', 'Damselfl', 'Dee', 'Ding', 'Dinosau', 'lis', 'Do', 'lis', 'Dolphi', 'Donke', 'lis', 'Dormous', 'Dov', 'Dragonfl', 'Drago', 'Duc', 'lis', 'Dung beetl', 'Eagl', 'Earthwor', 'Earwi', 'Echidn', 'Ee', 'Egre', 'Elephan', 'Elephant sea', 'El', 'Em', 'English pointe', 'Ermin', 'Falco', 'Ferre', 'Finc', 'Firefl', 'Fis', 'Flaming', 'Fle', 'Fl', 'Flyingfis', 'Fow', 'Fo', 'Fro', 'Fruit ba', 'Gamefow', 'lis', 'Gallifor', 'lis', 'Gazell', 'Geck', 'Gerbi', 'Giant pand', 'Giant squi', 'Gibbo', 'Gila monste', 'Giraff', 'Goa', 'lis', 'Goldfis', 'Goos', 'lis', 'Gophe', 'Gorill', 'Grasshoppe', 'Great blue hero', 'Great white shar', 'Grizzly bea', 'Ground shar', 'Ground slot', 'Grous', 'Gua', 'lis', 'Guanac', 'Guineafow', 'lis', 'Guinea pi', 'lis', 'Gul', 'Gupp', 'Haddoc', 'Halibu', 'Hammerhead shar', 'Hamste', 'Har', 'Harrie', 'Haw', 'Hedgeho', 'Hermit cra', 'Hero', 'Herrin', 'Hippopotamu', 'Hookwor', 'Horne', 'Hors', 'lis', 'Hoverfl', 'Hummingbir', 'Humpback whal', 'Hyen', 'Iguan', 'Impal', 'Irukandji jellyfis', 'Jacka', 'Jagua', 'Ja', 'Jellyfis', 'Junglefow', 'Kangaro', 'Kangaroo mous', 'Kangaroo ra', 'Kingfishe', 'Kit', 'Kiw', 'Koal', 'Ko', 'Komodo drago', 'Kril', 'Ladybu', 'Lampre', 'Landfow', 'Land snai', 'Lar', 'Leec', 'Lemmin', 'Lemu', 'Leopar', 'Leopo', 'Limpe', 'Lio', 'Lizar', 'Llam', 'Lobste', 'Locus', 'Loo', 'Lous', 'Lungfis', 'Lyn', 'Maca', 'Mackere', 'Magpi', 'Mamma', 'Manate', 'Mandril', 'Manta ra', 'Marli', 'Marmose', 'Marmo', 'Marsupia', 'Marte', 'Mastodo', 'Meadowlar', 'Meerka', 'Min', 'Minno', 'Mit', 'Mockingbir', 'Mol', 'Mollus', 'Mongoos', 'Monitor lizar', 'Monke', 'Moos', 'Mosquit', 'Mot', 'Mountain goa', 'Mous', 'Mul', 'Musko', 'Narwha', 'New', 'New World quai', 'Nightingal', 'Ocelo', 'Octopu', 'Old World quai', 'Opossu', 'Oranguta', 'Orc', 'Ostric', 'Otte', 'Ow', 'O', 'Pand', 'Panthe', 'Panthera hybri', 'Parakee', 'Parro', 'Parrotfis', 'Partridg', 'Peacoc', 'Peafow', 'Pelica', 'Pengui', 'Perc', 'Peregrine falco', 'Pheasan', 'Pi', 'Pigeo', 'lis', 'Pik', 'Pilot whal', 'Pinnipe', 'Piranh', 'Planaria', 'Platypu', 'Polar bea', 'Pon', 'Porcupin', 'Porpois', "Portuguese man o' wa", 'Possu', 'Prairie do', 'Praw', 'Praying manti', 'Primat', 'Ptarmiga', 'Puffi', 'Pum', 'Pytho', 'Quai', 'Quele', 'Quokk', 'Rabbi', 'lis', 'Raccoo', 'Rainbow trou', 'Ra', 'Rattlesnak', 'Rave', 'Ray (Batoidea', 'Ray (Rajiformes', 'Red pand', 'Reindee', 'Reptil', 'Rhinocero', 'Right whal', 'Roadrunne', 'Roden', 'Roo', 'Rooste', 'Roundwor', 'Saber-toothed ca', 'Sailfis', 'Salamande', 'Salmo', 'Sawfis', 'Scale insec', 'Scallo', 'Scorpio', 'Seahors', 'Sea lio', 'Sea slu', 'Sea snai', 'Shar', 'lis', 'Shee', 'lis', 'Shre', 'Shrim', 'Silkwor', 'Silverfis', 'Skin', 'Skun', 'Slot', 'Slu', 'Smel', 'Snai', 'Snak', 'lis', 'Snip', 'Snow leopar', 'Sockeye salmo', 'Sol', 'Sparro', 'Sperm whal', 'Spide', 'Spider monke', 'Spoonbil', 'Squi', 'Squirre', 'Starfis', 'Star-nosed mol', 'Steelhead trou', 'Stingra', 'Stoa', 'Stor', 'Sturgeo', 'Sugar glide', 'Swallo', 'Swa', 'Swif', 'Swordfis', 'Swordtai', 'Tah', 'Taki', 'Tapi', 'Tarantul', 'Tarsie', 'Tasmanian devi', 'Termit', 'Ter', 'Thrus', 'Tic', 'Tige', 'Tiger shar', 'Tiglo', 'Toa', 'Tortois', 'Touca', 'Trapdoor spide', 'Tree fro', 'Trou', 'Tun', 'Turke', 'lis', 'Turtl', 'Tyrannosauru', 'Uria', 'Vampire ba', 'Vampire squi', 'Vicun', 'Vipe', 'Vol', 'Vultur', 'Wallab', 'Walru', 'Was', 'Warble', 'Water Bo', 'Water buffal', 'Wease', 'Whal', 'Whippe', 'Whitefis', 'Whooping cran', 'Wildca', 'Wildebees', 'Wildfow', 'Wol', 'Wolverin', 'Womba', 'Woodpecke', 'Wor', 'Wre', 'Xerina', 'X-ray fis', 'Ya', 'Yellow perc', 'Zebr', 'Zebra finc', 'Animals by number of neuron', 'Animals by siz', 'Common household pest', 'Common names of poisonous animal', 'Alpac', 'Bali cattl', 'Ca', 'Cattl', 'Chicke', 'Do', 'Domestic Bactrian came', 'Domestic canar', 'Domestic dromedary came', 'Domestic duc', 'Domestic goa', 'Domestic goos', 'Domestic guineafow', 'Domestic hedgeho', 'Domestic pi', 'Domestic pigeo', 'Domestic rabbi', 'Domestic silkmot', 'Domestic silver fo', 'Domestic turke', 'Donke', 'Fancy mous', 'Fancy ra', 'Lab ra', 'Ferre', 'Gaya', 'Goldfis', 'Guinea pi', 'Gupp', 'Hors', 'Ko', 'Llam', 'Ringneck dov', 'Shee', 'Siamese fighting fis', 'Society finc', 'Ya']


driver = webdriver.Chrome(executable_path='chromedriver.exe')



# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# ------------ FONCTIONS ------------
# ____________________________________



# Vérifie si la tâche a déjà été effectué

def is_check(element:str):
    if element == "mee-icon mee-icon-AddMedium":
        return False
    elif element == "mee-icon mee-icon-SkypeCircleCheck":
        return True
# ________________________________________________________



# Définit le type de tâche

def what_type(element:str):
    if 'quiz' in element.lower():
        return 'quiz'
    elif 'sondage' in element.lower():
        return 'sondage'
    elif 'Ceci ou cela?' == element:
        return 'ceci_cela_quiz'
    else:
        return 'normal_link'
# ________________________________________________________



# Effectue un raccourci

def raccourci(touches:list):
    for touche in touches:
        pyautogui.keyDown(touche)
    for touche in touches:
        pyautogui.keyUp(touche)
# ________________________________________________________



# Change l'url de la page

def changer_url(url:str):
    raccourci(['ctrl', 'l'])
    pyautogui.press('backspace')
    pyautogui.write(url)
    pyautogui.press('enter')
# ________________________________________________________

def mobile(enabled=True):
    if enabled:
        set_device_metrics_override = dict({
            "width": 375,
            "height": 812,
            "deviceScaleFactor": 50,
            "mobile": True
        })
    else:
        set_device_metrics_override = dict({
            "width": 0,
            "height": 0,
            "deviceScaleFactor": 0,
            "mobile": False
        })
    driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', set_device_metrics_override)

# ________________________________________________________

# Effectue les recherches pc et téléphone

def recherches(nb_pc:int=40, nb_tel:int=30, liste_recherches:list=['banane', 'oui']):
    # -- RECHERCHES

        # Recherches PC
    for pc in range(nb_pc):
        driver.get(f'https://bing.com/search?q={liste_recherches[randint(0, len(liste_recherches)-1)]}')
        pause_pour_veski_le_bot(tps_en_moins=2)

        # Recherches Téléphone
    if nb_tel > 0:
        mobile()

        for tel in range(nb_tel):
            driver.get(f'https://bing.com/search?q={liste_recherches[randint(0, len(liste_recherches)-1)]}')
            pause_pour_veski_le_bot(tps_en_moins=2)

        mobile(False)
# ________________________________________________________



# Effectue toutes les taches

def rewards_auto_daily_weekly(set):
    for truc in set:
        pause_pour_veski_le_bot()

        if truc['check'] == False:
            if truc['type'] == 'normal_link':
                truc['link'].click()
                pause_pour_veski_le_bot()
                pause_pour_veski_le_bot()
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            elif truc['type'] == 'sondage':
                truc['link'].click()
                pause_pour_veski_le_bot()
                pause_pour_veski_le_bot()
                driver.switch_to.window(driver.window_handles[-1])
                if randint(1, 2) == 1:
                    driver.find_element(By.ID, "btoption0").click()
                else:
                    driver.find_element(By.ID, "btoption1").click()
                pause_pour_veski_le_bot()
                pause_pour_veski_le_bot()
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            elif truc['type'] == 'quiz':
                truc['link'].click()
                pause_pour_veski_le_bot()
                driver.switch_to.window(driver.window_handles[-1])
                driver.find_element(By.ID, "rqStartQuiz").click()
                sleep(1)
                for nb in range(3):
                    answers = [e.get_attribute("id")
                               for e in driver.find_elements(By.XPATH, '//*[@iscorrectoption="True"]')]
                    print(driver.find_elements(By.XPATH, '//*[@iscorrectoption="True"]'))
                    for a in answers:
                        driver.find_element(By.ID, a).click()
                        pause_pour_veski_le_bot(tps_en_moins=2)
                        # Si le nb de crédit augmente, on a la bonne de réponse donc on arrete de cliquer sur les
                        # réponses
                        if int(driver.find_element(By.CLASS_NAME, "rqECredits").text) == nb*10 + 10:
                            break
                    pause_pour_veski_le_bot()
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            elif truc['type'] == 'ceci_cela_quiz':
                truc['link'].click()
                pause_pour_veski_le_bot()
                driver.switch_to.window(driver.window_handles[-1])
                pyautogui.click(274, 935)
                sleep(1)
                for question in range(10):
                    if randint(1, 2) == 1:
                        pyautogui.click(645, 840)
                    else:
                        pyautogui.click(1150, 840)
                    pause_pour_veski_le_bot()
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
# ________________________________________________________



# C'est la pause pour veski le bot

def pause_pour_veski_le_bot(t1=4, t2=7, tps_en_moins=0):
    sleep(randint(t1-tps_en_moins, t2-tps_en_moins))
# ________________________________________________________







# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# ---------- CODE DE GAMING----------
# ____________________________________




def code_de_gaming(email, mdp, liste_recherches):

    try:

        # Vérifie si un élément existe
        def check_element(type:str, element:str):
            try:
                if type == 'By.XPATH':
                    driver.find_element(By.XPATH, element)
                if type == 'By.ID':
                    driver.find_element(By.ID, element)

                if element == 'bnp_btn_accept':
                    print('oui')
            except NoSuchElementException:
                return False
            return True


        #            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #            ----- OUVERTURE DU NAVIGATEUR -----
        #            ____________________________________


        driver.get("https://bing.com")
        driver.maximize_window()


        pause_pour_veski_le_bot()



    #            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    #            ------------- CONNEXION-------------
    #            ____________________________________


        # Bouton 'se connecter'
        button_connect = driver.find_element(By.ID, "id_l")
        button_connect.click()

        pause_pour_veski_le_bot()


        # Email
        email_input = driver.find_element(By.NAME, "loginfmt")
        email_input.send_keys(email)
        email_input.send_keys(Keys.ENTER)

        pause_pour_veski_le_bot()


        # Compte perso (Si on demande le choix entre compte perso et compte pro, le compte perso est prioritaire)
        if check_element('By.XPATH', '//*[@id="msaTile"]/div') == True:
            compte_perso = driver.find_element(By.XPATH, '//*[@id="msaTile"]/div')
            compte_perso.click()

            pause_pour_veski_le_bot()


        # Mot de passe
        mdp_input = driver.find_element(By.NAME, "passwd")
        mdp_input.send_keys(mdp)
        mdp_input.send_keys(Keys.ENTER)

        pause_pour_veski_le_bot()


        # Rester connecté (Bouton à cocher)
        if check_element('By.ID', "KmsiCheckboxField") == True:
            check_button_stay_connected = driver.find_element(By.ID, "KmsiCheckboxField")
            check_button_stay_connected.click()

        pause_pour_veski_le_bot()


        # Rester connecté (Click sur "oui")
        if check_element('By.ID', "idSIButton9") == True:
            stay_connected_non = driver.find_element(By.ID, "idSIButton9")
            pause_pour_veski_le_bot()
            stay_connected_non.click()

        pause_pour_veski_le_bot()


        # Cookies
        if check_element('By.ID', "bnp_btn_accept") == True:
            valider_cookies = driver.find_element(By.ID, "bnp_btn_accept")
            valider_cookies.click()

        pause_pour_veski_le_bot()





        #            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #            ------------ DAILY SET ------------
        #            ____________________________________



        driver.get('https://rewards.bing.com')

        pause_pour_veski_le_bot()

        daily_set = []

        for e in range(3):
            daily_set.append({
                'link' : driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{e+1}]'),
                'check': is_check(driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{e+1}]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[1]').get_attribute('class')),
                'pts'  : driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{e+1}]/div/card-content/mee-rewards-daily-set-item-content/div/a/mee-rewards-points/div/div/span[2]').text,
                'type' : what_type(driver.find_element(By.XPATH, f'//*[@id="daily-sets"]/mee-card-group[1]/div/mee-card[{e+1}]/div/card-content/mee-rewards-daily-set-item-content/div/a/div[2]/h3').text)
            })




        #            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        #            ------------ WEEKLY SET ------------
        #            ____________________________________




        pause_pour_veski_le_bot()

        weekly_set_items = len(driver.find_element(By.XPATH, '//*[@id="more-activities"]/div').find_elements(By.TAG_NAME, 'mee-card'))


        weekly_set = []
        for p in range(weekly_set_items):
            try:
                weekly_set.append({
        'check': is_check(driver.find_element(By.XPATH, f'//*[@id="more-activities"]/div/mee-card[{p+1}]/div/card-content/mee-rewards-more-activities-card-item/div/a/mee-rewards-points/div/div/span[1]').get_attribute('class')),
        'pts'  : driver.find_element(By.XPATH, f'//*[@id="more-activities"]/div/mee-card[{p+1}]/div/card-content/mee-rewards-more-activities-card-item/div/a/mee-rewards-points/div/div/span[2]').text,
        'type' : what_type(driver.find_element(By.XPATH, f'//*[@id="more-activities"]/div/mee-card[{p+1}]/div/card-content/mee-rewards-more-activities-card-item/div/a/div[2]/h3').text),
        'link' : driver.find_element(By.XPATH, f'//*[@id="more-activities"]/div/mee-card[{p+1}]')
                })
            except:
                print(f"L'itération {p+1} n'est pas un truc qui rapporte des points")


        rewards_auto_daily_weekly(daily_set)
        pause_pour_veski_le_bot(tps_en_moins=1)
        rewards_auto_daily_weekly(weekly_set)


        if driver.find_element(By.XPATH, '//*[@id="meeBanner"]/div/div/mee-persona/div[2]/persona-body/p[1]').text == 'Niveau 1':
            recherches(nb_pc=12, nb_tel=0, liste_recherches=liste_recherches)
        else:
            recherches(nb_pc=35, nb_tel=25, liste_recherches=liste_recherches)

        playsound(sound='notif.mp3')
        ToastNotifier().show_toast(title="Microsoft Rewards", msg="Toutes les tâches ont été effectuées", duration=10)



    except Exception as e:

        playsound(sound='notif.mp3')
        ToastNotifier().show_toast(title="Microsoft Rewards", msg="Erreur", duration=10)

        print(e)
        print(traceback.print_exc())

#            ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
#            ------- FAIRE TOUS LES TRUCS -------
#            ____________________________________


code_de_gaming(email, mdp, liste_recherches)




'''
sleep(3)
print(pyautogui.pixel(1727, 815))

print(pyautogui.position())
pyautogui.click(1727, 815)

exit()'''











