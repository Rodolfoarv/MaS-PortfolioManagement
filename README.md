# MaS-PortfolioManagement

## Installing the application
    # Setup the project
    Clone the repository with the following command:
    git clone https://github.com/Rodolfoarv/MaS-PortfolioManagement.git

    #Install packages

    pip install -r requirements.txt

    #Execute spade server

    cd /src/SPADE-2.2.1
    python runspade.py

    # Setup the database
    cd /src/db
    mysql -u root -p < seed.sql
    mysql -u root -p < dummyData.sql


    #Execute in a terminal each of the following agents

    python coordinator.py
    python technical_analysis.py
    python monitor.py
    python decision_making.py
    python profiler.py

    #You will be requested to create a user or you can use the default user
      - user: aers@gmail.com password: IBM

## Diagrams

![](https://github.com/Rodolfoarv/MaS-PortfolioManagement/blob/master/doc/img/PortafolioInversiones.png)

## Authors

- Rodolfo Andrés Ramírez Valenzuela
- Roberto Pliego Torres
- Steeven Muñoz
- Iván Díaz

#TODO

- Integrate the queries from profiler to coordinator

## License

See [LICENSE] (https://github.com/Rodolfoarv/Evil-Hangman/blob/master/LICENSE)
