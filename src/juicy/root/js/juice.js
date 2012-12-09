$(function () {

    $('.button.quit').click(function() {
        bridge.trigger({name: 'juice:quit'});
    });

    $('.button.pitchers').click(function() {
        bridge.trigger({name: 'pitchersboard:open'});
    });


    bridge.trigger({name: 'juice:open'});
});