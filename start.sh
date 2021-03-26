docker-compose down
docker-compose build
docker-compose up -d
flake8 --ignore E501,E231,E201,E202,E203,E226,W504,W504,E121,E122,F401,E265,E128,E126,E124,E712 api/ core/ dao_entities/ db/ entities/ idefix_api/ models/ tests/
