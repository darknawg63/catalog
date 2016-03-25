$('.vDateField').datetimepicker({
	showOn: null,
	buttonText: "Calendar",
	dateFormat: "yy-MM-dd",
	timeFormat: "HH:MM:ss",
    timeInput: true
});

$("#datepicker-img").click(function() {
    $(".vDateField").datepicker( "show" ); 
});

$("#today").on("click", function(){
    var today = new Date();
    var yyyy = today.getFullYear();
    var MM = today.getMonth()+1; //January is 0!
    var dd = today.getDate();
    var HH = today.getHours();
    var mm = today.getMinutes();
    var ss = today.getSeconds();

    if(dd<10) {
        dd='0'+dd
    } 

    if(MM<10) {
        MM='0'+MM
    } 

    if(ss<10) {
        ss='0'+ss
    }

    today = yyyy+'-'+MM+'-'+dd+' '+HH+':'+mm+':'+ss;

    $(".vDateField").val(today);

});
