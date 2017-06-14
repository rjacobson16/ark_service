# ark_service

To run:

-Install requirements.txt

python manage.py runserver

To mint a new ark, use the working test minter (minter #2) at the url below. Enter the number of ARKs you'd like to mint after the last slash.

https://127.0.0.1:8000/mint/2/

To bind the ARK to a new url, enter, where ####### is the ID number returned when you minted the ARK

https://127.0.0.1:8000/bind/######/[insert_url]

For instance, 

https://127.0.0.1:8000/bind/123456/www.google.com

binds ARK #123456 to www.google.com
