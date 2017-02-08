magicians = ["alice", "bob", "rome"]
shoes = ["nike", "adidas", "chanel"]


for magician in magicians:
    print(magician.title() + " is ugly.")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone.That was awesome!" + "\n")

for shoe in shoes:
    print(shoe.title() + " is expensive")
    print("Someday I will buy each pair of formal shoes." + "Plus this brand " + shoe.title())
