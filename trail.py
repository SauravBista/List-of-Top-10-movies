import requests



response = requests.get(url="https://api.themoviedb.org/3/search/movie")


curl --request GET \
     --url 'https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzODZjMWEzZGQ5YWNjM2FmNzY1Y2I0NDQ0NjQxMjQyMCIsIm5iZiI6MTcyNDU4NzU1MC40NTU5ODgsInN1YiI6IjY2Y2IxYzg4NzdiMDFlYTYxYjIwNTY1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ._7mMsWQzGuD9DAG_pAb2aTDh9fxfQ_rW4qp7RPaNASE' \
     --header 'accept: application/json'