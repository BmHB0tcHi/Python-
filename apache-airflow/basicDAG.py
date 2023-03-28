'''
    A basic DAG (Direct Acyclic Graph) implementation using apache airflow
'''


import airflow
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow import DAG


FILENAME = "/home/user_name/airflow_test.txt"
def read_sample_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print ("File is not found / does not exist")

# Creating a dag
'''
    scheduling params
    1) start_date = datetime.datetime(year=x, month=y, day=z)
    2) schedule_interval = @daily/@monthly/...
    3) end_date = datetime.datetime(year=x, month=y, day=z)
    if end_date is none, airflow will run this DAG forever!
'''
dag = DAG(
    dag_id="Simple_Dag",
    start_date=airflow.utils.dates.days_ago(14),
    schedule=None
)

# A bash operator to write "hello" to airflow_test.txt
write_echo = BashOperator(
    task_id = 'Write_Echo',
    bash_command=f"echo 'hello' >> {FILENAME}",
    dag=dag
)

# Python operator to read the airflow_test.txt file and print to screen its contents
print_hello = PythonOperator(
    task_id = "Read_file",
    python_callable=read_sample_file,
    # arguements to the python callable can be passed throught a dictionary mapping arguments
    # to their value
    op_args={"filename" : FILENAME},
    dag = dag,
)

# Defining the flow of operations, where print_hello is dependant on write_echo to finish execution
write_echo >> print_hello