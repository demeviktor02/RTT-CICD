""" Jelszó erősség ellenőrzése pythonban"""

class JelszoErossegEllenorzo():
    """ jelszó erősség ellenőrző osztály"""

    def nagybetu_tartalmazo_ellenorzo(self, jelszo):
        """nagybetűt tartalmazó ellenőrző, a felhasználó által beírt jelszóra"""
        for betu in jelszo:

            # checking for uppercase character and flagging
            if betu.isupper():
                return True
        return False

    def specialis_karakter_tartalmazo_ellenorzo(self, jelszo):
        """speciális karakter tartalmazó ellenőrző, a felhasználó által beírt jelszóra"""
        special = "#@$%^&*()-+?_=,<>/"
        for betu in jelszo:

            # checking for uppercase character and flagging
            if any(c in special for c in betu):
                return True
        return False

    def jelszo_erosseg_ellenorzo(self, jelszo):
        """jelszó erősség ellenőrző, a felhasználó által beírt jelszóra"""

        if type(jelszo) not in [str, chr]:
            raise TypeError('Csak string típus elfogadható!')

        print(f"A felhasználó által begépelt jelszó: {jelszo}")

        erosseg = 0

        if jelszo == "":
            print("-Nem adott meg jelszót")
            erosseg = -1
            return erosseg

        if len(jelszo) < 8:
            print(f"-A megadott jelszó hosszúsága kevesebb mint 8 karakter, csak "
                  f"{len(jelszo)} karaktert tartalmaz")
        else:
            erosseg += 1

        if self.nagybetu_tartalmazo_ellenorzo(jelszo):
            erosseg += 1
        else:
            print(f"-A megadott jelszó nem tartalmaz nagybetűt")

        if self.specialis_karakter_tartalmazo_ellenorzo(jelszo):
            erosseg += 1
        else:
            print(f"-A megadott jelszó nem tartalmaz speciális karaktert")


        if erosseg == 0:
            print("A jelszó nagyon gyenge")
        elif erosseg == 1:
            print("A jelszó gyenge")
        elif erosseg == 2:
            print("A jelszó közepes")
        elif erosseg == 3:
            print("A jelszó erős")

        print("")
        return erosseg


j = JelszoErossegEllenorzo()
j.jelszo_erosseg_ellenorzo("")
j.jelszo_erosseg_ellenorzo("12345")
j.jelszo_erosseg_ellenorzo("12345678")
j.jelszo_erosseg_ellenorzo("N2345678")
j.jelszo_erosseg_ellenorzo("N@345678")
