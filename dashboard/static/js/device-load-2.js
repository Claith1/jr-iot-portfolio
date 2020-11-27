let url = 'http://192.168.1.14:5000/api/device-load'
let method = 'GET'
let typeOfResponse = 'json'

let xhr = new XMLHttpRequest()
xhr.open(method, url)
xhr.responseType = typeOfResponse
xhr.send()
xhr.onload = function () {
    let responseObj = xhr.response;
    console.log(responseObj)
    for (let responseNumber in responseObj) {
        let response = responseObj[responseNumber]
        var cpuLoad = response
        var chartCanvas1 = document.getElementById('Device-Load_Pie')
        var barData = {
            labels: ['Cpu Usage','Idle'],
            datasets: [{
                label: 'Current',
                data: [cpuLoad,100-cpuLoad],
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
    }

};
xhr.onerror = function () {
    alert("Request failed");

}

