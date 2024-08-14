import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('archive/Australian Vehicle Prices.csv')

Australian_Vehicle_Prices_df = pd.read_csv('archive/Australian Vehicle Prices.csv',
                            header=None,
                            names=['Engine', 'DriveType', 'Model'])

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(Australian_Vehicle_Prices_df)

def showCharts():
    Australian_Vehicle_Prices_df.plot(
                    kind='bar',
                    x='Country',
                    y='AUD',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Australian Vehicle Prices Extraordinaire!
            
        Please select an option:
        1 - Show the original dataset
        2 - Show the updated Data Frame
        3 - Visualise the cost of Car Prices
        4 - Quit Program
            """)

    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('Choose a Car model and I will tell you the engine and Drivetype!')

    except:
        print('Damn bro, I dont got all day')

   

#----Main program----#
while not quit:
    userOptions()