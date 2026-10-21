# RUNNIN WILD BETA 666

import random
import time
from builtins import print

def get_tire_wear_rate(choice: str, weather) -> float:
    # Weather options to tires consuption
    if weather == "sunny":
        if choice == "soft":
            return 12.0
        elif choice == "hard":
            return 10.0
        elif choice == "wet":
            print("[!] WARNING: Wet tires wear out extremely fast on dry track!")
            return 15.0
        else:
            return 10.0
    else:  # rainy
        if choice == "wet":
            return 5.0
        elif choice == "soft":
            print("[!] WARNING: Soft tires slipping on wet track!")
            return 24.0
        elif choice == "hard":
            print("[!] WARNING: Hard tires slipping on wet track!")
            return 20.0
        else:
            return 10.0


def running_wild_race():

    # Track options (km per lap)
    track = {
        "rainbow road": 3.337,
        "highway to hell": 6.66,
        "route 66": 7.8,
        "fury road": 100
    }

    # Race distance options (km)
    race_options = {
        "A": 50,    # 50 km
        "B": 100,   # 100 km
        "C": 666  # 666 km
    }

    # Endurance options (minutes)
    endurance_options = {
        "1": 20,    # 20 min
        "2": 60,    # 60 min
        "3": 90     # 90 min
    }
    # Driver
    driver = {
        "I'M Batman" : 50,
        "Mad MAX": 200,
        "OzzY": 150,
        "Mario": 100
    }
    # Car options (kg)
    car = {
        "Kart": 2500,
        "waagh machine": 3000,
        "Bat mobile": 2700,
        "Lada": 1500,
        "Hellraiser": 666
    }

    # Engine options (L / km)
    engine = {
        "Hell": 5.7,
        "2JZ": 11.5,
        "M50": 8.5,
        "LS3": 6.3,
        "Hl69": 6.9
    }
    # Tank capacity options (Liters)
    tank_capacity_dict = {
        "small": 100,
        "medium": 200,
        "big": 500
    }

    # Horsepower options
    engine_horsepower = {
        "A": 750,
        "B": 900,
        "C": 1000,
        "D": 2500
    }

    # RPM options
    rpm_options = {
        "1": 7000,
        "2": 8000,
        "3": 9000,
        "4": 15000
    }

    print("\n" + "=" * 40)
    print("      RUNNING WILD RACE      ")
    print("=" * 40)

    # Select track
    race_track_input = input("Select race track (Rainbow road / Highway to Hell / Route 66 / Fury Road): ").strip().lower()
    lap_length = track.get(race_track_input, 6.66)

    # Choose race mode
    race_mode = input("Select Race Mode (1: Standard Distance / 2: Endurance Time): ").strip()

    if race_mode == "2":
        endurance_choice = input("Select Endurance Time (1: 20 min / 2: 60 min / 3: 90 min): ").strip()
        endurance_minutes = endurance_options.get(endurance_choice, 20)
        target_laps = int((endurance_minutes * 60) / 90)
        target_distance_str = f"Endurance ({endurance_minutes} min)"
    else:
        race_choice = input("Select race length (A: 50 km / B: 100 km / C: 666 km): ").strip().upper()
        total_race_distance = race_options.get(race_choice, 50)
        target_laps = int(total_race_distance // lap_length) + 1
        target_distance_str = f"{total_race_distance} km"

    # Initial weather setting
    weather = input("Select starting weather (sunny / rainy): ").strip().lower()
    if weather not in ["sunny", "rainy"]:
        weather = "sunny"

    # Select initial tires
    tire_choice = input("Select starting tires (soft / hard / wet): ").strip().lower()
    if tire_choice not in ["soft", "hard", "wet"]:
        tire_choice = "hard"

    # Select driver & car
    driver_option = input("select your driver (I'M Batman / MAD MAX / Ozzy / Mario): ").strip().lower()
    selected_boost: int = next(
        (boost for name, boost in driver.items() if name.lower() == driver_option),
        50
    )

    # Select car
    race_car_input = input("Select race car (Kart / Bat Mobile / Lada / Hellraiser / Waagh machine): ").strip().capitalize()
    car_weight = car.get(race_car_input, 2000)

    # Select engine
    motor = input("Select engine (R5P7 / 2JZ / M50 / LS3 / Hl69): ").strip().upper()
    fuel_consumption = engine.get(motor, 5.7)

    # Select horsepower
    hp_choice = input("Select horsepower (A: 750 / B: 900 / C: 1000 / D: 2500): ").strip().upper()
    if hp_choice not in engine_horsepower:
        hp_choice = "A"
    hp_val = engine_horsepower[hp_choice]

    # Select RPM
    rpm_input = input("Select RPM (1: 7000 / 2: 8000 / 3: 9000 / 4: 15000): ").strip()
    selected_rpm = rpm_options.get(rpm_input, 7000)

    # Performance Calculations
    base_speed_kmh = ((hp_val * 0.4) + (selected_rpm * 0.015) - (car_weight * 0.02)) * selected_boost
    if base_speed_kmh <= 0:
        base_speed_kmh = 10  # Prevent division by zero if car is too heavy


    print("\nRace Starting...")
    for countdown in range(3, 0, -1):
        print(countdown)
        time.sleep(0.4)

    print("I'M SPEED!!!\n")

    # Race Simulation Loop Variables
    lap = 1
    tank_capacity = 100.0   # Tank %
    tire_condition = 100.0  # Tire %
    total_race_time = 0.0
    pitstops_made = 0
    failed_pitstops = 0
    total_pitstop_delay = 0.0
    lap_times = []          # Race lap times

    # Safety Car - changes
    safety_car_active = False
    safety_car_laps_left = 0
    safety_car_periods = 0

    while tank_capacity > 0 and tire_condition > 0 and lap <= target_laps:

        # Dynamic weather check (15% chance per lap to switch)
        if random.random() < 0.15:
            new_weather = "rainy" if weather == "sunny" else "sunny"
            print(f"\n[WEATHER ALERT] new weather: {new_weather.upper()}!")
            weather = new_weather

        # Safety Car check / management
        if not safety_car_active and random.random() < 0.10 and lap < target_laps:
            safety_car_active = True
            safety_car_laps_left = random.randint(1, 3)
            safety_car_periods += 1
            print(f"\n[SAFETY CAR DEPLOYED] IMPS ON TRACKS {safety_car_laps_left} LAPS.")

        if safety_car_active:
            print(f"SAFETY CAR ON TRACK! Speed is controlled (Lap time: 120s, no wear/fuel drop).")
            current_lap_time = 120.0  # Slowed lap timne
            fuel_consumption_per_lap = 0.0
            tire_wear_rate = 0.0
            safety_car_laps_left -= 1
            if safety_car_laps_left <= 0:
                safety_car_active = False
                print("SAFETY CAR IN THIS LAP! Track is CLEAR on next lap!")
        else:
            # Regular lap time
            if weather == "sunny":
                fuel_consumption_per_lap = 12.5
                base_lap_time = (1.12 + 1.15) / 2 * 60
            else:
                fuel_consumption_per_lap = 7.0
                base_lap_time = (1.5 + 2.0) / 2 * 60

            # Calculate wear rate and penalties for wrong tires
            tire_wear_rate = get_tire_wear_rate(tire_choice, weather)

            lap_time_penalty = 0.0
            if weather == "rainy" and tire_choice != "wet":
                lap_time_penalty = 15.0
                print("Driving on wet track with dry tires! Heavy time penalty applied (+15s).")

            current_lap_time = base_lap_time + lap_time_penalty
            lap_times.append(current_lap_time)

        print(
            f"Lap {lap}/{target_laps} [{weather.upper()}]: Fuel {tank_capacity:.1f}%, Tires ({tire_choice}) {tire_condition:.1f}%"
        )

        # Consume fuel and tires
        tank_capacity -= fuel_consumption_per_lap
        tire_condition -= tire_wear_rate
        total_race_time += current_lap_time

        # --- PITSTOP CHECK ---
        needs_pitstop = tank_capacity <= 30 or tire_condition <= 30 or safety_car_active

        if needs_pitstop and lap < target_laps:
            if safety_car_active:
                print("\n[FREE PITSTOP OPPORTUNITY] Safety Car is on track!")
            else:
                print("\n[!] WARNING: Low fuel or high tire wear!")

            pitstop = input("Do you want to make a pitstop? (yes/no): ").strip().lower()

            if pitstop == "yes":
                print("\n---> PITSTOP! Refueling to 100%...")

                # Safety Car costs 5s penalty
                if safety_car_active:
                    pit_time = 5.0
                    print("CHEAP PITSTOP! Pitstop under Safety Car saved massive time (only +5s penalty)!")
                else:
                    pit_time = 25.0
                    # 20% for random Imps
                    if random.random() < 0.20:
                        failed_pitstops += 1
                        problem_type = random.random()

                        if problem_type < 0.50:
                            extra_delay = 15.0
                            print("PITSTOP FAIL! GOBLINGS Fighting during pitstop (+15s penalty)!")
                        elif problem_type < 0.80:
                            extra_delay = 30.0
                            print("PITSTOP FAIL! FIRE on pitstop! (+30s penalty)")
                        else:
                            extra_delay = 45.0
                            print("PITSTOP ERROR! DRIVER FIGHTING Goblings ! (+45s penalty)")

                        pit_time += extra_delay
                        total_pitstop_delay += extra_delay
                    else:
                        print("Clean pitstop!")

                tank_capacity = 100.0
                tire_choice = input("Select new tires (soft/hard/wet): ").strip().lower()
                if tire_choice not in ["soft", "hard", "wet"]:
                    tire_choice = "hard"

                tire_condition = 100.0
                pitstops_made += 1
                total_race_time += pit_time
                print(f"---> Fresh {tire_choice.upper()} tires fitted! Back to track (+{pit_time:.0f}s pitstop)!\n")

        lap += 1
        time.sleep(0.15)

    # Distance and Lap calculations
    completed_laps = lap - 1
    distance_driven = completed_laps * lap_length
    fastest_lap = min(lap_times) if lap_times else 0.0

    # Check finish state
    dnf = False
    if tank_capacity <= 0:
        print("\n[X] DNF: You ran out of fuel!")
        dnf = True
    elif tire_condition <= 0:
        print("\n[X] DNF: Your tires completely blew out!")
        dnf = True

    # Run Summary
    print("\n" + "=" * 40)
    print("RACE RESULTS")
    print("=" * 40)
    print(f"Status               : {'FINISHED' if not dnf else 'WASTED  (YOUR SOUL MINE)'}")
    print(f"Target race length   : {target_distance_str}")
    print(f"Distance driven      : {distance_driven:.2f} km ({completed_laps}/{target_laps} laps)")
    print(f"Fastest lap time     : {fastest_lap:.2f} s ({fastest_lap / 60:.2f} min)")
    print(f"Total race time      : {total_race_time:.2f} s ({total_race_time / 60:.2f} min)")
    print(f"Safety Car periods   : {safety_car_periods}")
    print(f"Pitstops made        : {pitstops_made} (Troubled pitstops: {failed_pitstops})")
    if failed_pitstops > 0:
        print(f"Pitstop time lost    : +{total_pitstop_delay:.1f} s")
    print(f"Fuel remaining       : {max(0.0, tank_capacity):.1f} %")
    print(f"Tire condition       : {max(0.0, tire_condition):.1f} %")
    print(f"Driver               : {driver_option.title()}")
    print("=" * 40)

    return race_car_input, driver_option, round(total_race_time, 2), round(fastest_lap, 2)


def main():
    all_results = []
    run_number = 1

    while True:
        car_name, driver_name, run_time, fastest_lap = running_wild_race()

        # Save record
        run_label = f"{driver_name.title()} ({car_name}) ({run_number})"
        all_results.append({
            "label": run_label,
            "driver": driver_name,
            "car": car_name,
            "time": run_time,
            "fastest lap": fastest_lap
        })
        run_number += 1

        # Sort results from fastest to slowest
        sorted_results = sorted(all_results, key=lambda x: x["time"])

        # Display Standings
        print("\n" + "=" * 55)
        print("LEADERBOARD (FASTEST TO SLOWEST)".center(55))
        print("=" * 55)
        print(f"{'Rank':<6}{'Car / Run':<30}{'Time (s)':<10}")
        print("-" * 55)

        for rank, record in enumerate(sorted_results, start=1):
            print(f"{rank:<6}{record['label']:<30}{record['time']:<10.2f}")
        print("-" * 55)

        # Rerun prompt
        again = input("\nWould you like to RUNNING WILD AGAIN? (yes/no) [yes]: ").strip().lower()
        if again == 'no':
            print("\nThanks for RUNNING WILD! Final RUNNING saved.")
            break

def new_func():
    car_name, driver_name, run_time = running_wild_race()


if __name__ == "__main__":
    main()
