const calendar = document.getElementById('calendar');

// Function to generate the calendar
function generateCalendar(year, month) {
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const firstDay   
 = new Date(year, month, 1).getDay();   


const table = document.createElement('table');
let tr = document.createElement('tr');

// Add empty cells for the days before the first day of the month
for (let i = 0; i < firstDay; i++) {
    let td = document.createElement('td');
    td.textContent = '';
    tr.appendChild(td);
}

// Add cells for the days of the month
for (let day = 1; day <= daysInMonth; day++) {
    let td = document.createElement('td');
    td.textContent = day;
    // Add event listeners or styling as needed
    tr.appendChild(td);

    if (day % 7 === 0) {
        table.appendChild(tr);
        tr = document.createElement('tr');
    }
}

// Add the final row to the table if necessary
if (tr.children.length > 0) {
    table.appendChild(tr);
}

calendar.appendChild(table);
}

// Initial calendar generation
generateCalendar(new Date().getFullYear(), new Date().getMonth());