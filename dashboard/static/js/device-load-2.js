let urlLoad = 'http://172.20.20.107:5000/api/device-load'
let methodLoad = 'GET'
let typeOfResponseLoad = 'json'

let xhrLoad = new XMLHttpRequest()
xhrLoad.open(methodLoad, urlLoad)
xhrLoad.responseType = typeOfResponseLoad
xhrLoad.send()
xhrLoad.onload = function () {
    let responseObj = xhrLoad.response;
    console.log(responseObj)
    for (let responseNumber in responseObj) {
        let response = responseObj[responseNumber]
        var load = response
        createLoad(load)
    }

};
xhrLoad.onerror = function () {
    alert("Request failed");

}

function createLoad(load) {
var pieLoadCanvas = document.getElementById('Device-Load_Pie')
        var barData = {
            labels: ['Cpu Usage','Idle'],
            datasets: [{
                label: 'Current',
                data: [+(load),100-+(load)],
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

        var myChart1 = new Chart(pieLoadCanvas, {
            type: 'pie',
            data: barData,
            options: barOptions,
        })
        }
