/* jquery */

const endpoint = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

const characterElement = $('#character');
characterElement.text('Loading . . .');
$.get(endpoint, (data) => {
  characterElement.text(data.name);
});
