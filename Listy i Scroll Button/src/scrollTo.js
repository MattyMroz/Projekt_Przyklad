// Przewijanie do danego elementu
jQuery(function ($) {
    //zresetuj scrolla
    $.scrollTo(0);

    // jeśli klikniesz id="link1" -> animacja przejścia do id="budowacrt"
    $('#link1').click(function () {
        $.scrollTo($('#budowacrt'), 500);
    });
    $('#link2').click(function () {
        $.scrollTo($('#zasadacrt'), 500);
    });
    $('#link3').click(function () {
        $.scrollTo($('#maskicrt'), 500);
    });
    $('#link4').click(function () {
        $.scrollTo($('#wadyzaletycrt'), 500);
    });
    $('#link5').click(function () {
        $.scrollTo($('#parametrycrt'), 500);
    });
    $('#link6').click(function () {
        $.scrollTo($('#budowalcd'), 500);
    });
    $('#link7').click(function () {
        $.scrollTo($('#zasadalcd'), 500);
    });
    $('#link8').click(function () {
        $.scrollTo($('#matrycelcd'), 500);
    });
    $('#link9').click(function () {
        $.scrollTo($('#wadyzaletylcd'), 500);
    });
    $('#link10').click(function () {
        $.scrollTo($('#parametrylcd'), 500);
    });
    $('#link11').click(function () {
        $.scrollTo($('#dsub'), 500);
    });
    $('#link12').click(function () {
        $.scrollTo($('#dvi'), 500);
    });
    $('#link13').click(function () {
        $.scrollTo($('#hdmi'), 500);
    });
    $('#link14').click(function () {
        $.scrollTo($('#przyszlosc'), 500);
    });
    $('#link15').click(function () {
        $.scrollTo($('#zrodla'), 500);
    });

    $('.scrollup').click(function () {
        $.scrollTo($('body'), 1000);
    });
});

// scroll button
// jeśli klikniesz button -> animacja przejścia do początku body
//pokaż podczas przewijania
$(window).scroll(function () {
    if ($(this).scrollTop() > 300) $('.scrollup').fadeIn();
    else $('.scrollup').fadeOut();
});
