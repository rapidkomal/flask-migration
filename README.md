## FLASK-MIGRATION

#### To install PostgreSql
> link to download : https://www.postgresql.org/download/
##### For Mac
```brew install postgresql ```
```brew services start postgresql ```

###### For Linux
``` sudo apt-get install postgresql postgresql-contrib ```
``` sudo systemctl start postgresql ```

###### Install PgAdmin4
MAC
```brew install --cask pgadmin4```

Linux
```sudo apt-get update && sudo apt-get install pgadmin4-desktop ```

###### Flask - migration
Initialisation Of migration
```flask db init ```
Create migration file
```flask db migrate```
Updrage migration
```flask db upgrade```






