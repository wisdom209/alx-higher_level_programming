# Dynamic Js and JQuery

## vanilla js
// Change the text content of an element
element.textContent = 'New content';

// Change the HTML content of an element
element.innerHTML = '<p>New content</p>';

// Add a new class to an element
element.classList.add('new-class');

// Remove a class from an element
element.classList.remove('old-class');

// Toggle a class on an element
element.classList.toggle('active');

## JQuery
// Change the text content of an element
element.text('New content');

// Change the HTML content of an element
element.html('<p>New content</p>');

// Add a new class to an element
element.addClass('new-class');

// Remove a class from an element
element.removeClass('old-class');

// Toggle a class on an element
element.toggleClass('active');

## async requests in JQuery
```
$.ajax({
  url: 'https://jsonplaceholder.typicode.com/todos/1',
  method: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log(data);
  },
  error: function(jqXHR, textStatus, errorThrown) {
    console.log(textStatus + ': ' + errorThrown);
  }
});
```
```
$.get('https://jsonplaceholder.typicode.com/todos/1', function(data) {
  console.log(data);
}, 'json');
```

