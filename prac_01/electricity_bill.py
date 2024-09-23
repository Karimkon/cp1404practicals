TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")

tariff_choice = input("which tariff was used? ")
if tariff_choice == "11":
    price_per_kwh = TARIFF_11
elif tariff_choice == "31":
    price_per_kwh = TARIFF_31
else:
    print("Invalid tariff choice!")
    price_per_kwh = 0

if price_per_kwh > 0:
    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    estimated_bill = price_per_kwh * daily_use * billing_days
    print(f"Estimated bill: ${estimated_bill}")
