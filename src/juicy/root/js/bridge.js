$(function () {

    bridge.callbacks = {};
    
    bridge.signal.connect(function(raw) {
        var message = JSON.parse(raw);
        if (bridge.callbacks.hasOwnProperty(message.name)) {
            bridge.callbacks[message.name].forEach(function (callback) {
                callback(message);
            });
        }
    });

    bridge.on = function (name, callback) {
        if (!bridge.callbacks.hasOwnProperty(name)) {
            bridge.callbacks[name] = [];
            bridge.listen(name);
        }
        bridge.callbacks[name].push(callback);
    };

    bridge.trigger = function (message) {
        var raw = JSON.stringify(message);
        bridge.send(raw);
    };


});