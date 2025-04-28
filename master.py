import time

#Step 1: we need to ask for input from the user

name = input("Enter your name: ")
city = input("Enter your city: ")
hobby = input("Enter your hobby: ")
favorite_color = input("Enter your favorite color: ")
spirit_animal = input("Enter your spirit animal: ")
age = int(input("Enter your age: "))
favorite_food = input("Enter your favorite food: ")

#Step 2: we need to print some statement by using import time

print("🏸 Scanning colors, foods, and animals energies...")
time.sleep(3)
print("🌟 Calculating your personality type using complex non-scientific logic...")
time.sleep(3)
print("🎉 Hey", name + ", here's your fun personality report!")

#step 3: now we need to write if and elif statement for age to define title

if age < 18:
    title = "Young Explorer"
elif age >= 18 and age <= 30:
    title = "Adventurer"
else:
    title = "Wise Owl"

#step 4: now we need to define personality code by defining length

personality_code = name[:3] + spirit_animal[:2] + favorite_food[:3]

if len(hobby) < 7:
    hobby_comment = "💡 Time to explore more hobbies? You've got hidden sparks waiting!"
else:
    hobby_comment = "✨ Seems you have a good height and that hobby says a lot about your vibe!"

#step 5: now basis on the input results we need to print the final result

print("🙌 Hey", name.title() + ", here is your fun personality report!")
print("🌆 You're from", city.title() + ", a place of dreams")
print(f"🍿 You love {favorite_food.lower()} and enjoy doing {hobby.lower()}.")
print(f"🎨 You vibe with the color {favorite_color.upper()} and your spirit animal is the {spirit_animal.title()}.")
print(f"📅 You've lived approximately {age*12} months already.")
print(f"🧩 You belong to the '{title}' tribe.")
print(f"🔐 Your Secret Personality Code is: 💡 {personality_code}")
print(hobby_comment)
print("🌈 You are officially certified as: FUNKY AND FABULOUS! 😍")