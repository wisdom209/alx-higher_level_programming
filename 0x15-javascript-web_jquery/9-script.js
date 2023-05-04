/* jquery */
$(document).ready(() => {
  const proxyendpoint = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const endpoint = 'https://fourtonfish.com/hellosalut/?lang=fr';

  const helloElement = $('#hello');

  helloElement.text('loading . . .');

  $.get(proxyendpoint + endpoint, (data) => {
    helloElement.text(data.hello);
  });
});
