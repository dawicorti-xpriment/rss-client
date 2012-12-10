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
            top: '120', // Top position relative to parent in px
            left: '240' // Left position relative to parent in px
        };
        var target = document.getElementById('pitchers-list');
        this.spinner = new Spinner(opts).spin(target);
    };

    PitchersBoard.prototype.open = function () {
        $('body').append(
            $('<div></div')
                .attr('id', 'pitchers-list')
        );
        this.showSpinner();
        var that = this;
        juicy.getConfig('pitchersboard', function (config) {
            that.config = config;
            that.retreiveList();  
        });
    };

    PitchersBoard.prototype.retreiveList = function () {
        var that = this;
        $.ajax({
            url: this.config.pitchers_url
        }).done(function(data) {
            var description = JSON.parse(data);
            that.showList(description.pitchers);
        });
    };

    PitchersBoard.prototype.showList = function (pitchers) {
        var that = this;
        $.each(pitchers, function (index, pitcher) {
            that.getPitcherDescription(pitcher);
        });
    };

    PitchersBoard.prototype.getPitcherDescription = function (pitcher) {
        var that = this;
        $.ajax({
            url: 'https://raw.github.com/'
                    + pitcher.repository
                    + '/'
                    + pitcher.commit
                    + '/pitcher.json'
        }).done(function(data) { 
            var infos = JSON.parse(data);
            that.readPitcherDescription(pitcher, infos);
        });
    };

    PitchersBoard.prototype.readPitcherDescription = function (pitcher, infos) {
        this.spinner.stop();
        var icon = 'https://raw.github.com/'
                        + pitcher.repository
                        + '/'
                        + pitcher.commit
                        + infos.icon.replace('./', '/');
        var thumb = $('<div></div>')
                        .addClass('pitcher')
                        .append(
                            $('<span></span>').addClass('name').html(infos.name),
                            $('<span></span>').addClass('description').html(infos.description),
                            $('<span></span>').addClass('author').html('by ' + infos.author),
                            $('<img />').attr('src', icon)
                        );
        $('#pitchers-list').append(thumb);
    };

    var pitchersBoard = new PitchersBoard();
    pitchersBoard.open();
});