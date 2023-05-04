/* jquery */
$(document).ready(() => {
  const proxyendpoint = 'https://hellosalut.stefanbohacek.dev/?lang=';

  let language = '';
  $('#hello').text('Enter a language: es, fr, en');
  $('#btn_translate').on('click', () => {
    $('#hello').text('Loading . . .');
    language = $('#language_code').val();
    $.get(proxyendpoint + language, (data) => {
      console.log(data);
      $('#hello').text(data.hello);
    });
  });
});
