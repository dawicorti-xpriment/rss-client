$(function () {


    $('.button.quit').click(function() {
        bridge.trigger({name: 'mainwindow:quit'});
    });

});