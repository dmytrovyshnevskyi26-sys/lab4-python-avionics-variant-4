"""
Лабораторна робота: Варіант 4
Студент: [Вишневський Дмитро]
Група: [EIP30]
"""

# Задача 1: Кут входження в атмосферу (if/elif/else)
def check_entry_angle(angle: float) -> str:
    """
    Оцінює кут входження gamma (градуси):
    - gamma > -5.5 -> "Рикошет від атмосфери"
    - gamma < -7.5 -> "Перегрів та руйнування"
    - -7.5 <= gamma <= -5.5 -> "Вхід успішний"
    """
    angle = float(input("Enter the value of entrance angle: "))
    if angle > -5.5:
        print("Рикошет від атмосфери")
        return("Рикошет від атмосфери")
    elif angle < -7.5:
        print("Перегрів та руйнування")
        return("Перегрів та руйнування")
    else:
        print("Вхід успішний")
        return("Вхід успішний")

# Задача 2: Статус сопел орієнтації (match-case)
def nozzle_stats(nozzle_id: int, pressure: float, temperature: float) -> str:
    """
    Зіставляє словник {'nozzle_id': int, 'temp': float, 'pressure': float}:
    - temp > 400 -> "Перегрів сопла {id}"
    - pressure < 1.2 -> "Витік палива в соплі {id}"
    - штатно -> "Сопло {id} працює штатно"
    """
    match {'nozzle_id': nozzle_id, 'pressure': pressure, 'temp': temperature}:
            case {'nozzle_id': nozzle_id, 'pressure': pressure, 'temp': temperature} if pressure > 1.2 and temperature > 400:
                return ("Витік палива і перегрів сопла") 
            case {'nozzle_id': nozzle_id, 'pressure': pressure, 'temp': temperature} if pressure <= 1.2 and temperature > 400:
                return ("Перегрів сопла")
            case {'nozzle_id': nozzle_id, 'pressure': pressure, 'temp': temperature} if pressure > 1.2 and temperature <= 400:
                return ("Витік палива")
            case {'nozzle_id': nozzle_id, 'pressure': pressure, 'temp': temperature} if pressure <= 1.2 and temperature <= 400:
                return ("Сопло в нормі")
            case _:
                return ("Невідповідні вхідні дані")

# Задача 3: Перевірка цілісності пакета (for / else)
def verify_telemetry_packet(packet: list) -> str:
    """
    Перевіряє байти пакета. Якщо знайдено 0xFF -> негайно перериває (break)
    і повертає "Помилка пакета: виявлено 0xFF".
    Якщо цикл завершився без break -> повертає через else: "Пакет валідний".
    """
    ...

# Задача 4: Пошук втрати GPS (zip / enumerate)
def find_gps_loss_moments(time_list: list, sats_list: list) -> list:
    """
    За допомогою zip та enumerate знаходить перші 3 моменти часу (time),
    коли кількість супутників sats < 4.
    """
    ...
