function setCookie(key, value) {
    var expires = new Date();
    expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
    document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
}



function getCookie(key) {
    var keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
    return keyValue ? keyValue[2] : null;
}



function deleteCookie(key) {
    document.cookie = key + '=; Max-Age=0';

}



function setRoomname() {
    $("span.roomname").html(room);
}



function logMessage(message) {
    $("#log").append(message + "<br />");
}



function showRooms(message) {
    console.log(message);
}


function refreshMessages(message) {
    try {
        $("#message-list").append(
            '<li><span class="bold">&lt;'+
            message.data.alias +
            '&gt;</span>&nbsp;' +
            message.data.message +
            '</li>'
        );
    } catch(err) {
        console.log(message);
    }
}


function clearMessageBox() {
    $("#messageText").val("");
}



function listRooms(rooms) {
    $("#roomname").autocomplete({
        source: rooms
    });
}