import os

def run_script():
    # Ausgabe des Infotextes
    print("Start-LuV Generator     -v0.5\n") 
    print("Dieses Script generiert Start-LuVs anhand der Beobachtungskennzahlen aus der Stärken-/Schwächen Analyse.\n")
    print("Der Name wird eingefügt und die Personalpronomen entsprechend der Anrede geändert.\n")
    print("Bei besonderer Eignung für ein Berufsfeld kann dieses alternativ eingetragen werden.\n")
    print(" \n")
    print("Die erste Zahl ist die Gesamteinschätzung des jeweiligen Kompetenzbereichs,\n")
    print("die folgenden Kennzahlen entsprechen der Reihenfolge in der Analyse.\n")
    print("                                                                                          /D. Drews 2024\n")
    print("                                                                                    Fach-Werk-Minden e.V.\n")
    print(" \n")

    # Eingabe der erforderlichen Daten
    anrede_nachname = input("Bitte die Anrede und den Nachnamen eingeben (z.B. Herr/Frau Meier): ")
    ora = input("Besondere Eignung für Berufsfeld eingeben, ansonsten frei lassen (z.B. Holz): ")
    kennzahlen_personale = input("Bitte die Kennzahlen für personale Kompetenzen eingeben (6 Stück; 1 - 5) (z.B. 434454): ")
    kennzahlen_sozial = input("Bitte die Kennzahlen für sozial-kommunikative Kompetenzen eingeben (5 Stück; 1 - 5) (z.B. 54433): ")
    kennzahlen_methodisch = input("Bitte die Kennzahlen für methodische Kompetenzen eingeben (4 Stück; 1 - 5) (z.B. 4334): ")
    kennzahlen_schulisch = input("Bitte die Kennzahlen für schulische Basiskompetenzen eingeben (6 Stück; 1 - 5) (z.B. 123455): ")
    kennzahlen_fachlich = input("Bitte die Kennzahlen für fachliche Basiskompetenzen eingeben (5 Stück; 1 - 5) (z.B. 33445): ")

    # Bestimmen der Personalpronomen
    if "Herr" in anrede_nachname:
        pronomen_er_sie = "Er"
        pronomen_ihm_ihr = "ihm"
        pronomen_sein_ihr = "Sein"
    else:
        pronomen_er_sie = "Sie"
        pronomen_ihm_ihr = "ihr"
        pronomen_sein_ihr = "Ihr"

    # Textbausteine für Unterpunkt "Personale Kompetenzen"
    personale_kompetenzen = [
        "NOMEN verfügt über die erforderlichen personalen Kompetenzen in geringem Maße.",
        "NOMEN verfügt teilweise über die erforderlichen personalen Kompetenzen.",
        "NOMEN verfügt in der Regel über die erforderlichen personalen Kompetenzen.",
        "NOMEN verfügt über die erforderlichen personalen Kompetenzen.",
        "NOMEN verfügt über außerordentliche personale Kompetenzen."
    ]

    leistungsbereitschaft = [
        f"{pronomen_er_sie} zeigt vereinzelt Leistungsbereitschaft/Motivation",
        f"{pronomen_er_sie} zeigt sporadische Leistungsbereitschaft/Motivation",
        f"{pronomen_er_sie} zeigt weitesgehend gute Leistungsbereitschaft/Motivation",
        f"{pronomen_er_sie} zeigt gute Leistungsbereitschaft/Motivation",
        f"{pronomen_er_sie} zeigt sehr gute Leistungsbereitschaft/Motivation"
    ]

    durchhaltevermoegen = [
        "und wenig Durchhaltevermögen.",
        "und etwas Durchhaltevermögen.",
        "und durchschnittliches Durchhaltevermögen.",
        "und viel Durchhaltevermögen.",
        "und außergewöhnliches Durchhaltevermögen."
    ]

    zuverlaessigkeit = [
        f"{pronomen_er_sie} zeigt sich selten zuverlässig.",
        f"{pronomen_er_sie} zeigt sich mitunter zuverlässig.",
        f"{pronomen_er_sie} zeigt sich grundsätzlich zuverlässig.",
        f"{pronomen_er_sie} zeigt sich zuverlässig.",
        f"{pronomen_er_sie} zeigt sich stets zuverlässig."
    ]

    sorgfalt = [
        f"{pronomen_er_sie} arbeitet im Einzelfall sorgfältig und genau.",
        f"{pronomen_er_sie} arbeitet zeitweilig sorgfältig und genau.",
        f"{pronomen_er_sie} arbeitet in der Regel sorgfältig und genau.",
        f"{pronomen_er_sie} arbeitet sorgfältig und genau.",
        f"{pronomen_er_sie} arbeitet überaus sorgfältig und genau."
    ]

    kritikfaehigkeit = [
        f"{pronomen_er_sie} verfügt über kaum ausgeprägte Kritikfähigkeit.",
        f"{pronomen_er_sie} verfügt über etwas Kritikfähigkeit.",
        f"{pronomen_er_sie} verfügt über Kritikfähigkeit.",
        f"{pronomen_er_sie} verfügt über gute Kritikfähigkeit.",
        f"{pronomen_er_sie} verfügt über sehr gute Kritikfähigkeit."
    ]

    # Wenn die ora-Variable gefüllt ist, den Satz ergänzen
    if ora:
        sorgfalt = [
            f"{pronomen_er_sie} arbeitet im Einzelfall sorgfältig und genau (vor allem im Bereich {ora}).",
            f"{pronomen_er_sie} arbeitet zeitweilig sorgfältig und genau (vor allem im Bereich {ora}).",
            f"{pronomen_er_sie} arbeitet in der Regel sorgfältig und genau (vor allem im Bereich {ora}).",
            f"{pronomen_er_sie} arbeitet sorgfältig und genau (vor allem im Bereich {ora}).",
            f"{pronomen_er_sie} arbeitet überaus sorgfältig und genau (vor allem im Bereich {ora})."
        ]

    # Textbausteine für Unterpunkt "Sozial-kommunikative Kompetenzen"
    sozial_kompetenzen = [
        "NOMEN verfügt über schwach ausgeprägte sozial-kommunikative Kompetenzen.",
        "NOMEN verfügt über unterdurchschnittlich ausgeprägte sozial-kommunikative Kompetenzen.",
        "NOMEN verfügt weitesgehend über die erforderlichen sozial-kommunikativen Kompetenzen.",
        "NOMEN verfügt über die erforderlichen sozial-kommunikative Kompetenzen.",
        "NOMEN verfügt über außerordentliche sozial-kommunikative Kompetenzen."
    ]

    team_konfliktfaehigkeit = [
        f"{pronomen_er_sie} zeigt wenig Team- und Konfliktfähigkeit, ",
        f"{pronomen_er_sie} zeigt etwas Team- und Konfliktfähigkeit, ",
        f"{pronomen_er_sie} zeigt durchschnittliche Team- und Konfliktfähigkeit, ",
        f"{pronomen_er_sie} zeigt gute Team- und Konfliktfähigkeit, ",
        f"{pronomen_er_sie} besitzt sehr gute Team und Konflikfähigkeit, "
    ]

    teamarbeit_loesung = [
        "wirkt selten an einer einvernehmlichen Lösung im Team mit",
        "wirkt nur in geringem Maße an einer einvernehmlichen Lösung im Team mit",
        "wirkt in der Regel an einer einvernehmlichen Lösung im Team mit",
        "wirkt engagiert an einer einvernehmlichen Lösung im Team mit",
        "wirkt überaus engagiert an einer einvernehmlichen Lösung im Team mit"
    ]

    erfahrung_wissen = [
        "und bringt wenig eigene/s Erfahrung/Wissen in die Teamarbeit mit ein.",
        "und bringt etwas eigene/s Erfahrung/Wissen in die Teamarbeit mit ein.",
        "und bringt eigene/s Erfahrung/Wissen in die Teamarbeit mit ein.",
        "und bringt viel eigene/s Erfahrung/Wissen in die Teamarbeit mit ein.",
        "und bringt immens viel eigene/s Erfahrung/Wissen in die Teamarbeit mit ein."
    ]

    kommunikative_faehigkeiten = [
        f"{pronomen_er_sie} weist wenig kommunikative Fähigkeiten auf.",
        f"{pronomen_er_sie} besitzt sporadische kommunikative Fähigkeiten.",
        f"{pronomen_er_sie} besitzt die erforderlichen kommunikativen Fähigkeiten.",
        f"{pronomen_er_sie} weist gute kommunikative Fähigkeiten auf.",
        f"{pronomen_er_sie} besitzt sehr gute kommunikative Fähigkeiten."
    ]

    # Textbausteine für Unterpunkt "Methodische Kompetenzen"
    methodische_kompetenzen = [
        "NOMEN verfügt über ausbaufähige methodische Kompetenzen.",
        "NOMEN verfügt über unterdurchschnittliche methodische Kompetenzen.",
        "NOMEN verfügt über die erforderlichen methodischen Kompetenzen.",
        "NOMEN verfügt über gute methodische Kompetenzen.",
        "NOMEN übertrifft die erforderlichen methodischen Kompetenzen."
    ]

    selbststaendigkeit_organisation = [
        f"{pronomen_er_sie} zeigt kaum Selbstständigkeit und Organisationsfähigkeit",
        f"{pronomen_er_sie} zeigt etwas Selbständigkeit und Organisationsfähigkeit",
        f"{pronomen_er_sie} zeigt Selbstständigkeit und Organisationsfähigkeit",
        f"{pronomen_er_sie} zeigt vermehrt Selbstständigkeit und Organisationsfähigkeit",
        f"{pronomen_er_sie} zeigt herausragende Selbstständigkeit und Organisationsfähigkeit"
    ]

    analyse_problemloesung = [
        "sowie eine ausbaufähige Analyse- und Problemlösefähigkeit.",
        "sowie eine grundlegende Analyse- und Problemlösefähigkeit.",
        "sowie eine durchschnittliche Analyse- und Problemlösefähigkeit.",
        "sowie eine gute Analyse- und Problemlösefähigkeit.",
        "sowie eine exzellente Analyse- und Problemlösefähigkeit."
    ]

    it_medienkompetenz = [
        f"Im Bereich IT- und Medienkompetenz verfügt {pronomen_er_sie.lower()} über vereinzelte Kenntnisse.",
        f"Im Bereich IT- und Medienkompetenz besitzt {pronomen_er_sie.lower()} unterdurchschnittliche Kenntnisse.",
        f"Im Bereich IT- und Medienkompetenz verfügt {pronomen_er_sie.lower()} über durchschnittliche Kenntnisse.",
        f"Im Bereich IT- und Medienkompetenz besitzt {pronomen_er_sie.lower()} überdurchschnittliche Kenntnisse.",
        f"Im Bereich IT- und Medienkompetenz verfügt {pronomen_er_sie.lower()} über umfassende Kenntnisse."
    ]

    # Textbausteine für Unterpunkt "Schulische Basiskompetenzen"
    schulische_kompetenzen = [
        "NOMEN verfügt über geringe schulische Basiskompetenzen.",
        "NOMEN verfügt über grundlegende schulische Basiskompetenzen.",
        "NOMEN verfügt über durchschnittliche schulische Basiskompetenzen.",
        "NOMEN besitzt überdurchschnittliche schulische Basiskompetenzen.",
        "NOMEN verfügt über umfangreiche schulische Basiskompetenzen."
    ]

    mathematische_kompetenzen = [
        "Er/Sie besitzt wenig mathematische Basiskompetenzen, verfügt über gering ausgeprägtes logisches Verständnis",
        "Er/Sie besitzt einige mathematische Basiskompetenzen, verfügt über sporadisch ausgeprägtes logisches Verständnis",
        "Er/Sie besitzt mathematische Basiskompetenzen, verfügt über angemessenes logisches Verständnis",
        "Er/Sie besitzt gute mathematische Basiskompetenzen, verfügt über breites logisches Verständnis",
        "Er/Sie besitzt herausragende mathematische Basiskompetenzen, verfügt über exzellentes logisches Verständnis"
    ]

    spracherwerb = [
        "und einen förderfähigen Spracherwerb.",
        "und einen grundlegenden Spracherwerb.",
        "und einen ausgeprägten Spracherwerb.",
        "und einen guten Spracherwerb.",
        "und einen erstklassigen Spracherwerb."
    ]

    rechtschreibung = [
        f"Die grundlegenden Rechtschreibregeln kennt {pronomen_er_sie.lower()} teilweise und es fällt {pronomen_ihm_ihr} schwer, Texte zusammenhängend und verständlich zu schreiben.",
        f"Die grundlegenden Rechtschreibregeln kennt {pronomen_er_sie.lower()} im Großen und Ganzen und auch zusammenhängendes, verständliches Schreiben gelingt {pronomen_ihm_ihr} meistens.",
        f"Die grundlegenden Rechtschreibregeln kennt {pronomen_er_sie.lower()} weitestgehend gut und auch zusammenhängendes, verständliches Schreiben gelingt {pronomen_ihm_ihr} insgesamt.",
        f"Die grundlegenden Rechtschreibregeln beherrscht {pronomen_er_sie.lower()} fast immer sicher und auch zusammenhängendes, verständliches Schreiben bereitet {pronomen_ihm_ihr} keine Probleme.",
        f"Die grundlegenden Rechtschreibregeln beherrscht {pronomen_er_sie.lower()} in höchstem Maße und auch zusammenhängendes, verständliches Schreiben gelingt {pronomen_ihm_ihr} nahezu perfekt."
    ]

    allgemeinwissen = [
        f"{pronomen_sein_ihr} Allgemeinwissen ist nur wenig ausgeprägt.",
        f"{pronomen_sein_ihr} Allgemeinwissen ist sehr themenbezogen.",
        f"{pronomen_sein_ihr} Allgemeinwissen liegt im durchschnittlichen Bereich.",
        f"{pronomen_sein_ihr} Allgemeinwissen ist umfangreich.",
        f"{pronomen_sein_ihr} Allgemeinwissen ist außerordentlich umfangreich."
    ]

    englischkenntnisse = [
        f"Englischkenntnisse sind im Ansatz vorhanden.",
        f"Grundlegende Englischkenntnisse sind vorhanden.",
        f"Englischkenntnisse sind weitestgehend vorhanden.",
        f"Gute Englischkenntnisse sind vorhanden.",
        f"Sehr gute Englischkenntnisse sind vorhanden."
    ]

    # Textbausteine für Unterpunkt "Fachliche Basiskompetenzen"
    fachliche_kompetenzen = [
        "NOMEN verfügt nur über schwach ausgeprägte fachliche Basiskompetenzen.",
        "NOMEN verfügt teilweise über die erforderlichen fachlichen Basiskompetenzen.",
        "NOMEN verfügt in der Regel über die erforderlichen fachlichen Basiskompetenzen.",
        "NOMEN weist überdurchschnittliche fachliche Basiskompetenzen auf.",
        "NOMEN weist herausragende fachliche Basiskompetenzen auf."
    ]

    raeumliches_vorstellungsvermoegen = [
        f"{pronomen_er_sie} besitzt wenig räumliches Vorstellungsvermögen,",
        f"{pronomen_er_sie} besitzt prinzipiell räumliches Vorstellungsvermögen,",
        f"{pronomen_er_sie} besitzt räumliches Vorstellungsvermögen,",
        f"{pronomen_er_sie} besitzt gutes räumliches Vorstellungsvermögen,",
        f"{pronomen_er_sie} besitzt sehr gutes räumliches Vorstellungsvermögen,"
    ]

    technisches_verstaendnis = [
        "ausbaufähiges technisches Verständnis",
        "etwas technisches Verständnis",
        "brauchbares technisches Verständnis",
        "gutes technisches Verständnis",
        "sehr gutes technisches Verständnis"
    ]

    feinmotorik = [
        "und grob ausgeprägte Feinmotorik.",
        "und in Teilen ausgeprägte Feinmotorik.",
        "und durchschnittliche feinmotorische Fähigkeiten.",
        "und ist feinmotorisch geschickt.",
        "und ist feinmotorisch äußerst geschickt."
    ]

    sorgfalt_fachlich = [
        f"{pronomen_er_sie} arbeitet selten sorgfältig und hält die Vorgaben nur manchmal ein.",
        f"{pronomen_er_sie} arbeitet zeitweilen sorgfältig und hält die Vorgaben teilweise ein.",
        f"{pronomen_er_sie} arbeitet in der Regel sorgfältig und hält auch meist die Vorgaben ein.",
        f"{pronomen_er_sie} arbeitet sehr sorgfältig und hält die Vorgaben ein.",
        f"{pronomen_er_sie} arbeitet überaus sorgfältig und hält stets die Vorgaben ein."
    ]

    # Auswahl der Textbausteine basierend auf den Kennzahlen für personale Kompetenzen
    index_personale_1 = int(kennzahlen_personale[0]) - 1
    index_personale_2 = int(kennzahlen_personale[1]) - 1
    index_personale_3 = int(kennzahlen_personale[2]) - 1
    index_personale_4 = int(kennzahlen_personale[3]) - 1
    index_personale_5 = int(kennzahlen_personale[4]) - 1
    index_personale_6 = int(kennzahlen_personale[5]) - 1

    text_personale_kompetenzen = f"{personale_kompetenzen[index_personale_1].replace('NOMEN', anrede_nachname)} " \
                                 f"{leistungsbereitschaft[index_personale_2].replace('Er/Sie', pronomen_er_sie)} " \
                                 f"{durchhaltevermoegen[index_personale_3]} " \
                                 f"{zuverlaessigkeit[index_personale_4].replace('Er/Sie', pronomen_er_sie)} " \
                                 f"{sorgfalt[index_personale_5].replace('Er/Sie', pronomen_er_sie)} " \
                                 f"{kritikfaehigkeit[index_personale_6].replace('Er/Sie', pronomen_er_sie)}"

    # Auswahl der Textbausteine basierend auf den Kennzahlen für sozial-kommunikative Kompetenzen
    index_sozial_1 = int(kennzahlen_sozial[0]) - 1
    index_sozial_2 = int(kennzahlen_sozial[1]) - 1
    index_sozial_3 = int(kennzahlen_sozial[2]) - 1
    index_sozial_4 = int(kennzahlen_sozial[3]) - 1
    index_sozial_5 = int(kennzahlen_sozial[4]) - 1

    text_sozial_kompetenzen = f"{sozial_kompetenzen[index_sozial_1].replace('NOMEN', anrede_nachname)} " \
                              f"{team_konfliktfaehigkeit[index_sozial_2].replace('Er/Sie', pronomen_er_sie)}" \
                              f"{teamarbeit_loesung[index_sozial_3]} " \
                              f"{erfahrung_wissen[index_sozial_4]} " \
                              f"{kommunikative_faehigkeiten[index_sozial_5].replace('Er/Sie', pronomen_er_sie)} "

    # Auswahl der Textbausteine basierend auf den Kennzahlen für methodische Kompetenzen
    index_methodisch_1 = int(kennzahlen_methodisch[0]) - 1
    index_methodisch_2 = int(kennzahlen_methodisch[1]) - 1
    index_methodisch_3 = int(kennzahlen_methodisch[2]) - 1
    index_methodisch_4 = int(kennzahlen_methodisch[3]) - 1

    text_methodische_kompetenzen = f"{methodische_kompetenzen[index_methodisch_1].replace('NOMEN', anrede_nachname)} " \
                                   f"{selbststaendigkeit_organisation[index_methodisch_2].replace('Er/Sie', pronomen_er_sie)} " \
                                   f"{analyse_problemloesung[index_methodisch_3]} " \
                                   f"{it_medienkompetenz[index_methodisch_4].replace('Er/Sie', pronomen_er_sie)}"

    # Auswahl der Textbausteine basierend auf den Kennzahlen für schulische Basiskompetenzen
    index_schulisch_1 = int(kennzahlen_schulisch[0]) - 1
    index_schulisch_2 = int(kennzahlen_schulisch[1]) - 1
    index_schulisch_3 = int(kennzahlen_schulisch[2]) - 1
    index_schulisch_4 = int(kennzahlen_schulisch[3]) - 1
    index_schulisch_5 = int(kennzahlen_schulisch[4]) - 1
    index_schulisch_6 = int(kennzahlen_schulisch[5]) - 1

    text_schulische_kompetenzen = f"{schulische_kompetenzen[index_schulisch_1].replace('NOMEN', anrede_nachname)} " \
                                  f"{mathematische_kompetenzen[index_schulisch_2].replace('Er/Sie', pronomen_er_sie)} " \
                                  f"{spracherwerb[index_schulisch_3]} " \
                                  f"{rechtschreibung[index_schulisch_4]} " \
                                  f"{allgemeinwissen[index_schulisch_5]} " \
                                  f"{englischkenntnisse[index_schulisch_6].replace('Er/Sie', pronomen_er_sie)}"

    index_fachlich_1 = int(kennzahlen_fachlich[0]) - 1
    index_fachlich_2 = int(kennzahlen_fachlich[1]) - 1
    index_fachlich_3 = int(kennzahlen_fachlich[2]) - 1
    index_fachlich_4 = int(kennzahlen_fachlich[3]) - 1
    index_fachlich_5 = int(kennzahlen_fachlich[4]) - 1

    text_fachliche_kompetenzen = f"{fachliche_kompetenzen[index_fachlich_1].replace('NOMEN', anrede_nachname)} " \
                                 f"{raeumliches_vorstellungsvermoegen[index_fachlich_2].replace('Er/Sie', pronomen_er_sie)} " \
                                 f"{technisches_verstaendnis[index_fachlich_3]} " \
                                 f"{feinmotorik[index_fachlich_4]} " \
                                 f"{sorgfalt_fachlich[index_fachlich_5].replace('Er/Sie', pronomen_er_sie)}"

    # Zusammensetzen des gesamten Textes
    text = f"{text_personale_kompetenzen}\n\n{text_sozial_kompetenzen}\n\n{text_methodische_kompetenzen}\n\n{text_schulische_kompetenzen}\n\n{text_fachliche_kompetenzen}"

    # Ergebnis anzeigen
    print("\nErgebnis:\n")
    print(text)
    
    # Rückfrage für erneute Ausführung
    restart = input("\nVon vorn beginnen? (j/n): ")
    if restart.lower() in ["ja", "j"]:
        os.system('cls' if os.name == 'nt' else 'clear')  # Bildschirm löschen
        run_script()
    else:
        print("Das Programm wird beendet.")

if __name__ == "__main__":
    run_script()
