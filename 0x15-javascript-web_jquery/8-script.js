$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  $.get(url, (data) => {
    $.each(data.results, function (idx, val) {
      $('ul#list_movies').append('<li>' + val.title + ' </li>');
    });
  });
});
