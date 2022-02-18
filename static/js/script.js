$(function() {
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover();
})

$('.toast').toast('show');

$(window).on("resize scroll",function(e) {
    if ($(window).width() <768 ||$(window).scrollTop() > 150) {
        $('#second-navbar').hide();
    }
    else {
        $('#second-navbar').show();
    }
});
