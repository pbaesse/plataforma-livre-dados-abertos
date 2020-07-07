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


$('form').on('submit', function(e){
		$.ajax({
			data: {
				name:$('#name').val()
			},
			type: 'POST',
			url : '/process'
		})
		.done(function(data1){
			if (data.error){
				$('#result').text(data.error).show();
			}
			else {
				$('#result').html(data.country).show()
			}
		})

		e.preventDefault();
	});
