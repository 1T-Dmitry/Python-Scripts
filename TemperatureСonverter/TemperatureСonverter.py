print("""
Select the current temperature:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Rankine
    5. Delisle
    6. Newton
    7. Réaumur
    8. Rømer
""")

choice = input(": ")

match choice:
    case "1":
        currentTemperature = float(input("Enter the temperature: "))

        print("""
Convert to:
    1. Fahrenheit
    2. Kelvin
    3. Rankine
    4. Delisle
    5. Newton
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{(currentTemperature * 9 / 5) + 32:.2f} °F")
            case "2":
                print(f"{currentTemperature + 273.15:.2f} K")
            case "3":
                print(f"{(currentTemperature + 273.15) * 9 / 5:.2f} °R")
            case "4":
                print(f"{(100 - currentTemperature) * 3 / 2:.2f} °De")
            case "5":
                print(f"{currentTemperature * 0.33:.2f} °N")
            case "6":
                print(f"{currentTemperature * 0.8:.2f} °Ré")
            case "7":
                print(f"{currentTemperature * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "2":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Kelvin
    3. Rankine
    4. Delisle
    5. Newton
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{(currentTemperature - 32) * 5 / 9:.2f} °C")
            case "2":
                print(f"{(currentTemperature - 32) * 5 / 9 + 273.15:.2f} K")
            case "3":
                print(f"{currentTemperature + 459.67:.2f} °R")
            case "4":
                celsius = (currentTemperature - 32) * 5 / 9
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "5":
                celsius = (currentTemperature - 32) * 5 / 9
                print(f"{celsius * 0.33:.2f} °N")
            case "6":
                celsius = (currentTemperature - 32) * 5 / 9
                print(f"{celsius * 0.8:.2f} °Ré")
            case "7":
                celsius = (currentTemperature - 32) * 5 / 9
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "3":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Rankine
    4. Delisle
    5. Newton
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{currentTemperature - 273.15:.2f} °C")
            case "2":
                print(f"{(currentTemperature - 273.15) * 9 / 5 + 32:.2f} °F")
            case "3":
                print(f"{currentTemperature * 9 / 5:.2f} °R")
            case "4":
                celsius = currentTemperature - 273.15
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "5":
                celsius = currentTemperature - 273.15
                print(f"{celsius * 0.33:.2f} °N")
            case "6":
                celsius = currentTemperature - 273.15
                print(f"{celsius * 0.8:.2f} °Ré")
            case "7":
                celsius = currentTemperature - 273.15
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "4":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Delisle
    5. Newton
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{(currentTemperature - 491.67) * 5 / 9:.2f} °C")
            case "2":
                print(f"{currentTemperature - 459.67:.2f} °F")
            case "3":
                print(f"{currentTemperature * 5 / 9:.2f} K")
            case "4":
                celsius = (currentTemperature - 491.67) * 5 / 9
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "5":
                celsius = (currentTemperature - 491.67) * 5 / 9
                print(f"{celsius * 0.33:.2f} °N")
            case "6":
                celsius = (currentTemperature - 491.67) * 5 / 9
                print(f"{celsius * 0.8:.2f} °Ré")
            case "7":
                celsius = (currentTemperature - 491.67) * 5 / 9
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "5":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Rankine
    5. Newton
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{100 - currentTemperature * 2 / 3:.2f} °C")
            case "2":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{celsius * 9 / 5 + 32:.2f} °F")
            case "3":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{celsius + 273.15:.2f} K")
            case "4":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{(celsius + 273.15) * 9 / 5:.2f} °R")
            case "5":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{celsius * 0.33:.2f} °N")
            case "6":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{celsius * 0.8:.2f} °Ré")
            case "7":
                celsius = 100 - currentTemperature * 2 / 3
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "6":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Rankine
    5. Delisle
    6. Réaumur
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{currentTemperature / 0.33:.2f} °C")
            case "2":
                celsius = currentTemperature / 0.33
                print(f"{celsius * 9 / 5 + 32:.2f} °F")
            case "3":
                celsius = currentTemperature / 0.33
                print(f"{celsius + 273.15:.2f} K")
            case "4":
                celsius = currentTemperature / 0.33
                print(f"{(celsius + 273.15) * 9 / 5:.2f} °R")
            case "5":
                celsius = currentTemperature / 0.33
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "6":
                celsius = currentTemperature / 0.33
                print(f"{celsius * 0.8:.2f} °Ré")
            case "7":
                celsius = currentTemperature / 0.33
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "7":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Rankine
    5. Delisle
    6. Newton
    7. Rømer
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{currentTemperature / 0.8:.2f} °C")
            case "2":
                celsius = currentTemperature / 0.8
                print(f"{celsius * 9 / 5 + 32:.2f} °F")
            case "3":
                celsius = currentTemperature / 0.8
                print(f"{celsius + 273.15:.2f} K")
            case "4":
                celsius = currentTemperature / 0.8
                print(f"{(celsius + 273.15) * 9 / 5:.2f} °R")
            case "5":
                celsius = currentTemperature / 0.8
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "6":
                celsius = currentTemperature / 0.8
                print(f"{celsius * 0.33:.2f} °N")
            case "7":
                celsius = currentTemperature / 0.8
                print(f"{celsius * 0.525 + 7.5:.2f} °Rø")
            case _:
                print("Invalid choice")

    case "8":
        currentTemperature = float(input("Enter the temperature: "))
        print("""
Convert to:
    1. Celsius
    2. Fahrenheit
    3. Kelvin
    4. Rankine
    5. Delisle
    6. Newton
    7. Réaumur
""")

        convertChoice = input(": ")

        match convertChoice:
            case "1":
                print(f"{(currentTemperature - 7.5) / 0.525:.2f} °C")
            case "2":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{celsius * 9 / 5 + 32:.2f} °F")
            case "3":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{celsius + 273.15:.2f} K")
            case "4":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{(celsius + 273.15) * 9 / 5:.2f} °R")
            case "5":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{(100 - celsius) * 3 / 2:.2f} °De")
            case "6":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{celsius * 0.33:.2f} °N")
            case "7":
                celsius = (currentTemperature - 7.5) / 0.525
                print(f"{celsius * 0.8:.2f} °Ré")
            case _:
                print("Invalid choice")

    case _:
        print("Invalid choice")
