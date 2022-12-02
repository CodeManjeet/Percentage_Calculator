def main():
    print("Welcome To Percentage Calculator \n Where You Can Calculate Your PT 1 Marks And Halfyealy Marks")
    print("Note : Who Students Get Passed In Both Or Even One \n Slap Them")
    print("Ok Bakwas To Hote Rahegi To Chaliye Shuru Karte Hai")
    a = input("Which Percentege You Wants To See If PT 1 So Type PT 1 Or Halfyearly So Write Halfyearly")
    m = int(input("Ok I Got It Enter Your Marks :-"))
    b = m/200*100
    c = m/370*100
    if a == "PT 1":
        print("Your PT 1 Percentage Is :-" , b)
    if a == "Halfyearly":
        print("Your Halfyearly Precentage Is :-" , c)
    r = input("Would You Try Again ? \n If Yes Simply Type Y Or No Type N").lower()
    if r == "Y":
        main()
    if r == "N":
        print("Thanks For Using This Calculator Is Made By Manjeet Singh If You Want More Customised Code Simple Search In Google 'github.com/CodeManjeet'")
    else:
        print("Invalid Input Found Please write Valid Input")
        print(r)
main()