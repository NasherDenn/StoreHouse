// Оптимизированная версия HotSearching
function HotSearching(tableId, methodId, manufactureId, typeId, nameId, serialId, locationId, statusId) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.querySelectorAll("tbody tr");
    if (!rows.length) return;

    const filters = {
        method: document.getElementById(methodId).value.toUpperCase(),
        manufacture: document.getElementById(manufactureId).value.toUpperCase(),
        type: document.getElementById(typeId).value.toUpperCase(),
        name: document.getElementById(nameId).value.toUpperCase(),
        serial: document.getElementById(serialId).value.toUpperCase(),
        location: document.getElementById(locationId).value.toUpperCase(),
        status: document.getElementById(statusId).value.toUpperCase()
    };

    rows.forEach(row => {
        const cells = row.cells;
        if (!cells || cells.length < 8) return;
        const methodMatch = !filters.method || cells[1].textContent.toUpperCase().includes(filters.method);
        const manufactureMatch = !filters.manufacture || cells[2].textContent.toUpperCase().includes(filters.manufacture);
        const typeMatch = !filters.type || cells[3].textContent.toUpperCase().includes(filters.type);
        const nameMatch = !filters.name || cells[4].textContent.toUpperCase().includes(filters.name);
        const serialMatch = !filters.serial || cells[5].textContent.toUpperCase().includes(filters.serial);
        const locationMatch = !filters.location || cells[7].textContent.toUpperCase().includes(filters.location);
        const statusMatch = !filters.status || cells[8].textContent.toUpperCase().includes(filters.status);
        row.style.display = methodMatch && manufactureMatch && typeMatch &&
        nameMatch && serialMatch && locationMatch && statusMatch ? "" : "none";
    });
}

// Использование:
function HotSearchingBase() {
    HotSearching(
        "myTableBase",
        "hot_searching_method_base",
        "hot_searching_manufacture_base",
        "hot_searching_type_base",
        "hot_searching_name_base",
        "hot_searching_serial_base",
        "hot_searching_location_base",
        "hot_searching_status_base"
    );
}

// Кэшируем данные таблицы при первой загрузке
let cachedTableData = null;

function cacheTableData() {
    if (cachedTableData) return cachedTableData;

    const tables = {};
    ['Base', 'Send', 'Edit', 'Delete'].forEach(type => {
        const table = document.getElementById(`myTable${type}`);
        if (table) {
            const rows = Array.from(table.querySelectorAll("tbody tr")).map(row => {
                const cells = row.cells;
                return {
                    element: row,
                    method: cells[1]?.textContent,
                    location: cells[7]?.textContent
                };
            });
            tables[type.toLowerCase()] = rows;
        }
    });

    cachedTableData = tables;
    return tables;
}

function applyFilters(filters) {
    const tables = cacheTableData();

    Object.entries(tables).forEach(([type, rows]) => {
        rows.forEach(rowData => {
            const methodMatch = !filters.method.length || filters.method.includes(rowData.method);
            const locationMatch = !filters.location.length || filters.location.includes(rowData.location);
            rowData.element.style.display = methodMatch && locationMatch ? "" : "none";
        });
    });
}

function getFilter() {
    const getCheckedValues = name => {
        const checkboxes = Array.from(document.getElementsByName(`Check${name}`));
        const labels = Array.from(document.getElementsByName(`label_${name.toLowerCase()}`));

        return checkboxes
            .map((checkbox, i) => checkbox.checked ? labels[i]?.textContent : null)
            .filter(Boolean);
    };

    const filters = {
        method: getCheckedValues('Method'),
        location: getCheckedValues('Location'),
    };

    applyFilters(filters);
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
    var btn_method = document.getElementById('button_method');
    var btn_location = document.getElementById('button_location');
    btn_method.classList.add('active');
    btn_method.ariaPressed = 'true';
    btn_location.classList.add('active');
    btn_location.ariaPressed = 'true';
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
    var btn_method = document.getElementById('button_method');
    var btn_location = document.getElementById('button_location');
    btn_method.classList.remove('active');
    btn_method.ariaPressed = 'false';
    btn_location.classList.remove('active');
    btn_location.ariaPressed = 'false';
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
            equipment_send.push(document.getElementById("myTableBase").rows[i + 1].cells[10].innerText)
        }
    } else {
        for (var i = 0; i < check_all_equipment.length; i++) {
            check_all_equipment[i].checked = false
            index_check_send = 0
        }
    }
    if (index_check_send == 0) {
        document.getElementById('button-send').innerHTML = '<i class="bi bi-truck" style="font-size: 1em; width: 150px;"><i/>'
        document.getElementById('button-send').disabled = true
    } else {
        document.getElementById('button-send').innerHTML = `<i class="bi bi-truck" style="font-size: 1em; width: 150px;"> ${index_check_send}<i/>`
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
            equipment_send.push(document.getElementById("myTableBase").rows[i + 1].cells[10].innerText)
        }
        if (index_check_send == 0) {
            check_box_send_all[0].checked = false
        } else {
            check_box_send_all[0].checked = true
        }
    }
    if (index_check_send == 0) {
        document.getElementById('button-send').innerHTML = '<i class="bi bi-truck" style="font-size: 1em; width: 150px;"><i/>'
        document.getElementById('button-send').disabled = true
    } else {
        document.getElementById('button-send').innerHTML = `<i class="bi bi-truck" style="font-size: 1em; width: 150px;"> ${index_check_send}<i/>`
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
