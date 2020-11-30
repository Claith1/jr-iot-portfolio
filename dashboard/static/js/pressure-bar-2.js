let urlPres = 'http://192.168.1.14:5000/api/pressure'
let methodPres = 'GET'
let typeOfResponsePres = 'json'

let xhrPres = new XMLHttpRequest()
xhrPres.open(methodPres, urlPres)
xhrPres.responseType = typeOfResponsePres
xhrPres.send()
xhrPres.onload = function () {
    let responseObj = xhrPres.response;
    console.log(responseObj)
    for (let responseNumber in responseObj) {
        let response = responseObj[responseNumber]
        var pressure = response
        createPress(pressure)
    }

};
xhrPres.onerror = function () {
    alert("Request failed");

}
function createPress(pressure)
{
    var pressureChartCanvas = document.getElementById('Pressure-Bar')

        var barData = {
                datasets: [{
                    label: 'Current',
                    data: [+(pressure)],
                    borderWidth: 1,
                    backgroundColor: [
                        'rgba(67, 37, 52, 0.4)',
                    ],
                    borderColor: [
                        'rgba(67, 37, 52, 1)',
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

            var myChart1 = new Chart(pressureChartCanvas, {
                type: 'bar',
                data: barData,
                options: barOptions,
            })
        }
