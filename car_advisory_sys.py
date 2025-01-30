class CarSelectionExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = []
        self.car_database = {}  # Słownik modeli samochodów przypisanych do rekomendacji

    def add_fact(self, key, value):
        self.facts[key] = value

    def add_rule(self, condition, result):
        self.rules.append((condition, result))

    def add_car_models(self, recommendation, models):
     
        self.car_database[recommendation] = models

    def evaluate(self):
        recommendations = []
        for condition, result in self.rules:
            if condition(self.facts):
                recommendations.append(result)
        return recommendations

    def get_car_models(self, recommendations):
     
        car_models = []
        for rec in recommendations:
            if rec in self.car_database:
                car_models.extend(self.car_database[rec])
        return car_models

    def ask_question(self, question, fact_key, expected_type="bool"):
        """
        Zadaj pytanie użytkownikowi i dodaj odpowiedź jako fakt.
        """
        while True:
            print(question)
            answer = input("Odpowiedź: ").lower()
            if expected_type == "bool":
                if answer in ["tak", "nie"]:
                    self.add_fact(fact_key, answer == "tak")
                    break
                else:
                    print("Proszę odpowiedzieć 'tak' lub 'nie'.")
            elif expected_type == "int":
                try:
                    value = int(answer)
                    self.add_fact(fact_key, value)
                    break
                except ValueError:
                    print("Proszę podać kwotę.")


def main():
    system = CarSelectionExpertSystem()

    # Zadawanie pytań użytkownikowi
    system.ask_question("Czy potrzebujesz samochodu rodzinnego? (tak/nie)", "family_car")
    system.ask_question("Jaki jest Twój budżet na samochód? (podaj kwotę w PLN)", "budget", "int")
    system.ask_question("Czy jeździsz głównie po mieście? (tak/nie)", "city_driving")
    system.ask_question("Czy zależy Ci na niskim zużyciu paliwa? (tak/nie)", "fuel_efficiency")
    system.ask_question("Czy masz dostęp do ładowarki samochodowej? (tak/nie)", "charger_access")
    system.ask_question("Czy planujesz podróże na długie dystanse? (tak/nie)", "long_distance")
    system.ask_question("Czy zależy Ci na dużym bagażniku? (tak/nie)", "large_trunk")
    system.ask_question("Czy preferujesz samochody z wysokim zawieszeniem? (tak/nie)", "high_clearance")
    system.ask_question("Czy zależy Ci na niskich kosztach utrzymania? (tak/nie)", "low_maintenance")
    system.ask_question("Czy cenią Cię zwrotność i łatwość parkowania? (tak/nie)", "maneuverability")

    
    # Baza reguł
    rules = [
    (lambda f: f.get("family_car") and f.get("large_trunk"), "SUV lub kombi dla rodzin."),
    (lambda f: f.get("budget", 0) < 30000, "Samochody używane do 30 tys. PLN."),
    (lambda f: 30000 <= f.get("budget", 0) <= 100000, "Nowe modele z niższego segmentu."),
    (lambda f: f.get("budget", 0) > 100000, "Marki premium do 100 tys. PLN."),
    (lambda f: f.get("city_driving") and f.get("fuel_efficiency"), "Hybrydy do miasta."),
    (lambda f: f.get("city_driving") and f.get("electric_no_emission"), "Samochody elektryczne do miasta."),
    (lambda f: f.get("long_distance") and f.get("diesel_long_distance"), "Diesel idealny na długie trasy."),
    (lambda f: f.get("charger_access") and f.get("electric_charger_required"), "Elektryki dzięki dostępowi do ładowarek."),
    (lambda f: not f.get("charger_access") and f.get("electric_charger_required"), "Elektryki niewskazane bez ładowarki."),
    (lambda f: f.get("large_family") and f.get("suv_spacious"), "SUV-y idealne dla dużych rodzin."),
    (lambda f: f.get("high_clearance") and f.get("off_road"), "Napęd 4x4 dla jazdy terenowej."),
    (lambda f: f.get("low_maintenance") and f.get("hybrids_fuel_efficient"), "Hybrydy mają niskie koszty utrzymania."),
    (lambda f: f.get("luxury_interior") and f.get("high_budget"), "Samochody luksusowe z wysokim budżetem."),
    (lambda f: f.get("fuel_efficiency") and f.get("budget", 0) < 100000, "Hybrydy w niższym segmencie."),
    (lambda f: f.get("city_driving") and f.get("small_cars_maneuverable"), "Samochody miejskie dla łatwego parkowania."),
    (lambda f: f.get("compact_cars") and f.get("budget", 0) <= 30000, "Używane auta segmentu C."),
    (lambda f: f.get("diesel_torque") and f.get("diesel_towing"), "Diesle dla ciężkich przyczep."),
    (lambda f: f.get("electric_range") and not f.get("long_distance"), "Elektryki na krótkie dystanse."),
    (lambda f: f.get("electric_no_emission") and f.get("fuel_efficiency"), "Elektryki dla niskiej emisji spalin."),
    (lambda f: f.get("kombi_large_trunk") and f.get("family_car"), "Kombi dla rodzin z dziećmi."),
    (lambda f: f.get("suv_high_power") and f.get("high_clearance"), "SUV-y o dużej mocy do trudnych warunków."),
    (lambda f: f.get("suv_medium_trunk") and f.get("family_car"), "SUV-y dla rodzin z dużym bagażnikiem."),
    (lambda f: f.get("suv_high_consumption") and not f.get("low_maintenance"), "SUV-y mogą być drogie w eksploatacji."),
    (lambda f: f.get("kombi_large_trunk") and f.get("budget", 0) < 100000, "Kombi dla rodzin w średnim budżecie."),
    (lambda f: f.get("gasoline_economical") and not f.get("long_distance"), "Benzyna na krótkie dystanse."),
    (lambda f: f.get("4x4_safety") and f.get("off_road"), "Napęd 4x4 zwiększa bezpieczeństwo."),
    (lambda f: f.get("city_trunk_small") and f.get("maneuverability"), "Małe auta miejskie z małym bagażnikiem."),
    (lambda f: f.get("premium_safety") and f.get("luxury_interior"), "Samochody premium dla bezpieczeństwa i komfortu."),
    (lambda f: f.get("low_budget") and f.get("compact_cars"), "Samochody używane segmentu C."),
    (lambda f: f.get("electric_cost_efficient") and f.get("charger_access"), "Elektryki są tanie w eksploatacji przy ładowarce."),
    (lambda f: f.get("city_cars_economical") and f.get("budget", 0) < 50000, "Małe auta miejskie w niskim budżecie."),
    (lambda f: f.get("maneuverability") and not f.get("large_cars_parking_difficulty"), "Zwrotne auta dla łatwego parkowania."),
    (lambda f: f.get("luxury_interior") and f.get("fuel_efficiency"), "Samochody luksusowe hybrydowe."),
    (lambda f: f.get("family_car") and f.get("kombi_large_trunk"), "Kombi to dobry wybór dla rodzin."),
    (lambda f: f.get("city_driving") and f.get("small_cars_maneuverable"), "Małe auta do miasta."),
]

    for condition, result in rules:
        system.add_rule(condition, result)

    # Dodanie bazy modeli samochodów
    system.add_car_models("SUV lub kombi dla rodzin.", ["Toyota RAV4", "Kia Sportage", "Volkswagen Passat Variant"])
    system.add_car_models("Samochody używane do 30 tys. PLN.", ["Ford Focus Mk3", "Opel Astra H", "Volkswagen Golf V"])
    system.add_car_models("Nowe modele z niższego segmentu.", ["Toyota Yaris", "Hyundai i20", "Skoda Fabia"])
    system.add_car_models("Marki premium do 100 tys. PLN.", ["BMW Seria 3", "Audi A4", "Mercedes-Benz C-Class"])
    system.add_car_models("Hybrydy do miasta.", ["Toyota Prius", "Hyundai Ioniq Hybrid", "Honda Jazz Hybrid"])
    system.add_car_models("Samochody elektryczne do miasta.", ["Nissan Leaf", "Renault Zoe", "BMW i3"])
    system.add_car_models("Diesel idealny na długie trasy.", ["Volkswagen Passat TDI", "Skoda Octavia TDI", "Ford Mondeo TDCi"])
    system.add_car_models("Elektryki dzięki dostępowi do ładowarek.", ["Tesla Model 3", "Hyundai Kona Electric", "Volkswagen ID.4"])
    system.add_car_models("Elektryki niewskazane bez ładowarki.", [])
    system.add_car_models("SUV-y idealne dla dużych rodzin.", ["Kia Sorento", "Hyundai Santa Fe", "Toyota Highlander"])
    system.add_car_models("Napęd 4x4 dla jazdy terenowej.", ["Jeep Wrangler", "Land Rover Defender", "Suzuki Jimny"])
    system.add_car_models("Hybrydy mają niskie koszty utrzymania.", ["Toyota Corolla Hybrid", "Lexus UX 250h", "Honda Insight"])
    system.add_car_models("Samochody luksusowe z wysokim budżetem.", ["Tesla Model S", "Mercedes-Benz S-Class", "Audi A8"])
    system.add_car_models("Hybrydy w niższym segmencie.", ["Toyota C-HR Hybrid", "Kia Niro Hybrid", "Hyundai Ioniq Hybrid"])
    system.add_car_models("Samochody miejskie dla łatwego parkowania.", ["Fiat 500", "Mini Cooper", "Volkswagen Polo"])
    system.add_car_models("Używane auta segmentu C.", ["Mazda 3", "Ford Focus", "Volkswagen Golf"])
    system.add_car_models("Diesle dla ciężkich przyczep.", ["Ford Ranger", "Toyota Hilux", "Nissan Navara"])
    system.add_car_models("Elektryki na krótkie dystanse.", ["Renault Zoe", "BMW i3", "Peugeot e-208"])
    system.add_car_models("Elektryki dla niskiej emisji spalin.", ["Tesla Model 3", "Nissan Leaf", "Hyundai Kona Electric"])
    system.add_car_models("Kombi dla rodzin z dziećmi.", ["Volkswagen Passat Variant", "Skoda Superb Combi", "Opel Insignia Sports Tourer"])
    system.add_car_models("SUV-y o dużej mocy do trudnych warunków.", ["Volvo XC90", "Audi Q7", "BMW X5"])
    system.add_car_models("SUV-y dla rodzin z dużym bagażnikiem.", ["Honda CR-V", "Nissan X-Trail", "Hyundai Tucson"])
    system.add_car_models("SUV-y mogą być drogie w eksploatacji.", [])
    system.add_car_models("Kombi dla rodzin w średnim budżecie.", ["Skoda Octavia Combi", "Ford Focus Kombi", "Hyundai i30 Wagon"])
    system.add_car_models("Benzyna na krótkie dystanse.", ["Toyota Aygo", "Fiat Panda", "Suzuki Swift"])
    system.add_car_models("Napęd 4x4 zwiększa bezpieczeństwo.", ["Subaru Forester", "Jeep Compass", "Toyota RAV4 AWD"])
    system.add_car_models("Małe auta miejskie z małym bagażnikiem.", ["Fiat 500", "Toyota Aygo", "Volkswagen up!"])
    system.add_car_models("Samochody premium dla bezpieczeństwa i komfortu.", ["Volvo XC60", "Mercedes-Benz GLE", "Audi Q5"])
    system.add_car_models("Samochody używane segmentu C.", ["Opel Astra", "Renault Megane", "Ford Focus"])
    system.add_car_models("Elektryki są tanie w eksploatacji przy ładowarce.", ["Hyundai Kona Electric", "Nissan Leaf", "Volkswagen ID.3"])
    system.add_car_models("Małe auta miejskie w niskim budżecie.", ["Skoda Citigo", "Toyota Aygo", "Renault Twingo"])
    system.add_car_models("Zwrotne auta dla łatwego parkowania.", ["Fiat 500", "Volkswagen Polo", "Toyota Yaris"])
    system.add_car_models("Samochody luksusowe hybrydowe.", ["Lexus RX 450h", "Volvo XC60 Recharge", "BMW X5 xDrive45e"])
    system.add_car_models("Kombi to świetny wybór dla rodzin.", ["Skoda Superb Combi", "Ford Mondeo Kombi", "Volkswagen Passat Variant"])
    system.add_car_models("Małe auta do miasta.", ["Toyota Yaris", "Fiat Panda", "Hyundai i10"])


    # Wnioskowanie
    recommendations = system.evaluate()

    # Pobranie modeli samochodów
    car_models = system.get_car_models(recommendations)

    # Wyświetlenie wyników
    print("\n**Rekomendacje:**")
    if recommendations:
        for rec in recommendations:
            print(f"- {rec}")
    else:
        print("Brak rekomendacji na podstawie podanych danych.")

    if car_models:
        print("\n**Proponowane modele samochodów:**")
        for model in car_models:
            print(f"- {model}")
    else:
        print("Brak dopasowanych modeli samochodów.")

if __name__ == "__main__":
    main()
