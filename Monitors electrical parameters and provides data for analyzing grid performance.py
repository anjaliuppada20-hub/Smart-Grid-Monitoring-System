# Smart-Grid-Monitoring-System
Monitors electrical parameters and provides data for analyzing grid performance
import random
import time

print("===== SMART GRID MONITORING SYSTEM =====")

total_energy = 0

for i in range(10):
    voltage = random.uniform(220, 240)
    current = random.uniform(5, 20)
    frequency = random.uniform(49.5, 50.5)

    power = voltage * current
    energy = power / 3600000
    total_energy += energy

    print("\n--- GRID DATA ---")
    print(f"Voltage   : {voltage:.2f} V")
    print(f"Current   : {current:.2f} A")
    print(f"Power     : {power:.2f} W")
    print(f"Frequency : {frequency:.2f} Hz")

    if voltage < 220 or voltage > 240:
        print("Status: VOLTAGE FAULT")
    elif frequency < 49.5 or frequency > 50.5:
        print("Status: FREQUENCY FAULT")
    else:
        print("Status: GRID NORMAL")

    time.sleep(1)

print("\n===== MONITORING COMPLETE =====")
print(f"Total Energy: {total_energy:.6f} kWh")
