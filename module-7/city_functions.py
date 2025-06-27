def cityAndCountry(city, country, population=None, language=None):
  result = f"{city}, {country}"
  if population:
      result += f" - population {population}"
  if language:
      result += f", {language}"
  return result

print(cityAndCountry("Santiago", "Chile",5000000))
print(cityAndCountry("Cleveland", "USA", 362656))
print(cityAndCountry("New York City", "USA", 8258000, "English"))