# Shift Scheduling Application

This is a pure python application written using Abstract Factory Designing Principle. The application takes in a csv that
specifies the demand of service during a time period and produces optimum number of shifts that would cater to those 
demands. 

To run this application, follow the steps

1. Ensure there is python3, pip, pipenv on your machine. If pipenv is not there, you can install it by running
```
pip install pipenv
```

2. clone this repository by running the command
``git clone https://github.com/girish1993/scheduler``

3. Once cloned head over to the root folder of the application and activate the virtual enviroment by running the command
``pipenv shell`` . This ensures a virual environment is activated and then run `pipenv install` to install all the dependencies on 
the virtual environment.

4. Next, simply run `python3 scheduler.py`. This runs the application and produces an output csv containing the shifts allocated.
The file will be availble in ``data/output/``.