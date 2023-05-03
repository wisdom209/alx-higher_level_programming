/* jquery */

const endpoint = 'https://swapi-api.alx-tools.com/api/films/?format=json';

const ulElement = $('#list_movies');
ulElement.text('Loading . . .');
$.get(endpoint, (data) => {
  ulElement.text('');
  data.results.forEach(obj => {
    ulElement.append(`<li>${obj.title}</li>`);
  });
});
