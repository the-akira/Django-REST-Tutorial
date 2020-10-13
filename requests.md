# Requests

## AUTH

curl -d '{"username":"akira", "password":"5565340gabriel"}' -H "Content-Type: application/json" -X POST http://localhost:8000/login/

## GET

curl -X GET http://localhost:8000/filmes/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'

curl -X GET http://localhost:8000/filmes/5/ -H 'Authorization: Token d1781baac8f55daf296f6f32144ba2e107d949b5'

## POST

curl -d '{"titulo":"The Lord of the Rings","diretor":"Peter Jackson","sinopse":"The Lord of the Rings is a film series of three epic fantasy adventure films directed by Peter Jackson, based on the novel written by J. R. R. Tolkien.","genero":"Adventure","owner":1}' -H "Content-Type: application/json" -X POST http://localhost:8000/filmes/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'

## PUT

curl -d '{"titulo":"Fight Club","diretor":"David Fincher","sinopse":"Fight Club is a 1999 American film directed by David Fincher","genero":"cult","owner":1}' -H "Content-Type: application/json" -X PUT http://localhost:5000/filmes/2/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'

## DELETE

curl -H "Content-Type: application/json" -X DELETE http://localhost:5000/filmes/1/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'
