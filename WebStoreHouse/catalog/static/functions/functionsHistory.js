// Оптимизированная версия HotSearching
function HotSearching(tableId, dateId, timeId, fromId, whoId, crudId, toId, whomId, methodId, nameId, serialId,
                     statusId, locationId, typeId, manufactureId) {
    const table = document.getElementById(tableId);
    if (!table) return;

    const rows = table.querySelectorAll("tbody tr");
    if (!rows.length) return;

    const filters = {
        date: document.getElementById(dateId).value.toUpperCase(),
        time: document.getElementById(timeId).value.toUpperCase(),
        from: document.getElementById(fromId).value.toUpperCase(),
        who: document.getElementById(whoId).value.toUpperCase(),
        crud: document.getElementById(crudId).value.toUpperCase(),
        to: document.getElementById(toId).value.toUpperCase(),
        whom: document.getElementById(whomId).value.toUpperCase(),
        method: document.getElementById(methodId).value.toUpperCase(),
        name: document.getElementById(nameId).value.toUpperCase(),
        serial: document.getElementById(serialId).value.toUpperCase(),
        status: document.getElementById(statusId).value.toUpperCase(),
        location: document.getElementById(locationId).value.toUpperCase(),
        type: document.getElementById(typeId).value.toUpperCase(),
        manufacture: document.getElementById(manufactureId).value.toUpperCase(),
    };

    rows.forEach(row => {
        const cells = row.cells;
        if (!cells || cells.length < 8) return;
        const dateMatch = !filters.date || cells[1].textContent.toUpperCase().includes(filters.date);
        const timeMatch = !filters.time || cells[2].textContent.toUpperCase().includes(filters.time);
        const fromMatch = !filters.from || cells[3].textContent.toUpperCase().includes(filters.from);
        const whoMatch = !filters.who || cells[4].textContent.toUpperCase().includes(filters.who);
        const crudMatch = !filters.crud || cells[5].textContent.toUpperCase().includes(filters.crud);
        const toMatch = !filters.to || cells[6].textContent.toUpperCase().includes(filters.to);
        const whomMatch = !filters.whom || cells[7].textContent.toUpperCase().includes(filters.whom);
        const methodMatch = !filters.method || cells[8].textContent.toUpperCase().includes(filters.method);
        const nameMatch = !filters.name || cells[9].textContent.toUpperCase().includes(filters.name);
        const serialMatch = !filters.serial || cells[10].textContent.toUpperCase().includes(filters.serial);
        const statusMatch = !filters.status || cells[11].textContent.toUpperCase().includes(filters.status);
        const locationMatch = !filters.location || cells[13].textContent.toUpperCase().includes(filters.location);
        const typeMatch = !filters.type || cells[15].textContent.toUpperCase().includes(filters.type);
        const manufactureMatch = !filters.manufacture || cells[16].textContent.toUpperCase().includes(filters.manufacture);
        row.style.display = dateMatch && timeMatch && fromMatch && whoMatch && crudMatch && toMatch && whomMatch &&
                            methodMatch && manufactureMatch && typeMatch && nameMatch && serialMatch &&
                            locationMatch && statusMatch ? "" : "none";
    });
}

// Использование:
function HotSearchingHistory() {
    HotSearching(
        "myTableHistory",
        "hot_searching_date_history",
        "hot_searching_time_history",
        "hot_searching_from_history",
        "hot_searching_who_history",
        "hot_searching_crud_history",
        "hot_searching_to_history",
        "hot_searching_whom_history",
        "hot_searching_method_history",
        "hot_searching_name_history",
        "hot_searching_serial_history",
        "hot_searching_status_history",
        "hot_searching_location_history",
        "hot_searching_type_history",
        "hot_searching_manufacture_history",
    );
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
