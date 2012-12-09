$(function () {
    var PitchersBoard = function () {};

    PitchersBoard.prototype.showSpinner = function () {
        var opts = {
            lines: 9, // The number of lines to draw
            length: 18, // The length of each line
            width: 13, // The line thickness
            radius: 40, // The radius of the inner circle
            corners: 1, // Corner roundness (0..1)
            rotate: 0, // The rotation offset
            color: '#000', // #rgb or #rrggbb
            speed: 0.8, // Rounds per second
            trail: 60, // Afterglow percentage
            shadow: false, // Whether to render a shadow
            hwaccel: false, // Whether to use hardware acceleration
            className: 'spinner', // The CSS class to assign to the spinner
            zIndex: 2e9, // The z-index (defaults to 2000000000)
            top: '80', // Top position relative to parent in px
            left: '220' // Left position relative to parent in px
        };
        var target = document.getElementById('pitchers-list');
        this.spinner = new Spinner(opts).spin(target);
        console.log($('#pitchers-list'));
    };

    PitchersBoard.prototype.open = function () {
        $('body').append(
            $('<div></div')
                .attr('id', 'pitchers-list')
        );
        this.showSpinner();
        this.retreiveList();
    };

    PitchersBoard.prototype.retreiveList = function () {


    };

    PitchersBoard.prototype.showList = function () {

    }

    var pitchersBoard = new PitchersBoard();
    pitchersBoard.open();
});