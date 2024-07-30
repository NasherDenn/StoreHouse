// установить флажок всех checkbox в фильтрах и сделать нажатыми кнопки фильтров (Метод контроля, Месторасположение и Статус)
function check() {
    var check = document.getElementsByTagName('input');
    for (var i = 0; i < check.length; i++) {
        if (check[i].type == 'checkbox') {
            check[i].checked = true;
        }
    }
    var btn_method = document.getElementById('button_method');
    var btn_location = document.getElementById('button_location');
    var btn_status = document.getElementById('button_status');
    btn_method.classList.add('active');
    btn_method.ariaPressed = 'true';
    btn_location.classList.add('active');
    btn_location.ariaPressed = 'true';
    btn_status.classList.add('active');
    btn_status.ariaPressed = 'true';
}

// убрать флажок всех checkbox в фильтрах и отжать кнопки фильтров (Метод контроля, Месторасположение и Статус)
function uncheck() {
    var uncheck = document.getElementsByTagName('input');
    for (var i = 0; i < uncheck.length; i++) {
        if (uncheck[i].type == 'checkbox') {
            uncheck[i].checked = false;
        }
    }
    var btn_method = document.getElementById('button_method');
    var btn_location = document.getElementById('button_location');
    var btn_status = document.getElementById('button_status');
    btn_method.classList.remove('active');
    btn_method.ariaPressed = 'false';
    btn_location.classList.remove('active');
    btn_location.ariaPressed = 'false';
    btn_status.classList.remove('active');
    btn_status.ariaPressed = 'false';
}

// установить флажок всех checkbox фильтра "Метод контроля"
function check_method() {
    var btn_method = document.getElementById('button_method');
    if (btn_method.classList.contains('active')) {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckMethod') {
                    if (check[i].checked == false) {
                        check[i].checked = true;
                    }
                }
            }
        }
    } else {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckMethod') {
                    if (check[i].checked == true) {
                        check[i].checked = false;
                    }
                }
            }
        }
    }
}

// установить флажок всех checkbox фильтра "Месторасположение"
function check_location() {
    var btn_location = document.getElementById('button_location');
    if (btn_location.classList.contains('active')) {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckLocation') {
                    if (check[i].checked == false) {
                        check[i].checked = true;
                    }
                }
            }
        }
    } else {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckLocation') {
                    if (check[i].checked == true) {
                        check[i].checked = false;
                    }
                }
            }
        }
    }
}

// установить флажок всех checkbox фильтра "Статус"
function check_status() {
    var btn_status = document.getElementById('button_status');
    if (btn_status.classList.contains('active')) {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckStatus') {
                    if (check[i].checked == false) {
                        check[i].checked = true;
                    }
                }
            }
        }
    } else {
        var check = document.getElementsByTagName('input');
        for (var i = 0; i < check.length; i++) {
            if (check[i].type == 'checkbox') {
                if (check[i].id == 'CheckStatus') {
                    if (check[i].checked == true) {
                        check[i].checked = false;
                    }
                }
            }
        }
    }
}

// список выбранных фильтров для отправки запроса в БД
function get_filter() {
    var checkboxesChecked = {};
    checkboxesChecked['method'] = []
    checkboxesChecked['location'] = []
    checkboxesChecked['status'] = []
    var checkboxes_method = document.getElementsByName('CheckMethod');
    var label_method = document.getElementsByName('label_method');
    for (var index = 0; index < checkboxes_method.length; index++) {
        if (label_method[index].htmlFor == 'CheckMethod') {
            if (checkboxes_method[index].checked) {
                checkboxesChecked['method'].push(label_method[index].textContent);
            }
        }
    }
    var checkboxes_location = document.getElementsByName('CheckLocation');
    var label_location = document.getElementsByName('label_location');
    for (var index = 0; index < checkboxes_location.length; index++) {
        if (label_location[index].htmlFor == 'CheckLocation') {
            if (checkboxes_location[index].checked) {
                checkboxesChecked['location'].push(label_location[index].textContent);
            }
        }
    }
    var checkboxes_status = document.getElementsByName('CheckStatus');
    var label_status = document.getElementsByName('label_status');
    for (var index = 0; index < checkboxes_status.length; index++) {
        if (label_status[index].htmlFor == 'CheckStatus') {
            if (checkboxes_status[index].checked) {
                checkboxesChecked['status'].push(label_status[index].textContent);
            }
        }
    }
    console.log(checkboxesChecked)
    console.log('ok')
}