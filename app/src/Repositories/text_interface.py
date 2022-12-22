from config import TARGETS_FILE_PATH


class Functionality:

    """ Säästökohteisiin liittyviä toimenpiteitä käsittelevä luokka"""

    def __init__(self):
        self.file = TARGETS_FILE_PATH


    def get_id(self):
        """Luodaan säästökohteelle id, sen perusteella monesko kohde on tiedostossa."""

        with open(self.file) as file:
            return (sum(1 for line in file)+1)
    

    def delete_all(self):
        """Poistaa kaikki säästökohteet CSV-tiedostosta"""
        with open(self.file, "w") as file:
            pass
        return "Everything deleted"


