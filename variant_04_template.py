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
    if angle > -5.5:
        return("Рикошет від атмосфери")
    elif angle < -7.5:
        return("Перегрів та руйнування")
    else:
        return("Вхід успішний")

# Examples for input values for task 1
print(check_entry_angle(-6.0))
print(check_entry_angle(-4.0))
print(check_entry_angle(-8.0)) 


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

# Examples for input values for task 2
print(nozzle_stats(1, 1.5, 450)) 
print(nozzle_stats(2, 1.0, 300.0))


# Задача 3: Перевірка цілісності пакета (for / else)
def verify_telemetry_packet(checksums: list) -> str:
    """
    Перевіряє байти пакета. Якщо знайдено 0xFF -> негайно перериває (break)
    і повертає "Помилка пакета: виявлено 0xFF".
    Якщо цикл завершився без break -> повертає через else: "Пакет валідний".
    """
    for byte in checksums:
        if byte == 0xFF:
            print("Виявлено байт помилки 0xFF! Обробку зупинено.")
            result = "Пакет пошкоджено"
            break
        else:
            result = "Пакет валідний"
    return(result)

# Examples for input values for task 3
print(verify_telemetry_packet([0x12, 0xAB, 0xFF, 0x04]))
print(verify_telemetry_packet([0x12, 0xAB, 0x04, 0x05]))


# Задача 4: Пошук втрати GPS (zip / enumerate)
def find_gps_loss_moments(time_list: list, sats_list: list) -> list:
    """
    За допомогою zip та enumerate знаходить перші 3 моменти часу (time),
    коли кількість супутників sats < 4.
    """
    found_count = 0
    loss_moments = []
    for index, (t, sat) in enumerate(zip(time_list, sats_list)):
        if sat < 4:
            found_count += 1
            loss_moments.append((t, sat))
            if found_count == 3:
                print("Знайдено 3 моменти втрати GPS.")
                break
    return loss_moments

# Examples for input values for task 4
print(find_gps_loss_moments([0, 1, 2, 3, 4, 5], [5, 3, 2, 6, 5, 4]))
print(find_gps_loss_moments([0, 1, 2, 3, 4, 5], [2, 1, 3, 8, 3, 10]))