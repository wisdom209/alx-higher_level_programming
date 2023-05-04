/* JQuery */

$(document).ready(function () {
  const addItemElem = $('#add_item');
  const delItemElem = $('#remove_item');
  const clearItemsElem = $('#clear_list');
  const myListElem = $('.my_list');

  addItemElem.on('click', () => {
    myListElem.append('<li>Item</li>');
  });

  delItemElem.on('click', () => {
    myListElem.children().last().remove();
  });

  clearItemsElem.on('click', () => {
    myListElem.empty();
  });
});
