import math 

stock_values = 1

# The E24 Series of PVNS Values https://learnabout-electronics.org/Resistors/resistors_05.php
if stock_values == 0:
	resistor_values = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91]

# Currently Owned Resistors (in kOhm): 
# resistor_values = [10, 10.5, 5.1, 4.53, 4.12, 15.8, 392, 23.7, 147, 1.5, 61]
if stock_values == 1:
	resistor_values = [0.392, 0.500, 0.510, 0.665, 0.680, 1.5, 2.4, 4.12, 4.53, 4.7, 5.1, 10, 10.5, 15, 15.8, 18, 23.7, 26.1, 40.4, 53.6, 60.4, 66.5, 86.6, 90.9, 95.3, 100, 124, 147, 392]

Vh = 3.3
Vl = 0.8


# Resistor divider gain
valGain = (Vl)/(Vh)
# Manual Gain Override
# valGain = 14
 
pvns_results = []

for R1 in resistor_values:
	for R2 in resistor_values:

		entry = {}
		entry["R1"] 	= R1
		entry["R2"] 	= R2
		entry["gain"] 	= abs(R2/(R1+R2))
		entry["err%"] 	= abs(100 * (entry["gain"] - valGain) / valGain)
		entry["Vh_alt"]	= Vl * (R2 + R1) / R2
		entry["Vl_alt"]	= Vh * R2 / (R2 + R1)
		pvns_results.append(entry);

pvns_results_sorted = sorted(pvns_results, key=lambda k: k["err%"]) 

print("### BEST MATCHES ###\n")
print("Rank \t R1 \t\t R2 \t\t Gain \t\t err% \t\tVh_alt \t\t   Vl_alt")
for i in range(10):
	print( i, 											" \t\t", end =" ")
	print( f"{(pvns_results_sorted[i])['R1']:.3f}",		" \t", end =" ")
	print( f"{(pvns_results_sorted[i])['R2']:.3f}",		" \t", end =" ")
	print( f"{(pvns_results_sorted[i])['gain']:.6f}", 	" \t", end =" ")
	print( f"{(pvns_results_sorted[i])['err%']:.6f}", 	" \t", end =" ")
	print( f"{(pvns_results_sorted[i])['Vh_alt']:.6f}", 	" \t", end =" ")
	print( f"{(pvns_results_sorted[i])['Vl_alt']:.6f}", 	" \t", end =" ")
	print(  )





############Code Archive#############

# 		if (this_gain < closestGain): 

# 			if not closestGain == closestGain_prev:
# 				closestR1_prev = closestR1
# 				closestR2_prev = closestR2
# 				closestGain_prev = closestGain

# 			closestR1 = R1
# 			closestR2 = R2
# 			closestGain = this_gain

# 		elif (closestGain < this_gain) and (this_gain < closestGain_prev):
# 			closestR2_prev = closestR2
# 			closestR1_prev = closestR1
# 			closestGain_prev = this_gain
# 		# if stock_values == 0:
# 		# 	if (abs((R2*10/R1) - valGain) < abs((closestR2/closestR1) - valGain)):
# 		# 		closestR1 = R1
# 		# 		closestR2 = R2*10
# 		# 	elif (abs((R2*0.1/R1) - valGain) < abs((closestR2/closestR1) - valGain)):
# 		# 		closestR1 = R1
# 		# 		closestR2 = R2*0.1


# print("### BEST MATCH ###")
# print("R1: \t\t", closestR1)
# print("R2: \t\t", closestR2)
# print("Ratio: \t\t", f"{closestR2 / closestR1:.6f}")
# print("Error %: \t", f"{(((closestR2 / closestR1) - valGain) / (closestR2 / closestR1) * 100):.6f}")
# print("Vh_alt: \t", f"{Vl*((closestR1 + closestR2) / (closestR2)):.6f}")
# print("Vl_alt: \t", f"{Vh*(closestR2 / (closestR1 + closestR2)):.6f}")
# print("")

# print("### NEXT BEST MATCH ###")
# print("R1_prev: \t\t", closestR1_prev)
# print("R2_prev: \t\t", closestR2_prev)
# print("Ratio: \t\t", f"{closestR2_prev / closestR1_prev:.6f}")
# print("Error %: \t", f"{(((closestR2_prev / closestR1_prev) - valGain) / (closestR2_prev / closestR1_prev) * 100):.6f}")
# print("Vh_alt: \t", f"{Vl*((closestR1_prev + closestR2_prev) / (closestR2_prev)):.6f}")
# print("Vl_alt: \t", f"{Vh*(closestR2_prev / (closestR1_prev + closestR2_prev)):.6f}")
# print("")


