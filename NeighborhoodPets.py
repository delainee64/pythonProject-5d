# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/08/2023
# Description: rite a class named NeighborhoodPets that has methods for adding a pet, deleting a pet,
# searching for the owner of a pet, saving data to a JSON file, loading data from a JSON file,
# and getting a set of all pet species.
import json


class DuplicateNameError(Exception):
    """User-defined exception when target isn't found."""
    pass


class NeighborhoodPets:
    """Represents pets in a neighborhood."""

    def __init__(self):
        self._pet_dict = {}

    def add_pet(self, name, species, owner):
        """Returns the name, species, and owner in a specific neighborhood."""
        if name not in self._pet_dict:
            self._pet_dict[name] = {"name": name, "species": species, "owner": owner}
        else:
            raise DuplicateNameError

    def delete_pet(self, name):
        """Deletes a pet in the pet dictionary."""
        if name in self._pet_dict:
            del self._pet_dict[name]

    def get_owner(self, name):
        """Returns the name of the pet's owner."""
        if name in self._pet_dict:
            return self._pet_dict[name]["owner"]

    def save_as_json(self, file):
        """Saves data in a JSON file."""
        data = self._pet_dict
        with open(file, 'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, file):
        """Reads data in a JSON file."""
        with open(file, 'r') as json_file:
            self._pet_dict = json.load(json_file)

    def get_all_species(self):
        """Return's all species in the data."""
        pet_species = {pet["species"] for pet in self._pet_dict.values()}
        return pet_species


# np = NeighborhoodPets()
# try:
    # np.add_pet("Fluffy", "gila monster", "Oksana")
    # np.add_pet("Tiny", "stegasaurus", "Rachel")
    # np.add_pet("Spot", "zebra", "Farrokh")
# except DuplicateNameError:
    # print('You tried to enter a pet with the same name as another pet.')
# np.save_as_json("pets.json")
# np.delete_pet("Tiny")
# spot_owner = np.get_owner("Spot")
# np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
# species_set = np.get_all_species()
# print(species_set)
