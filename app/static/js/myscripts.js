$(document).ready(function () {
  var titles = [

  ];

  function loadTitles() {
    $.getJSON('/_autocomplete', function (data, status, xhr) {
      for (var i = 0; i < data.length; i++) {
        titles.push(data[i].title);
      }
    });
  };

  loadTitles();

  $('#autocomplete').autocomplete({
    source: titles
  });
});



$(document).ready(function () {
  var tags = [

  ];

  function loadTags() {
    $.getJSON('/_tag', function (data, status, xhr) {
      for (var i = 0; i < data.length; i++) {
        tags.push(data[i].tag);
      }
    });
  };

  loadTags();

});
