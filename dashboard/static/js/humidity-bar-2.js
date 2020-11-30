let urlHum = 'http://192.168.1.14:5000/api/humidity'
let methodHum = 'GET'
let typeOfResponseHum = 'json'

let xhrHum = new XMLHttpRequest()
xhrHum.open(methodHum, urlHum)
xhrHum.responseType = typeOfResponseHum
xhrHum.send()
xhrHum.onload = function () {
    let responseObj = xhrHum.response;
    console.log(responseObj)
    for (let responseNumber in responseObj) {
        let response = responseObj[responseNumber]
        var humidity = response
        createHum(humidity)
    }

};
xhrHum.onerror = function () {
    alert("Request failed");

}
function createHum(humidity) {
 var humidityChartCanvas = document.getElementById('Humidity-Bar')
        var barData = {
            datasets: [{
                label: 'Current',
                data: [+(humidity)],
                borderWidth: 1,
                backgroundColor: [
                    'rgba(4, 21, 31, 0.4)',
                ],
                borderColor: [
                    'rgba(4, 21, 31, 1)',
                ],
            }],
        }

        var barOptions = {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true,
                    },
                }],
            },
        }

        var myChart1 = new Chart(humidityChartCanvas, {
            type: 'bar',
            data: barData,
            options: barOptions,
        })
}