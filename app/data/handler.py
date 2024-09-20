import json


def get_films(f_path:str = "app/data/films.json") -> list:
   with open(f_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)
        films = data.get("films")
        return films




def get_film(index: int) -> dict:
   films = get_films()
   return films[index]



if __name__ == "__main__":
   print(get_films())
