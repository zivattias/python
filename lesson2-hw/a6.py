# Self learning exercise - Structural Pattern Matching
# USA -> US dollar
# Israel - New Israel Shekel (NIS)
# UK -> Pound
# All the EU countries (Germany, Austria, Czech, France, Italy, Spain,...) -> Euro
# If user provides any other country, print “I don’t know”

country = input("Enter a country: ").strip().capitalize()  # capitalizes only first letter and makes rest lower

match country:
    case "Usa" | "United states of america":
        print("US Dollar")
    case "Israel":
        print("Shekel")
    case "Uk" | "United kingdom":
        print("Pound")
    case 'Austria' | 'Belgium' | 'Bulgaria' | 'Croatia' | 'Cyprus' | 'Czechia' | 'Denmark' | \
         'Estonia' | 'Finland' | 'France' | 'Germany' | 'Greece' | 'Hungary' | 'Ireland' | \
         'Italy' | 'Latvia' | 'Lithuania' | 'Luxembourg' | 'Malta' | 'Netherlands' | \
         'Poland' | 'Portugal' | 'Romania' | 'Slovakia' | 'Slovenia' | 'Spain' | 'Sweden':
        print("Euro")
    case _:
        print("I don't know.")
