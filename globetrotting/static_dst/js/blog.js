$(document).ready(function(){
    var links = $('.location a');
    var path = location.pathname;
    links.each(function(){
        var href = $(this).attr('href');
        if (href === path){
            $(this).addClass('btn-info');
        }
    })

    $('.dateinput').datepicker({
        format: 'dd/mm/yyyy'
    });
});

