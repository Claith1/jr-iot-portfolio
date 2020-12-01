let urlTemp = 'http://172.20.20.107:5000/api/temperature'
let methodTemp = 'GET'
let typeOfResponseTemp = 'json'

let xhrTemp = new XMLHttpRequest()
xhrTemp.open(methodTemp, urlTemp)
xhrTemp.responseType = typeOfResponseTemp
xhrTemp.send()
xhrTemp.onload = function () {
    let responseObj = xhrTemp.response;
    console.log(responseObj)
    for (let responseNumber in responseObj) {
        let response = responseObj[responseNumber]
        var temp = response
        createTemp(temp)
    }

};
xhrTemp.onerror = function () {
    alert("Request failed");

}
function createTemp(temp) {
var temperatureChartCanvas = document.getElementById('Temperature-Bar')
        var barData = {
            datasets: [{
                label: 'Current',
                data: [+(temp)],
                borderWidth: 1,
                backgroundColor: [
                    'rgba(24, 58, 55, 0.4)',
                ],
                borderColor: [
                    'rgba(24, 58, 55, 1)',
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

        var myChart1 = new Chart(temperatureChartCanvas, {
            type: 'bar',
            data: barData,
            options: barOptions,
        })
        }