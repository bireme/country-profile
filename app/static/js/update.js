function open_popup_win(url, target, width, height) {
    var w = width;    // field assist window weight
    var h = height;    // field assist window height

    // calculate position to center field assist window
    var dualScreenLeft = window.screenLeft != undefined ? window.screenLeft : screen.left;
    var dualScreenTop = window.screenTop != undefined ? window.screenTop : screen.top;

    var width = window.innerWidth ? window.innerWidth : document.documentElement.clientWidth ? document.documentElement.clientWidth : screen.width;
    var height = window.innerHeight ? window.innerHeight : document.documentElement.clientHeight ? document.documentElement.clientHeight : screen.height;

    var left = ((width / 2) - (w / 2)) + dualScreenLeft;
    var top = ((height / 2) - (h / 2)) + dualScreenTop;

    popup_win = window.open(url, target, 'scrollbars=yes, width=' + w + ', height=' + h + ', top=' + top + ', left=' + left);

    if (window.focus) {
        popup_win.focus();
    }
}

function open_update_data(country_indicator_id, mode){
    update_url = '/' + mode + '/';
    if (mode == 'update'){
        update_url += country_indicator_id + '/';
    }


    open_popup_win(update_url, 'update_create', 800, 550);
    return false;
}