# Learn truth tables in the book.
# 1. True and True   True
print(True and True)
print(f"1. My guess: True\n\n")

# 2. False and True   False
print(False and True)
print(f"2. My guess: False\n\n")

# 3. 1 == 1and2 == 1   
print(1 == 1 and 2 == 1)
print(f"3. My guess: False\n\n")

# 4. "test" == "test"   
print("test" == "test")
print(f"4. xMy guess: True\n\n")

# 5. 1 == 1or2 != 1   
print(1 == 1 or 2 != 1)
print(f"5. My guess: True\n\n")

# 6. True and1 == 1   
print(True and 1 == 1)
print(f"6. My guess: True\n\n")

# 7. False and 0 != 0   
print(False and 0 != 0)
print(f"7. My guess: False\n\n")

# 8. True or1 == 1   
print(True or 1 == 1)
print(f"8. My guess: True\n\n")

# 9. "test" == "testing"   
print("test" == "testing")
print(f"9. My guess: False\n\n")

# 10. 1 != 0and2 == 1   
print(1 != 0 and 2 == 1)
print(f"10. My guess: False\n\n")

# 11. "test" != "testing"   
print("test" != "testing")
print(f"11. My guess: True\n\n")

# 12. "test" == 1   
print("test" == 1)
print(f"12. My guess: False\n\n")

# 13. not (True and False)   
print(not (True and False))
print(f"13. My guess: True\n\n")

# 14. not(1 == 1and0 != 1)   
print(not(1 == 1 and 0 != 1))
print(f"14. My guess: False\n\n")

# 15. not (10 == 1 or 1000 == 1000)   
print(not (10 == 1 or 1000 == 1000))
print(f"15. My guess: False\n\n")

# 16. not(1 != 10or3 == 4)   
print(not(1 != 10 or 3 == 4))
print(f"16. My guess: False\n\n")

# 17. not ("testing" == "testing" and "Zed" == "Cool Guy"   
print(not ("testing" == "testing" and "Zed" == "Cool Guy"))
print(f"17. My guess: True\n\n")

# 18. 1 == 1 and (not ("testing"==1or1 == 0))
print(1 == 1 and (not ("testing" == 1 or 1 == 0)))
print(f"18. My guess: True\n\n")

# 19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3))   
print("chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print(f"19. My guess: False\n\n")

# 20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))   
print(3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")))
print(f"20. My guess: False\n\n")

