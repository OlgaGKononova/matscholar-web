
var countTime = 3000;

function animatedCount(id, duration) {
    var radix = 10
    var obj = document.getElementById(id);
    var countTo = obj.innerHTML.replace(/,/g, "")
    var countTo = parseInt(countTo, radix)
//    var countTo = 10000

    // assumes integer values for start and end
    var start = 0 * countTo;
    var end = countTo;

    var range = end - start;
    // no timer shorter than 50ms (not really visible any way)
    var minTimer = 50;
    // calc step time to show all interediate values
    var stepTime = Math.abs(Math.floor(duration / range));

    // never go below minTimer
    stepTime = Math.max(stepTime, minTimer);

    // get current time and calculate desired end time
    var startTime = new Date().getTime();
    var endTime = startTime + duration;
    var timer;

    function run() {
        var now = new Date().getTime();
        var remaining = Math.max((endTime - now) / duration, 0);
        var value = Math.round(end - (remaining * range));
        var formattedValue = value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        obj.innerHTML = formattedValue
        if (value == end) {
            clearInterval(timer);
        }
    }

    timer = setInterval(run, stepTime);
    run();
}


if(!window.dash_clientside) {window.dash_clientside = {};}
window.dash_clientside.clientside = {
    display123: function (pathname, id1, id2, id3) {
        if (pathname == "/about"){
                animatedCount(id1, countTime)
                animatedCount(id2, countTime)
                animatedCount(id3, countTime)
        }
    }
}