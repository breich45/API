#!/usr/bin/python3
import pandas

def main():

    #create a dataframe called superdf from our csv data
    superdf = pandas.read_csv("superbirthday.csv")

    # display the column names
    print(f"Column names are {', '.join(superdf)}")

    # uncomment the line below if you need to see what we are looping across
    # orient = 'records' prevents to_dict() from using the index value
    #print(superdf.to_dict(orient='records'))
    mydata = []
    for row in superdf.to_dict(orient='records'):
        mydata.append(f"\t{row['name']} was born in {row['birthday month']}.")
   
    df = pandas.DataFrame(mydata)
    df.to_csv("regularbirthday.csv", index=False)
    
    # print the total number of lines (span returns (lines, columns))
    print(f"Total lines processed {superdf.shape[0]}")
    
if __name__ == "__main__":
    main()

