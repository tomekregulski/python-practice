print("How many kilometers did you cycle today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Ok, that is equal to {miles} miles")