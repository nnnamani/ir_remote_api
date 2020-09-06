function start_app() {
    $.ajax({
	url: '/ir-remote/api/v1/command-list',
	dataType:'json',
	type: 'get',
	contentType: 'application/json',
	data: '{}'
    }).done(function(data) {
	if('ir_code' in data) {
	    for(var i = 0; i < data['ir_code'].length; i++) {
		$('div#app').append(render_remocon(data['ir_code'][i]['name'], data['ir_code'][i]['codes']));
	    }
	}
    });
}



/* リモコンの描画 */
function render_remocon(name, button_list) {
    $container = $('<div>').addClass('container');
    $name = $('<h1>').html(name);

    $container.append($name);
    
    for(var i = 0; i < button_list.length; i++) {
	$container.append(render_button(name,button_list[i].name));
    }
    return $container;
}


/* ボタンの描画 */
function render_button(remocon_name, action) {
    var $button = $('<button>');
    $button.text(action);

    /* クリックイベントの登録 */
    $button.on('click',function() {
	//alert('debug:send ' + remocon_name + '/' + action);
	send_request(remocon_name + '/' + action);
    });
    return $button;
}

function send_request(strAction) {
    var url = '/ir-remote/api/v1/' + strAction;

    $.ajax({
        url: url,
        dataType:'json',
        type: 'post',
        contentType: 'application/json',
        data: '{}'
    })
}
