var total = 0;
var prices_day = {
    'auger': 80,
    'nailgun': 40,
    'tilesaw': 60,
    'air compressor': 120,
    'generator': 200
};
var prices_week = {
    'auger': 40,
    'nailgun': 30,
    'tilesaw': 45,
    'air compressor': 90,
    'generator': 150
};
var prices_month = {
    'auger': 20,
    'nailgun': 15,
    'tilesaw': 30,
    'air compressor': 60,
    'generator': 100
};
$("#submit").click(function () {
    var selectedText = $("#tools").find("option:selected").text();
    var selectedValue = $("#tools").val();
    var enteredDays = $("#num_days").val();
    $.post("rent_tool/", {name: selectedText, days: enteredDays}, function () {
        if (enteredDays === 1) {
            total=(prices_day[selectedValue]*enteredDays)*1.07
        }
        else if (enteredDays > 1 && enteredDays < 8) {
            total=(prices_week[selectedValue]*enteredDays)*1.07
        }
        else {
            total=(prices_month[selectedValue]*enteredDays)*1.07
        }
        $("#rented_modal").html("Item: " + selectedText + "<br/>Days Renting: " + enteredDays + "<br/>Amount Owed: $" + (total).toFixed(2));
    });
});
