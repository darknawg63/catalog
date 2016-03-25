$(document).ready(function() {
    // AJAX GET
    $('.get-more').click(function(){

        $.ajax({
            type: "GET",
            url: "/ajax/more/",
            success: function(data) {

            for(i = 0; i < data.length; i++){
                $('ul').append('<li>'+data[i]+'</li>');
            }
        }
        });

    });

    // AJAX POST
    $('form.ajax').on('submit', function(e){

		e.preventDefault();
		var self = $(this),
			url = self.attr('action'),
            type = self.attr('method'),
			data = {}

        self.find('[name]').each(function(index, value) {
            var self = $(this),
                name = self.attr('name'),
                value = self.val();

            data[name] = value;
        });

        $.ajax({
            url: url,
            type: type,
            datatype: 'json',
            data: data,

            success: function(response) {

                if (response) {
                    console.log(response.success);
                }
            },

            error: function(error) {

                if (error) {
                    var errors = jQuery.parseJSON(error.responseText);
                    var keys = Object.keys(errors);

                    for (key in keys) {
                        var token = keys[key]; 

                        if ($('input[name="' + token + '"]').next(".errorlist").length <= 0) {
                            $('input[name="' + token + '"]').after( '<ul class="errorlist"><li>' + errors[token] + '</li></ul>' );
                        }   
                    }   
                }   
                console.log(error.responseText);
            }
        });

    });



    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 
});
