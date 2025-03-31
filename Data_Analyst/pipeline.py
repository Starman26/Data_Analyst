from Actions.analyze import analysis
from Create_Doc import create_docx

def main(path, folder,image_folder):
    #Create Analysis
    analysis(path, folder)
    # Create the report
    create_docx(image_folder)
    print("Report created successfully!")

if __name__ == "__main__":
    path = r"C:\Users\lench\Desktop\Data_Analyst\CSV\ControlSystemsData_Clean.csv"
    folder = r"C:\Users\lench\Desktop\Data_Analyst\Images"
    image_folder = r"C:\Users\lench\Desktop\Data_Analyst\Images"
    main(path, folder,image_folder)
