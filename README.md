# Projektni Zadatak  – Load Balancer

Sistem sadrži 5 komponenti:
1. Writer
2. Load Balancer
3. Worker
4. Database CRUD
5. Database Analitics
# Writer

Writer je komponenta koja služi za upisivanje novih podataka u Load Balancer komponentu.

# Load Balancer

Load Balancer je komponenta koja služi za ravnomerno raspoređivanje posla. 

# Worker

Worker je komponenta koja služi za obradu podataka dobijenih od Load Balancer komponente. 

# Database CRUD

DatabaseCRUD komponenta služi za svu komunikaciju koja se obavlja sa bazom podataka
i ova komponenta je zadužena za izvršavanje CRUD operacija. 

# Database Analitics

Database Analitics komponenta komunicira sa DatabaseCRUD komponentom i služi za izvlacenje statistika
iz baze podataka u vidu izveštaja.
