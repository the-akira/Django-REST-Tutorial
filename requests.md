# Requests

## AUTH

curl -d '{"username":"akira", "password":"997851gabriel"}' -H "Content-Type: application/json" -X POST http://localhost:8000/login/

## GET

curl -X GET http://localhost:8000/filmes/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'

curl -X GET http://localhost:8000/filmes/5/ -H 'Authorization: Token d1781baac8f55daf296f6f32144ba2e107d949b5'

## POST

curl -d '{"titulo":"x","diretor":"x","sinopse":"x","genero":"x","owner":1}' -H "Content-Type: application/json" -X POST http://localhost:8000/filmes/ -H 'Authorization: Token 75c0bba76256298d8d7ea5f204cfad83fe9a174d'

## PUT

curl -d '{"titulo":"v","diretor":"v","sinopse":"v","genero":"v","owner":1}' -H "Content-Type: application/json" -X PUT http://localhost:8000/filmes/3/ -H 'Authorization: Token d1781baac8f55daf296f6f32144ba2e107d949b5'

## DELETE

curl -H "Content-Type: application/json" -X DELETE http://localhost:8000/filmes/5/ -H 'Authorization: Token d1781baac8f55daf296f6f32144ba2e107d949b5'