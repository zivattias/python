m_income = int(input("Enter your monthly income: "))
y_income = m_income * 12
tax = 0
if y_income >= 77_401:
    if y_income < 110_881:
        tax += (y_income - 77_400) * 0.14 + 77_400 * 0.1
    else:
        tax += (110_880 - 77_400) * 0.14 + 77_400 * 0.1

if y_income >= 110_881:
    if y_income < 178_081:
        tax += (y_income - 110_880) * 0.2
    else:
        tax += (178_080 - 100_880) * 0.2

if y_income >= 178_081:
    if y_income < 247_441:
        tax += (y_income - 178_080) * 0.31
    else:
        tax += (y_income - 178_080) * 0.31

# continue here:
            if y_income >= 247_441:
                tax += (y_income - 247_440) * 0.35

                if y_income >= 514_921:
                    tax += (y_income - 514_920) * 0.47

                    if y_income >= 663_241:
                        tax += (y_income - 663_240) * 0.5
    print(f"For a monthly salary of {m_income}, you earn {y_income} annually. Tax to be paid: {tax}")
else:
    if y_income <= 77_400:
        tax += y_income * 0.1
        print(f"For a monthly salary of {m_income}, you earn {y_income} annually. Tax to be paid: {tax}")
    else:
        print("Invalid input.")
