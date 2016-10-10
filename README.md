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


    #Execute in another terminal the agents

    python <agent>.py

## Diagrams

![](https://github.com/Rodolfoarv/MaS-PortfolioManagement/blob/master/doc/img/PortafolioInversiones.png)

## Authors

- Rodolfo Andrés Ramírez Valenzuela
- Roberto Pliego Torres
- Iván Díaz Sánchez
- Steeven Muñoz


## License

See [LICENSE] (https://github.com/Rodolfoarv/Evil-Hangman/blob/master/LICENSE)
