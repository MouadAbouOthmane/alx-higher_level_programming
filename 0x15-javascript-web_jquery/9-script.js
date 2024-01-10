$(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, (data) => {
    $('DIV#hello').text(data.hello);
  });
});
