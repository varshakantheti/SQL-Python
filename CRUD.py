//CRUD
import psycopg
from pandas.core.indexes.multi import names_compat

from psycopg.rows import dict_row
# from tenacity import retry

def get_users(cursor):
    cursor.execute("SELECT * FROM public.dept")

    return cur.fetchall()

def select (choice):
    if choice == "all":
        users = get_users(cur)
        for user in users:
            print(user)
    else:
        users = get_users(cur)
        for user in users:
            if user["dept_no"] == int(choice):
                return user
        return "Sorry could not find anything for that department ID."

def insert (choice):
    users = get_users(cur)
    for user in users:
        if user["dept_name"] == choice:
            return "Sorry this department already exists."

    date = input("when was the last updated date?")
    cur.execute(
        "INSERT INTO public.dept (dept_name, last_updated_date) VALUES (%s, %s)",
        (choice, date))
    return (f"we have added the department {choice} to the database")

def update (choice):
    users = get_users(cur)
    myUser = None
    change = input("Would you like to update the name of the department of the last updated date? enter n for name or d for date.")
    for user in users:
        if user["dept_no"] == int(choice):
            myUser = user
            break
    if change == "n":
        name = input("What name would you like to change it to?")
        cur.execute(
            "UPDATE public.dept SET dept_name = %s WHERE dept_no = %s",
            (name, int(choice)),
        )
        return f"We have updated department {choice}"
    elif change == "d":
        date = input("What date would you like to change it to?")
        cur.execute(
            "UPDATE public.dept SET last_updated_date = %s WHERE dept_no = %s",
            (date, int(choice)),
        )
        return f"We have updated department {choice}"

def delete(choice):
    users = get_users(cur)
    for user in users:
        if user["dept_no"] == int(choice):
            cur.execute(
                "Delete from public.dept where dept_no = %s",
                (int(choice),),
            )
            return f"we have deleted the department with id: {choice}"
    return "Sorry this ID does not exist in the database."


#with psycopg.connect("dbname=firstDB user=postgres password=Royal123$") as conn:
with psycopg.connect("dbname=firstDB user=postgres password=insert password here", row_factory=dict_row) as conn:

    with conn.cursor() as cur:
        letter = input("Enter s to select data, u to update data, d to delete data, or i to insert data.")
        # select
        if letter == "s":
            choice = input("Enter which department number you would like to see. If you want them all type 'all'")
            print(select(choice))
        if letter == "u":
            choice = input("Enter the department id for the department you wish to update.")
            print(update(choice))
        if letter == "i":
            choice = input("Enter the name of the new department you would like to add.")
            print(insert(choice))
        if letter == "d":
            exists = True
            choice =  input("Enter the department id for the department you wish to delete.")
            myVal = delete(choice)
            print(myVal)
            while "does not exist" in myVal and not (choice == "no"):
                choice = input("Do you want to enter a different department ID to delete?(enter yes or no)")
                if choice == "yes":
                    choice = input("Enter the department id for the department you wish to delete.")
                    print(delete(choice))
                else:
                    print("Bye!")

