$(function () {
  $('div#add_item').on('click', () => {
    const item = document.createElement('li');
    $(item).text('Item');
    $('ul.my_list').append(item);
  });
});
