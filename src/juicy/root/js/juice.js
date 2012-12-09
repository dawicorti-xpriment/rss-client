$(function () {

    $('.button.quit').click(function() {
        bridge.trigger({name: 'mainwindow:quit'});
    });

    $('.button.pitchers').click(function() {
        bridge.trigger({name: 'pitchersboard:open'});
    });

});