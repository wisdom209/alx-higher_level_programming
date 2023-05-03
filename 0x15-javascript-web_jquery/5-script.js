/* jquery */

const addItem = $('#add_item');

addItem.on('click', () => {
  const myList = $('.my_list');
  myList.append('<li>Item</item>');
});
