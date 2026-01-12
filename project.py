'''SKY BUS
Journey Details:
Start Location :done
End Location :done
Pick up location:
drop location :
Number of Passangers :done
Discount :
Couch Type :done
Journey Date :done
Journey Time :Day / Night-done
Meals:
Distance in KM :
Fare Per KM :
Payment Method :done

Ticket
Start to End :
Couch type :
Total Number Of Passangers :
Journey Date:
Journey Time :
Total Distance :
Total Fare :

Rating for our service:
feedback for our service:
______________Thank you for choosing our service_______________________
______________________________________________________________________________________'''
import random

class SKY_BUS:
    def __init__(self):
        self.stops_distance = {
            "Delhi": 0, "Jaipur": 280, "Ahmedabad": 950, "Mumbai": 1400,
            "Pune": 1470, "Nagpur": 1050, "Bhopal": 780, "Indore": 820,
            "Lucknow": 550, "Kanpur": 470, "Agra": 230,
            "Patna": 1000, "Kolkata": 1500,
            "Chennai": 2200, "Bangalore": 2150, "Hyderabad": 1600,
            "Coimbatore": 2450, "Madurai": 2550,
            "Trivandrum": 2900,
            "Kochi": 2700,
            "Panaji": 1900
        }

        # PICKUP & DROP
        self.Pickup_Point = [
            "Main Bus Stand","Railway Station","Airport","City Center","Metro Station",
            "Bypass","Shopping Mall","University Gate","Hospital Stop","Tech Park",
            "Industrial Area","Hotel Zone","Town Hall","Old Bus Stop",
            "New Bus Terminal","Highway Point","Petrol Bunk",
            "Police Station","City Crossroad","Market Yard"
        ]

        self.Drop_Point = [
            "Central Bus Terminal","Railway Junction","Airport Terminal","Tourist Area",
            "Hotel Area","Market Area","Business District","IT Park",
            "Metro Gate","Residential Area","Industrial Hub","Shopping Complex",
            "City Outskirts","Main Junction","University Area","Hospital Zone",
            "Town Center","Suburban Area","Highway Exit","Harbor Point"
        ]

        self.stops = list(self.stops_distance.keys())
        self.Booking_id = ""
        self.Start = ""
        self.End = ""
        self.Pickup= ""
        self.Drop = ""
        self.Passengers = 0
        self.Discount = 0
        self.Couch_type = ""
        self.Journey_date = ""
        self.Journey_month = ""
        self.journey_year = ""
        self.Journey_time = ""
        self.Distance = 0
        self.Fare = 0
        self.Payment_Method = ""
        self.Total_Fare=0
        self.Seats =[]
        self.Return_Date = ""
        self.Return_Month = ""
        self.Return_year = ""
        self.Return_Fare = 0
        self.Travel_hours = 0
        self.Break_taken="No"
        self.Break_hours=0
        self.Hotel_name = ""
        self.Hotel_cost = 0
        
    #show stops
    def Show_stops(self):
        print("\n========== WELCOME TO SKY_BUS ==========\n")
        print("\n========== AVAILABLE BUS TRIPS ==========\n")
        for i in self.stops:
            print("-",i)
            
    def Show_pickup(self):
        print("\n-------- PICKUP POINTS --------")
        for i,j in enumerate(self.Pickup_Point,1):
            print(i,".",j)
            
    def Show_Drop(self):
        print("\n-------- DROP POINTS --------")
        for i,j in enumerate(self.Drop_Point,1):
            print(i,".",j)

    def get_details(self):
        self.Show_stops()
        
        print("\n======  BOOKING FORM ======\n")

        self.Start=input("\nEnter the Start location: ").strip().title()
        self.End = input("Enter the End location: ").strip().title()
        
        if (self.Start not in self.stops or self.End not in self.stops) or(self.Start==self.End) :
            print(("❌ Invalid Location Selected!"))
            return False
        
        print(f"\n====== Distance will be auto-calculated from {self.Start} to {self.End} ======\n")
        
        self.Show_pickup()
        
        #pickup
        p = int(input("\nEnter the Pickup point Number: "))
        if p<1 or p>(len(self.Pickup_Point)):
            print("❌ Invalid pickup")
            return False
        self.Pickup=self.Pickup_Point[p-1]
        
        self.Show_Drop()
        #drop
        d = int(input("\nEnter the Drop point Number: "))
        if d<1 or d>(len(self.Drop_Point)):
            print("❌ Invalid pickup")
            return False
        self.Drop=self.Drop_Point[d-1]
        print("\n====== Passangers list ======\n")
        
        self.Passengers = int(input("\nEnter the Number of Passangers: "))
        if self.Passengers<=0 or self.Passengers>=56:
            print("❌ Invalid Passenger Count!")
            return False
        
        print(f"\n====== Now we have {self.Passengers} Passangers let's move on to the Coach type ======\n")
        print("\nChoose Coach Type:")
        print("1. AC (₹900)")
        print("2. Non-AC (₹650)")
        print("3. Sleeper (₹1100)")
        
        C_t = int(input("Enter the choice: "))
        
        if C_t==1:
            self.Couch_type="AC"
            self.Fare = 900
        elif C_t == 2:
            self.Couch_type = "Non-AC"
            self.Fare = 650
        elif C_t == 3:
            self.Couch_type = "Sleeper"
            self.Fare = 1100
        else:
            print("Invalid Coach Type!")
            return False
            
        print(f"\n====== Greart you have selected the {self.Couch_type} Coach type ======\n")
        
        print("\n====== Enter your Journey Date ======\n")
        #date
        J_d = int(input("Enter the Date (1-31): "))
        if not (1 <= J_d <= 31):
            print("❌ Invalid Day!")
            return False
        
        #month
        J_M = int(input("Enter the Month (1-12): "))
        if not (1<=J_M<=12):
            print("❌ Invalid Month!")
            return False
        
        #year
        J_y = int(input("Enter the Year (2025-2026): "))
        if not (2025<=J_y<=2026):
            print("❌ Invalid Year!")
            return False
        
        self.Journey_date=J_d
        self.Journey_month=J_M
        self.journey_year=J_y
        
        print(f"\n====== Your ticket has been booked on {self.Journey_date}/{self.Journey_month}/{self.journey_year} ======\n")
        
        print("\nJourney Time")
        print("1. Morning")
        print("2. Afternoon")
        print("3. Evening")
        print("4. Night (+₹120) per passenger")
        
        J_time = int(input("Enter the Time : "))
        if J_time == 1:
            self.Journey_time = "Morning"
        elif J_time == 2:
            self.Journey_time = "Afternoon"
        elif J_time == 3:
            self.Journey_time = "Evening"
        elif J_time == 4:
            self.Journey_time = "Night"
        else:
            print("Invalid time !")
            return False       
        
        print(f"\n====== OK you will travel on {self.Journey_time} ======\n")
        
        
        print("\nPayment Mode")
        print("1. UPI")
        print("2. Debit Card")
        print("3. Cash")
        print("4. VIA INDIAN BANK APP")
        
        P = int(input("Enter Payment Method: "))
        if P==1:
            self.Payment_Method = "UPI"
        elif P==2:
            self.Payment_Method = "Debit Card"
        elif P==3:
            self.Payment_Method = "Cash"
        elif P==4:
            self.Payment_Method = "VIA INDIAN BANK APP"
        else:
            print("Invalid type !")
            return False
            
        print(f"\n====== Oh you will using {self.Payment_Method} for Payment ======\n")
        print("\nIf you want return ticket if yes then Enter(y)")
                
        #Return ticket
        Rt = input("\nReturn Ticket? (y/n): ").lower()
        if Rt == "y":
            print("\n====== Enter Return Journey Date ======\n")

            # DAY
            R_d = int(input("Enter Return Day (1–31): "))
            if not (1 <= R_d <= 31):
                print("❌ Invalid Return Day!")
                return False   

            # MONTH
            R_m = int(input("Enter Return Month (1–12): "))
            if not (1 <= R_m <= 12):
                print("❌ Invalid Return Month!")
                return False

            # YEAR
            R_y = int(input("Enter Return Year (2025–2026): "))
            if not (2025 <= R_y <= 2026):
                print("❌ Invalid Return Year!")
                return False

            # check return > journey
            journey_val = self.journey_year*10000 + self.Journey_month*100 + self.Journey_date
            return_val  = R_y*10000 + R_m*100 + R_d

            if return_val < journey_val:
                print("❌ Return Date cannot be before Journey Date!")
                return False

            self.Return_Date  = R_d
            self.Return_Month = R_m
            self.Return_year  = R_y

            
        print("\n✅ Booking details saved successfully!")
        return True

        
    #Distance
    def CAL_distance(self):
        self.Distance = abs(self.stops_distance[self.Start] - self.stops_distance[self.End])
        print("\n✅ Distance:", self.Distance, "KM")
        
        #travel time
        Avg_speed = 60
        self.Travel_hours=round(self.Distance/Avg_speed,2)
        print(f"🕒 Estimated Travel Time (no break): {self.Travel_hours} hours")

        Ask_break = input("\nDo you want to take a break during travel? (y/n): ").lower()
        if Ask_break=="y":
            self.Break_taken="yes"
            #hotel name
            hotels = {
                "Hotel Highway Inn": 1200,
                "Hotel Rest & Go": 1500,
                "Hotel Comfort Stay": 1000
            }
            
            print("\n🏨 Available Hotels for Break:")
            for i,j in hotels.items():
                print(f"- {i} : ₹{j}")
                
            self.Hotel_name = input("\nChoose Hotel Name: ").strip().title()
            
            if self.Hotel_name in hotels:
                self.Hotel_cost = hotels[self.Hotel_name]
                print(f"🏨 Selected Hotel: {self.Hotel_name} (₹{self.Hotel_cost})")
            else:
                print("❌ Invalid hotel! No hotel selected.")
                self.Hotel_name=""
                self.Hotel_cost=0
                
            self.Break_hours=float(input("\nEnter break duration (in hours): "))

            self.Travel_hours += self.Break_hours
            print(f"\n🛑 Break Added! Total Travel Time is now {self.Travel_hours} hours")
        else:
            self.Break_taken="No"


    #generate id
    def b_id(self):
        self.Booking_id = "SKY"+str(random.randint(10000,99999))
    
    #generate seats
    def seat(self):
        total_seats=list(range(1,56))
        self.Seats=random.sample(total_seats, self.Passengers)        
            
    #fare
    def cal_fare(self):
        print("\n✅ Calculating Fare...")

        Base_fare=self.Fare*self.Passengers
        
        # BUSINESS PRICING PER KM
        if self.Distance > 2500:
            Base_fare+=500 *self.Passengers
        elif self.Distance > 2000:
            Base_fare+=350 * self.Passengers
        elif self.Distance > 1500:
            Base_fare+=250 *self.Passengers
        elif self.Distance > 1000:
            Base_fare+=150 *self.Passengers
            
        print("📌 🚌 Base Fare:", Base_fare)
        print("📌 Seat Fare per Passenger:", self.Fare)
        print("📌 Distance Charge Applied Based on KM")

        #night charge  
        if self.Journey_time == "Night":
            Base_fare+=120 *self.Passengers
            print("🌙 Night charges added")
            
        if self.Hotel_cost>0:
            Base_fare+=self.Hotel_cost
            print("🏨 Hotel cost added:", self.Hotel_cost)

        self.discount(Base_fare)
        
        #Return ticket fare calculation
        if self.Return_Date !="":
            self.Return_Fare = round(self.Total_Fare * 0.9,2) #10% off
    
    
    #Discount
    def discount(self,Base_fare):
        
        self.Discount =0
        #grp passangerz
        if self.Passengers>=5:
            self.Discount+=5 #5% grp dis
            print("🎉 Group Discount Applied (5%)")
        
        #couple + Indian bank app subscribers 
        if self.Passengers==2 and self.Payment_Method=="VIA INDIAN BANK APP":   
            self.Discount+=3 #couple+app dis
            print("🎉 Couple + Bank App Discount (3%)")
            
        discount_amount = (Base_fare*self.Discount)/100
        print("💸 Discount Amount:", discount_amount)

        self.Total_Fare = round(Base_fare-discount_amount,2)
    
    
    # TICKET    
    def print_ticket(self):
        
        print("\n=========== SKY BUS TICKET ===========")
        print("Booking ID:", self.Booking_id)
        print("Route :", self.Start, "➡", self.End)
        print("Pickup:", self.Pickup)
        print("Drop:", self.Drop)
        print("Distance :", self.Distance, "KM")
        print("Coach :", self.Couch_type)
        seats= ["S"+str(i) for i in self.Seats]
        print("Seats:", ", ".join(seats))
        print("Passengers :", self.Passengers)
        print("Journey Date:", f"{self.Journey_date}/{self.Journey_month}/{self.journey_year}")
        print("Time :", self.Journey_time)
        print("Estimated Travel Time:", self.Travel_hours, "Hours")
        print("Break Taken:", self.Break_taken)
        
        if self.Break_taken == "yes":
            print("Break Duration:", self.Break_hours, "Hours")
            print("Hotel Name:", self.Hotel_name)
            print("Hotel Cost: ₹", self.Hotel_cost)
            
        print("Fare per Seat :", "₹", self.Fare)
        print("Payment Mode :", self.Payment_Method)
        print("Discount :", self.Discount, "%")
        print("Total Fare :", "₹", self.Total_Fare)
        
        if self.Return_Date != "":
            print("\n----- RETURN JOURNEY -----")
            print("Return Date:", f"{self.Return_Date}/{self.Return_Month}/{self.Return_year}")
            print("Return Fare (10% OFF): ₹",self.Return_Fare)
        print("=====================================")
        
    def Feedback(self):
        r = input("\n⭐ Rate our booking service (1-5): ")
        f = input("📝 Feedback: ")

        print("\n✅ Thank you!")
        print("Rating:", r)
        print("Feedback:", f)
        print("\n_____ THANK YOU FOR CHOOSING SKY BUS _____")
        print("🚍 Visit Again!")

# ======= MAIN MENU =======
Booking_Record = None
while True:
    print("\n======= SKY BUS MENU =======")
    print("1. Book Ticket")
    print("2. View Last Ticket")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        SB = SKY_BUS()
        SB.get_details()
        
        if SB.Start == "" or SB.End == "":
            continue
        
        SB.CAL_distance()
        SB.seat()
        SB.b_id()
        SB.cal_fare()
        SB.print_ticket()
        
        Booking_Record = SB
        
        SB.Feedback()
        
    elif choice == "2":
        if Booking_Record is None:
            print("\n❌ No ticket booked yet!")
        else:
            print(f"{Booking_Record.Booking_id} | {Booking_Record.Start} -> {Booking_Record.End} | {Booking_Record.Passengers} Pax | ₹{Booking_Record.Total_Fare}")
            
    elif choice =="3":
        print("\n🚍 Exiting SKY BUS System… Thank you!")
        break
    else:
        print("❌ Invalid choice! Try again.")
