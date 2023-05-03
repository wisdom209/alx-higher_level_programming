/* jquery */
const toggleHeader = $('#toggle_header');
const headerElement = $('header');

toggleHeader.on('click', () => {
  const headerClass = headerElement.attr('class');
  if (headerClass === 'green') {
    headerElement.removeClass('green');
    headerElement.addClass('red');
  }
  else {
    headerElement.removeClass('red');
    headerElement.addClass('green');
  }
});
