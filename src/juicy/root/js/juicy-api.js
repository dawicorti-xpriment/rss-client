$(function () {

    var juicy = {};

    juicy.getConfig = function (module, callback) {
        bridge.on('config:send', function (message) {
            if (message.module === module) {
                callback(message.data);
            }
        });
        bridge.trigger({
            name: 'config:get',
            module: module
        });
    };

    window.juicy = juicy;
});