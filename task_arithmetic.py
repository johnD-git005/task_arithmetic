allowance = 2000

# QUESTION 1
print("")

print("QUESTION 1")

print("Spent ₦400 on Books ")
allowance -= 400
print(f"Your Balance after spending on Books is ₦{allowance}")

# QUESTION 2
print("")

print("QUESTION 2")

print("Found ₦100 and Added to your Allowance")
allowance += 100
print(f"Your New Balance after adding ₦100 is ₦{allowance}")

# QUESTION 3
print("")

print("QUESTION 3")

print("You bought snacks worth ₦250")
allowance -= 250
print(f"Your new Balance after buying snacks is ₦{allowance}")

# QUESTION 4
print("")

print("QUESTION 4")

print("You gave 25% of your current allowance to your younger siblings")
allowance -= (allowance * 0.25)
#allowance -= (allowance * 25) / 100
print(f"Your new balance after giving 25% to your younger sibling is ₦{allowance}")

# QUESTION 5
print("")

print("QUESTION 5")

print("You use one third of what's left to buy data")
allowance -= allowance / 3
print(f"New Balance is ₦{allowance}")

# QUESTION 6
print("")

print("Question 6")
print("You split the remaining balance equally between Savings and Tithing")
allowance //= 2
print(f"Balance: ₦{allowance}")

# QUESTION 7
print("")

print("QUESTION 7")
print("Balance of what remains after removing all complete ₦100 notes using the modulus operator")
allowance %= 100
print(f"Modulus ₦{allowance}")
