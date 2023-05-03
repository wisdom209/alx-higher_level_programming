/* jquery */

const updateHeaderElement = $('#update_header');

updateHeaderElement.on('click', () => {
  const headerElement = $('header');
  headerElement.text('New Header!!!');
});
