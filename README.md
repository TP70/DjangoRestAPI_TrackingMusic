To execute, run the following commands:

pip install virtualenv // virtualenv venv // source venv/bin/activate // pip install -r requirements.txt //

python manage.py runserver // or // python3 manage.py runserver //

And then access the browser through the localhost link.

__________________________________________________________________________________________________________

The API should allow a client to perform the following:

- Fetch a single track
  - There are two ways to get a single track, you can use the url extension 'tracks/<int:pk>/' 
    or simply use the filter in the main localhost
    
- Create a new track
  - There are two ways to create a new track, you can use the url extension 'seed-track/' or simply use the 
    option button and then, place a new track using the post method at the bottom of the page in the main localhost

- List the first 100 most recently played tracks (most recent first)
  - You can use the url extension 'recent-tracks/'

- Filter tracks by name
  - You can use the url extension 'artists/'

Bonus:

- Allow the client to fetch a list of artists. Each result should contain artist name, the total number of tracks 
for that artist and their most recently played track.
  - all these are available using the filter in the main localhost

-->>  I also created an option to delete an existent track as a plus.

