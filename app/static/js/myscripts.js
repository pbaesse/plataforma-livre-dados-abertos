$(document).ready(function(){
  var titles=[];

  function loadTitles(){
      $.getJSON('/_autocomplete', function(data, status, xhr){
        for (var i = 0; i < data.length; i++ ) {
          titles.push(data[i].title);
        }
      });
    };

    loadTitles();

    $('#autocomplete').autocomplete({
      source: titles
    });
  });
