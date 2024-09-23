def main():
    tariffs = {
        11: 0.244618,
        31: 0.136928,
        45: 0.198752,
        50: 0.179512,
        55: 0.158620
    }

    print("Electricity Bill Estimator 2.0")
    print("Available tariffs:", ", ".join(map(str, tariffs.keys())))

    while True:
        try:
            tariff_choice = int(input("Which tariff? "))
            if tariff_choice in tariffs:
                break
            else:
                print("Invalid tariff. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))

    estimated_bill = tariffs[tariff_choice] * daily_use * billing_days
    print(f"Estimated bill: ${estimated_bill:.2f}")


if __name__ == "__main__":
    main()
