let xhr = new XMLHttpRequest();
xhr.open('Get','http://127.0.0.1:5555/api/environment/')
xhr.send()
xhr.onload = function() {
    if(xhr.status != 200){
        alert('Error ${xhr.status}: ${xhr.statusText}');
    }else{
        alert('Done, got ${xhr.response.length} bytes');
    }
}

xhr.onprogress = function(event){
    if (event.lengthComputable){
        alert('Received ${event.loaded} of ${event.total} bytes')
    } else {
        alert('Recieved ${event.loaded}')
    }
}

xhr.onerror = function () {
    alert("Request failed");

}
var chartCanvas1 = document.getElementById('Device-Load_Pie')
        var barData = {
            labels: ['Cpu Usage','Idle'],
            datasets: [{
                label: 'Current',
                data: [36,64],
                borderWidth: 1,
                borderAlign: 'inner',
                backgroundColor: [
                    'rgba(239, 214, 172, 0.5)',
                    'rgba(196, 73, 0, 0.5)',
                ],
                borderColor: [
                    'rgba(239, 214, 172, 1)',
                    'rgba(196, 73, 0, 1)',
                ],
            }],
        }

        var barOptions = {}

        var myChart1 = new Chart(chartCanvas1, {
            type: 'pie',
            data: barData,
            options: barOptions,
        })