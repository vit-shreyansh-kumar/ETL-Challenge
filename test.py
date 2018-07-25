from ETL_challenge import transform

if __name__ == "__main__":

    obj = transform.Transform("Challenge_me.txt")
    pr = obj.transform()
    """ write to a csv file."""
    import csv

    """ utf-8 encoded output. """
    with open("output.csv","w",encoding='utf-8') as f:
        write = csv.writer(f , quoting=csv.QUOTE_ALL)
        for x in pr:
            write.writerow(x)

    obj = transform.Transform('ETL_challenge/Challenge_me.txt')
    pr = obj.full_tranformation()
    """ write to a csv file."""
    import csv

    """ utf-8 encoded output. """
    with open("full_output.csv", "w", encoding='utf-8') as f:
        write = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in pr:
            write.writerow(x)



