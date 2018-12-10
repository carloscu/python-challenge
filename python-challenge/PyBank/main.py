# Modlules
import os
import csv

#Set Path
csvpath = os.path.join('.','Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
   
    #CSV reader to specify delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    Total = 0 
    Average = 0
    Months = sum(1 for row in csvreader) 

    #Total_Amount = sum (1 for row in csvreader(1))
    #Total_Amount = sum(int(row[1]) for row in csvreader

    for row in csvreader:         
        #Total_Amount += float(row[1])
        Total = sum(float(row[1]) for row in csvreader)
        print(Total)    
        Average = sum(float(row[1])/len(row[1]) for row in csvreader)
        print(Average)             


    print(" ")
    print("Financial Analysis")
    print("---------------------")
    print("Total Months: " + str(Months))
    print(f"       Total: {Total}")
    print(f"     Average: {Average}")

#Zip List
budget_summary_csv = zip(Months,Total,Average)

#Specify the file to write to
output_path = os.path.join('.','Output','budget_summary.csv')
#output_path = os.path.join('"budget_summary.csv")

#Open the file to 'write mode'
with open(output_path,'w', newline='') as datafile:
    
    #initialize csv.writer
    writer = csv.writer(datafile)

    #write in zipped rows
    writer.writerows(budget_summary_csv)


    #csvwriter = csv.writer(datafile, delimiter=',')


