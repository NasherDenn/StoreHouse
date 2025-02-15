window.onload = FirstLoad;

var tableBase = ''
var trBase = ''
var tableSend = ''
var trSend = ''
var tableEdit = ''
var trEdit = ''
var tableDelete = ''
var trDelete = ''

function FirstLoad() {
    tableBase = document.getElementById("myTableBase");
    trBase = tableBase.getElementsByTagName("tr");
    tableSend = document.getElementById("myTableSend");
    trSend = tableSend.getElementsByTagName("tr");
    tableEdit = document.getElementById("myTableEdit");
    trEdit = tableEdit.getElementsByTagName("tr");
    tableDelete = document.getElementById("myTableDelete");
    trDelete = tableDelete.getElementsByTagName("tr");
}

function HotSearchingBase() {
    var i;
    var input_method = document.getElementById("hot_searching_method_base");
    var input_manufacture = document.getElementById("hot_searching_manufacture_base");
    var input_name = document.getElementById("hot_searching_name_base");
    var input_serial = document.getElementById("hot_searching_serial_base");
    var input_location = document.getElementById("hot_searching_location_base");
    var filter_method = input_method.value.toUpperCase();
    var filter_manufacture = input_manufacture.value.toUpperCase();
    var filter_name = input_name.value.toUpperCase();
    var filter_serial = input_serial.value.toUpperCase();
    var filter_location = input_location.value.toUpperCase();
    for (i = 0; i < trBase.length; i++) {
        var td_method = trBase[i].getElementsByTagName("td")[1];
        var td_manufacture = trBase[i].getElementsByTagName("td")[2];
        var td_name = trBase[i].getElementsByTagName("td")[4];
        var td_serial = trBase[i].getElementsByTagName("td")[5];
        var td_location = trBase[i].getElementsByTagName("td")[7];
        if (td_method || td_manufacture || td_name || td_serial) {
            var txtValue_method = td_method.textContent || td_method.innerText;
            var txtValue_manufacture = td_manufacture.textContent || td_manufacture.innerText;
            var txtValue_name = td_name.textContent || td_name.innerText;
            var txtValue_serial = td_serial.textContent || td_serial.innerText;
            var txtValue_location = td_location.textContent || td_serial.innerText;
            if (txtValue_method.toUpperCase().indexOf(filter_method) > -1 && txtValue_manufacture.toUpperCase().indexOf(filter_manufacture) > -1 && txtValue_name.toUpperCase().indexOf(filter_name) > -1 && txtValue_serial.toUpperCase().indexOf(filter_serial) > -1 && txtValue_location.toUpperCase().indexOf(filter_location) > -1) {
                trBase[i].style.display = "";
            } else {
                trBase[i].style.display = "none";
            }
        }
    }
}

function HotSearchingSend() {
    var i;
    var input_method = document.getElementById("hot_searching_method_send");
    var input_manufacture = document.getElementById("hot_searching_manufacture_send");
    var input_name = document.getElementById("hot_searching_name_send");
    var input_serial = document.getElementById("hot_searching_serial_send");
    var input_location = document.getElementById("hot_searching_location_send");
    var filter_method = input_method.value.toUpperCase();
    var filter_manufacture = input_manufacture.value.toUpperCase();
    var filter_name = input_name.value.toUpperCase();
    var filter_serial = input_serial.value.toUpperCase();
    var filter_location = input_location.value.toUpperCase();
    for (i = 0; i < trSend.length; i++) {
        var td_method = trSend[i].getElementsByTagName("td")[1];
        var td_manufacture = trSend[i].getElementsByTagName("td")[2];
        var td_name = trSend[i].getElementsByTagName("td")[4];
        var td_serial = trSend[i].getElementsByTagName("td")[5];
        var td_location = trSend[i].getElementsByTagName("td")[7];
        if (td_method || td_manufacture || td_name || td_serial) {
            var txtValue_method = td_method.textContent || td_method.innerText;
            var txtValue_manufacture = td_manufacture.textContent || td_manufacture.innerText;
            var txtValue_name = td_name.textContent || td_name.innerText;
            var txtValue_serial = td_serial.textContent || td_serial.innerText;
            var txtValue_location = td_location.textContent || td_serial.innerText;
            if (txtValue_method.toUpperCase().indexOf(filter_method) > -1 && txtValue_manufacture.toUpperCase().indexOf(filter_manufacture) > -1 && txtValue_name.toUpperCase().indexOf(filter_name) > -1 && txtValue_serial.toUpperCase().indexOf(filter_serial) > -1 && txtValue_location.toUpperCase().indexOf(filter_location) > -1) {
                trSend[i].style.display = "";
            } else {
                trSend[i].style.display = "none";
            }
        }
    }
}

function HotSearchingEdit() {
    var i;
    var input_method = document.getElementById("hot_searching_method_edit");
    var input_manufacture = document.getElementById("hot_searching_manufacture_edit");
    var input_name = document.getElementById("hot_searching_name_edit");
    var input_serial = document.getElementById("hot_searching_serial_edit");
    var input_location = document.getElementById("hot_searching_location_edit");
    var filter_method = input_method.value.toUpperCase();
    var filter_manufacture = input_manufacture.value.toUpperCase();
    var filter_name = input_name.value.toUpperCase();
    var filter_serial = input_serial.value.toUpperCase();
    var filter_location = input_location.value.toUpperCase();
    for (i = 0; i < trEdit.length; i++) {
        var td_method = trEdit[i].getElementsByTagName("td")[1];
        var td_manufacture = trEdit[i].getElementsByTagName("td")[2];
        var td_name = trEdit[i].getElementsByTagName("td")[4];
        var td_serial = trEdit[i].getElementsByTagName("td")[5];
        var td_location = trEdit[i].getElementsByTagName("td")[7];
        if (td_method || td_manufacture || td_name || td_serial) {
            var txtValue_method = td_method.textContent || td_method.innerText;
            var txtValue_manufacture = td_manufacture.textContent || td_manufacture.innerText;
            var txtValue_name = td_name.textContent || td_name.innerText;
            var txtValue_serial = td_serial.textContent || td_serial.innerText;
            var txtValue_location = td_location.textContent || td_serial.innerText;
            if (txtValue_method.toUpperCase().indexOf(filter_method) > -1 && txtValue_manufacture.toUpperCase().indexOf(filter_manufacture) > -1 && txtValue_name.toUpperCase().indexOf(filter_name) > -1 && txtValue_serial.toUpperCase().indexOf(filter_serial) > -1 && txtValue_location.toUpperCase().indexOf(filter_location) > -1) {
                trEdit[i].style.display = "";
            } else {
                trEdit[i].style.display = "none";
            }
        }
    }
}

function HotSearchingDelete() {
    var i;
    var input_method = document.getElementById("hot_searching_method_delete");
    var input_manufacture = document.getElementById("hot_searching_manufacture_delete");
    var input_name = document.getElementById("hot_searching_name_delete");
    var input_serial = document.getElementById("hot_searching_serial_delete");
    var input_location = document.getElementById("hot_searching_location_delete");
    var filter_method = input_method.value.toUpperCase();
    var filter_manufacture = input_manufacture.value.toUpperCase();
    var filter_name = input_name.value.toUpperCase();
    var filter_serial = input_serial.value.toUpperCase();
    var filter_location = input_location.value.toUpperCase();
    for (i = 0; i < trDelete.length; i++) {
        var td_method = trDelete[i].getElementsByTagName("td")[1];
        var td_manufacture = trDelete[i].getElementsByTagName("td")[2];
        var td_name = trDelete[i].getElementsByTagName("td")[4];
        var td_serial = trDelete[i].getElementsByTagName("td")[5];
        var td_location = trDelete[i].getElementsByTagName("td")[7];
        if (td_method || td_manufacture || td_name || td_serial) {
            var txtValue_method = td_method.textContent || td_method.innerText;
            var txtValue_manufacture = td_manufacture.textContent || td_manufacture.innerText;
            var txtValue_name = td_name.textContent || td_name.innerText;
            var txtValue_serial = td_serial.textContent || td_serial.innerText;
            var txtValue_location = td_location.textContent || td_serial.innerText;
            if (txtValue_method.toUpperCase().indexOf(filter_method) > -1 && txtValue_manufacture.toUpperCase().indexOf(filter_manufacture) > -1 && txtValue_name.toUpperCase().indexOf(filter_name) > -1 && txtValue_serial.toUpperCase().indexOf(filter_serial) > -1 && txtValue_location.toUpperCase().indexOf(filter_location) > -1) {
                trDelete[i].style.display = "";
            } else {
                trDelete[i].style.display = "none";
            }
        }
    }
}

function getFilter() {
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
    tableBase = document.getElementById("myTableBase");
    trBase = tableBase.getElementsByTagName("tr");
    var new_tr_base = []
    for (var i = 1; i < trBase.length; i++) {
        var visible = false
        var td_method = trBase[i].getElementsByTagName("td")[1];
        var td_location = trBase[i].getElementsByTagName("td")[7];
        var td_status = trBase[i].getElementsByTagName("td")[8];
        for (var method_index = 0; method_index < checkboxesChecked['method'].length; method_index++) {
            for (var location_index = 0; location_index < checkboxesChecked['location'].length; location_index++) {
                for (var status_index = 0; status_index < checkboxesChecked['status'].length; status_index++) {
                    if (td_method.innerText == checkboxesChecked['method'][method_index] && td_location.innerText == checkboxesChecked['location'][location_index] && td_status.innerText == checkboxesChecked['status'][status_index]) {
                        visible = true;
                    }
                }
            }
        }
        if (visible == true) {
            trBase[i].style.display = "";
            new_tr_base.push(trBase[i])
        } else {
            trBase[i].style.display = "none";
        }
    }
    tableSend = document.getElementById("myTableSend");
    trSend = tableSend.getElementsByTagName("tr");
    var new_tr_send = []
    for (var i = 1; i < trSend.length; i++) {
        var visible = false
        var td_method = trSend[i].getElementsByTagName("td")[1];
        var td_location = trSend[i].getElementsByTagName("td")[7];
        var td_status = trSend[i].getElementsByTagName("td")[8];
        for (var method_index = 0; method_index < checkboxesChecked['method'].length; method_index++) {
            for (var location_index = 0; location_index < checkboxesChecked['location'].length; location_index++) {
                for (var status_index = 0; status_index < checkboxesChecked['status'].length; status_index++) {
                    if (td_method.innerText == checkboxesChecked['method'][method_index] && td_location.innerText == checkboxesChecked['location'][location_index] && td_status.innerText == checkboxesChecked['status'][status_index]) {
                        visible = true;
                    }
                }
            }
        }
        if (visible == true) {
            trSend[i].style.display = "";
            new_tr_send.push(trSend[i])
        } else {
            trSend[i].style.display = "none";
        }
    }
    trSend = new_tr_send
    tableEdit = document.getElementById("myTableEdit");
    trEdit = tableEdit.getElementsByTagName("tr");
    var new_tr_edit = []
    for (var i = 1; i < trEdit.length; i++) {
        var visible = false
        var td_method = trEdit[i].getElementsByTagName("td")[1];
        var td_location = trEdit[i].getElementsByTagName("td")[7];
        var td_status = trEdit[i].getElementsByTagName("td")[8];
        for (var method_index = 0; method_index < checkboxesChecked['method'].length; method_index++) {
            for (var location_index = 0; location_index < checkboxesChecked['location'].length; location_index++) {
                for (var status_index = 0; status_index < checkboxesChecked['status'].length; status_index++) {
                    if (td_method.innerText == checkboxesChecked['method'][method_index] && td_location.innerText == checkboxesChecked['location'][location_index] && td_status.innerText == checkboxesChecked['status'][status_index]) {
                        visible = true;
                    }
                }
            }
        }
        if (visible == true) {
            trEdit[i].style.display = "";
            new_tr_edit.push(trEdit[i])
        } else {
            trEdit[i].style.display = "none";
        }
    }
    trEdit = new_tr_edit
    tableDelete = document.getElementById("myTableDelete");
    trDelete = tableDelete.getElementsByTagName("tr");
    var new_tr = []
    for (var i = 1; i < trDelete.length; i++) {
        var visible = false
        var td_method = trDelete[i].getElementsByTagName("td")[1];
        var td_location = trDelete[i].getElementsByTagName("td")[7];
        var td_status = trDelete[i].getElementsByTagName("td")[8];
        for (var method_index = 0; method_index < checkboxesChecked['method'].length; method_index++) {
            for (var location_index = 0; location_index < checkboxesChecked['location'].length; location_index++) {
                for (var status_index = 0; status_index < checkboxesChecked['status'].length; status_index++) {
                    if (td_method.innerText == checkboxesChecked['method'][method_index] && td_location.innerText == checkboxesChecked['location'][location_index] && td_status.innerText == checkboxesChecked['status'][status_index]) {
                        visible = true;
                    }
                }
            }
        }
        if (visible == true) {
            trDelete[i].style.display = "";
            new_tr.push(trDelete[i])
        } else {
            trDelete[i].style.display = "none";
        }
    }
    trDelete = new_tr
}

// установить флажок всех checkbox в фильтрах и сделать нажатыми кнопки фильтров (Метод контроля, Месторасположение и Статус)
function check() {
    var checkMethod = document.getElementsByName('CheckMethod');
    for (var i = 0; i < checkMethod.length; i++) {
        if (checkMethod[i].type == 'checkbox') {
            checkMethod[i].checked = true;
        }
    }
    var checkLocation = document.getElementsByName('CheckLocation');
    for (var ii = 0; ii < checkLocation.length; ii++) {
        if (checkLocation[ii].type == 'checkbox') {
            checkLocation[ii].checked = true;
        }
    }
    var checkStatus = document.getElementsByName('CheckStatus');
    for (var iii = 0; iii < checkStatus.length; iii++) {
        if (checkStatus[iii].type == 'checkbox') {
            checkStatus[iii].checked = true;
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
    var uncheckMethod = document.getElementsByName('CheckMethod');
    for (var i = 0; i < uncheckMethod.length; i++) {
        if (uncheckMethod[i].type == 'checkbox') {
            uncheckMethod[i].checked = false;
        }
    }
    var uncheckLocation = document.getElementsByName('CheckLocation');
    for (var ii = 0; ii < uncheckLocation.length; ii++) {
        if (uncheckLocation[ii].type == 'checkbox') {
            uncheckLocation[ii].checked = false;
        }
    }
    var uncheckStatus = document.getElementsByName('CheckStatus');
    for (var iii = 0; iii < uncheckStatus.length; iii++) {
        if (uncheckStatus[iii].type == 'checkbox') {
            uncheckStatus[iii].checked = false;
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


var equipment_send = []


// кнопка для выделения или снятия всех флажков оборудования в закладке "Отправить"
function check_send_all() {
    var check_send_all = document.getElementsByName('CheckSendAll');
    var check_all_equipment = document.getElementsByName('CheckSend');
    var index_check_send = 0;
    // список id, выбранных строк (оборудования для отправки)
    equipment_send = []
    if (check_send_all[0].checked == true) {
        for (var i = 0; i < check_all_equipment.length; i++) {
            check_all_equipment[i].checked = true
            index_check_send++
            equipment_send.push(document.getElementById("myTableSend").rows[i + 1].cells[10].innerText)
        }
    } else {
        for (var i = 0; i < check_all_equipment.length; i++) {
            check_all_equipment[i].checked = false
            index_check_send = 0
        }
    }
    if (index_check_send == 0) {
        document.getElementById('button-send').innerHTML = '<i class="bi bi-truck" style="font-size: 1em; color: white; width: 150px; background-color: #e6f0fc;"><i/>'
        document.getElementById('button-send').disabled = true
    } else {
        document.getElementById('button-send').innerHTML = `<i class="bi bi-truck" style="font-size: 1em; color: white; width: 150px; background-color: #e6f0fc;"> ${index_check_send}<i/>`
        document.getElementById('button-send').disabled = false

    }
    return equipment_send
}


// делаем активным общую кнопку по выделению всех строк с оборудованием
function check_send_all_active() {
    var index_check_send = 0
    var check_box_send_all = document.getElementsByName('CheckSendAll')
    var choose_check_box_send = document.getElementsByName('CheckSend')
    // список id, выбранных строк (оборудования для отправки)
    equipment_send = []
    for (var i = 0; i < choose_check_box_send.length; i++) {
        if (choose_check_box_send[i].checked == true) {
            index_check_send++
            equipment_send.push(document.getElementById("myTableSend").rows[i + 1].cells[10].innerText)
        }
        if (index_check_send == 0) {
            check_box_send_all[0].checked = false
        } else {
            check_box_send_all[0].checked = true
        }
    }
    if (index_check_send == 0) {
        document.getElementById('button-send').innerHTML = '<i class="bi bi-truck" style="font-size: 1em; color: white; width: 150px; background-color: #e6f0fc;"><i/>'
        document.getElementById('button-send').disabled = true
    } else {
        document.getElementById('button-send').innerHTML = `<i class="bi bi-truck" style="font-size: 1em; color: white; width: 150px; background-color: #e6f0fc;"> ${index_check_send}<i/>`
        document.getElementById('button-send').disabled = false
    }
}


function do_form_send() {
    // загружаем список выбранного оборудования в localStorage
    localStorage.setItem("data", equipment_send);
    window.open('/forms_send', '_blank')
}


// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
}

function scrollFunction() {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        document.getElementById("myBtn").style.display = "block";
    } else {
        document.getElementById("myBtn").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
